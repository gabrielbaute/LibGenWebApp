# LibGenWebApp

LibGenWebApp es una interfaz web para la API de LibGen desarrollada por Harrison Broadbent. Esta aplicación permite buscar libros y artículos en la biblioteca de LibGen de manera amigable y eficiente. La aplicación está en desarrollo continuo y se agradece mucho el trabajo y aporte de Harrison Broadbent.

## Características

- Búsqueda de libros y artículos por autor y título.
- Filtros avanzados de búsqueda por idioma, año, y formato.
- Historial de búsquedas del usuario.
- Modo oscuro y modo claro.
- Restablecimiento de contraseña por correo electrónico con tokens válidos por 30 minutos.

## Instalación

1. **Clonar el repositorio**
    ```sh
    git clone https://github.com/yourusername/LibGenWebApp.git
    cd LibGenWebApp
    ```

2. **Crear y activar un entorno virtual**
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno**
   - Crea un archivo `.env` en el directorio raíz del proyecto y agrega las siguientes líneas:
   ```env
   # Flask
   FLASKPORT=5000
   SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
   FLASK_DOMAIN=http://localhost:{FLASKPORT}
   SECRET_KEY=your-generated-secret-key
   DEBUG=False

   # Admin credentials
   ADMIN_USERNAME='admin'
   ADMIN_EMAIL='admin@mail.com'
   ADMIN_PASSWORD='admin'

   # SMTP configuration
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USE_SSL=False
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-password
   MAIL_DEFAULT_SENDER=noreply@example.com
   ```

5. **Generar la clave secreta**
   - Ejecuta el script `generate_secret_key.py` y copia la clave generada en el archivo `.env`:
   
   ```sh
   python generate_secret_key.py
   ```
   - Añade la línea `SECRET_KEY=your-generated-secret-key` en tu archivo `.env`.

6. **Inicializar la base de datos**
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

7. **Ejecutar la aplicación**
   ```sh
   flask run
   ```

## Estructura de Archivos

```plaintext
LibGenWebApp/
├── app.py
├── routes.py
├── models.py
├── forms.py
├── mail.py
├── loadadmin.py
├── generate_secret_key.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── reset_request.html
│   ├── reset_token.html
│   ├── authorsearch.html
│   ├── titlesearch.html
│   ├── results.html
│   ├── history.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── theme.js
│   └── images/
│       └── logo.png
├── .env
├── requirements.txt
├── README.md
```

## Variables de Entorno

| Nombre                     | Valor por Defecto          | Descripción                                                |
|----------------------------|----------------------------|------------------------------------------------------------|
| `FLASKPORT`                | `5000`                     | Puerto en el que se ejecuta la aplicación Flask.           |
| `SQLALCHEMY_DATABASE_URI`  | `sqlite:///site.db`        | URI de la base de datos.                                   |
| `FLASK_DOMAIN`             | `http://localhost:{FLASKPORT}` | Dominio de la aplicación Flask.                             |
| `SECRET_KEY`               | `your-generated-secret-key` | Clave secreta para la aplicación Flask.                     |
| `DEBUG`                    | `False`                    | Modo de depuración de Flask.                               |
| `ADMIN_USERNAME`           | `admin`                    | Nombre de usuario del administrador por defecto.           |
| `ADMIN_EMAIL`              | `admin@mail.com`           | Correo electrónico del administrador por defecto.          |
| `ADMIN_PASSWORD`           | `admin`                    | Contraseña del administrador por defecto.                  |
| `MAIL_SERVER`              | `smtp.example.com`         | Servidor SMTP para enviar correos.                         |
| `MAIL_PORT`                | `587`                      | Puerto del servidor SMTP.                                  |
| `MAIL_USE_TLS`             | `True`                     | Usar TLS para el servidor SMTP.                            |
| `MAIL_USE_SSL`             | `False`                    | Usar SSL para el servidor SMTP.                            |
| `MAIL_USERNAME`            | `your-email@example.com`   | Nombre de usuario para el servidor SMTP.                   |
| `MAIL_PASSWORD`            | `your-password`            | Contraseña para el servidor SMTP.                          |
| `MAIL_DEFAULT_SENDER`      | `noreply@example.com`      | Dirección de correo del remitente por defecto.             |

## Importancia de la Clave Secreta

La clave secreta (`SECRET_KEY`) es fundamental para la seguridad de tu aplicación Flask. Se utiliza para firmar cookies, tokens y otras tareas de seguridad. Asegúrate de generar una clave secreta segura usando el script `generate_secret_key.py` y guardarla en el archivo `.env` para que no se exponga accidentalmente en el código fuente.

## Agradecimientos

Este proyecto se basa en la [API de LibGen](https://github.com/harrison-broadbent/libgen-api) desarrollada por [Harrison Broadbent](https://github.com/harrison-broadbent). Agradecemos enormemente su trabajo y contribución.

¡Gracias por usar LibGenWebApp!