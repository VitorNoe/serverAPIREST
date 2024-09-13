from flask import Flask
from flask_jwt_extended import JWTManager
from database import DatabaseConnection
from api_handler import LeadAPIHandler
from auth import init_auth_routes

init_auth_routes(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'  
jwt = JWTManager(app)
db_connection = DatabaseConnection(app)

try:
    db_connection.initialize_db(app)
except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")

api_handler = LeadAPIHandler(app, db_connection.get_db())

if __name__ == '__main__':
    app.run(debug=True)