from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))
    cpf = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(100), unique=True)
    interesses = db.Column(db.String(1000))
    eventos_compras = db.Column(db.String(1000))
    caminho_documento = db.Column(db.String(255))
    data_cadastro = db.Column(db.DateTime, default=db.func.now())


