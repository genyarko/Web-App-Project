import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'mssql+pyodbc://@Geo\\SQLEXPRESS/Ada_App?driver=ODBC Driver 17 for SQL Server&Trusted_Connection=yes')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

