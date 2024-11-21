from models import User, db
import os
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt() # Crear una instancia de Bcrypt

def create_admin_user():
    admin_username = os.getenv('ADMIN_USERNAME', 'defaultadmin')
    admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    admin_password = os.getenv('ADMIN_PASSWORD', 'defaultpassword')
    if not admin_username or not admin_email or not admin_password:
        print("Admin credentials not set in environment variables.")
        return

    if User.query.filter_by(email=admin_email).first() is None:
        hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        admin = User(username=admin_username, email=admin_email, password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")