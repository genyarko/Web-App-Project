from flask import Flask
from config import Config
from models import db, User  # Ensure User is imported
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object(Config)

# Print configuration for debugging
print(f"SECRET_KEY: {app.config['SECRET_KEY']}")
print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
from routes.auth import auth_bp
from routes.tasks import tasks_bp
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
