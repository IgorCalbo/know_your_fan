import os
from flask import Flask, render_template, request
from models import db, Usuario
from PIL import Image, ImageOps
import pytesseract


# Flask setup
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

# OCR setup
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# DB init 
db.init_app(app)

# Cria tabelas
with app.app_context():
    db.create_all()

# Rotas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registrar", methods=['POST'])
def registrar():
    nome = request.form.get("nome")
    endereco = request.form.get("endereco")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    interesses = request.form.get("interesses")
    eventos_compras = request.form.get("eventosOuCompras")
    documento = request.files.get("documento")

    caminho = os.path.join(app.config['UPLOAD_FOLDER'], documento.filename)
    documento.save(caminho)

    # Chama funcao que utiliza bibloteca pytesseract
    if validar(nome, caminho):
        usuario = Usuario(
            nome = nome, 
            endereco = endereco, 
            cpf = cpf, email = email, 
            interesses = interesses, 
            eventos_compras = eventos_compras, 
            caminho_documento = caminho,
        )
        db.session.add(usuario)
        db.session.commit()
    else:
        return "Documento invalido"

    return render_template("sucesso.html")

def validar(nome, caminho):
    # adicionando contraste e um tom de cinza a imagem para facilitar visualizacao
    imagem = Image.open(caminho).convert('L')
    imagem = ImageOps.autocontrast(imagem)
    texto = pytesseract.image_to_string(imagem)

    if nome.lower() in texto.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)

