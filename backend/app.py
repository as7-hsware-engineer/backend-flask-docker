from flask import Flask
import database

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá do Backend!"

if __name__ == "__main__":
    database.create_database()  # Cria o banco de dados ao iniciar o backend
    app.run(debug=True, host='0.0.0.0')