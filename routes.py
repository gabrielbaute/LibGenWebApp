from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from forms import TitleSearchForm, AuthorSearchForm, LoginForm, RegistrationForm, RequestResetForm, ResetPasswordForm
from models import User, Searches
from datetime import datetime
import email_validator, smtplib
from mail import send_reset_email

def init_routes(app, libgen, db, login_manager, bcrypt):
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def libhome():
        return render_template('index.html')
    
    @app.route('/authorsearch', methods=['GET', 'POST'])
    @login_required
    def authorsearch():
        form = AuthorSearchForm()
        if form.validate_on_submit():
            filters = {}
            if form.language.data:
                filters['Language'] = form.language.data
            if form.year.data:
                filters['Year'] = form.year.data
            if form.extension.data:
                filters['Extension'] = form.extension.data

            results = libgen.search_author_filtered(form.author.data, filters, exact_match=False)
            new_search = Searches(item=form.author.data, user_id=current_user.id)
            db.session.add(new_search)
            db.session.commit()
            return render_template('results.html', results=results)
        return render_template('authorsearch.html', form=form)

    @app.route('/titlesearch', methods=['GET', 'POST'])
    @login_required
    def titlesearch():
        form = TitleSearchForm()
        if form.validate_on_submit():
            filters = {}
            if form.language.data:
                filters['Language'] = form.language.data
            if form.year.data:
                filters['Year'] = form.year.data
            if form.extension.data:
                filters['Extension'] = form.extension.data

            results = libgen.search_title_filtered(form.title.data, filters, exact_match=False)
            new_search = Searches(item=form.title.data, user_id=current_user.id)
            db.session.add(new_search)
            db.session.commit()
            return render_template('results.html', results=results)
        return render_template('titlesearch.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('libhome'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('libhome'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('libhome'))
    
    @app.route('/reset_password', methods=['GET', 'POST'])
    def reset_request():
        if current_user.is_authenticated:
            return redirect(url_for('libhome'))
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                send_reset_email(user)
            flash('An email has been sent with instructions to reset your password.', 'info')
            return redirect(url_for('login'))
        return render_template('reset_request.html', form=form)

    @app.route('/reset_password/<token>', methods=['GET', 'POST'])
    def reset_token(token):
        if current_user.is_authenticated:
            return redirect(url_for('libhome'))
        user = User.verify_reset_token(token)
        if user is None:
            flash('That is an invalid or expired token', 'warning')
            return redirect(url_for('reset_request'))
        
        form = ResetPasswordForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated! You are now able to log in', 'success')
            return redirect(url_for('login'))
        return render_template('reset_token.html', form=form, token=token)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('libhome'))
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/search-result')
    @login_required
    def results():
        return render_template('results.html')
    
    @app.route('/history')
    @login_required
    def history():
        # Recuperar todas las búsquedas del usuario actual
        searches = Searches.query.filter_by(user_id=current_user.id).all()
        return render_template('history.html', searches=searches)