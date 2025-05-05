# Know Your Fan
Know Your Fan é uma aplicação web desenvolvida com Flask, projetada para analisar e visualizar dados relacionados a fãs e suas interações.

## Tecnologias Utilizadas
Python 3

Flask

Jinja2

HTML5, CSS3

SQLite

## 📁 Estrutura do Projeto
know_your_fan/
├── app.py             
├── models.py          
├── requirements.txt   
├── instance/          
├── static/            
├── templates/         
└── uploads/ 

## Instalação e Execução
Clone o repositório:
git clone https://github.com/IgorCalbo/know_your_fan.git

cd know_your_fan

Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv

source venv/bin/activate  # Para Linux/Mac

venv\Scripts\activate     # Para Windows

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação:
python app.py

Acesse no navegador:
http://localhost:5000

## Funcionalidades
Upload e processamento de dados de fãs.
Visualização de informações através de templates HTML.
Armazenamento de dados utilizando SQLite.
