from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatabaseConnection:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app)

    def get_db(self):
        return db

    def initialize_db(self, app):
        try:
            with app.app_context():
                db.create_all()
                print("Banco de dados inicializado com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar o banco de dados: {e}")
            raise 