from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Conectar ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="database",  # Nome do serviço no docker-compose
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn

# Rota principal com o formulário e a tabela
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Se o método for POST, insira a cidade no banco de dados
    if request.method == "POST":
        cidade = request.form["cidade"]
        cur.execute("INSERT INTO minha_tabela (nome) VALUES (%s)", (cidade,))
        conn.commit()

    # Buscar todas as cidades para exibir na tabela
    cur.execute("SELECT * FROM minha_tabela ORDER BY id;")
    cidades = cur.fetchall()
    conn.close()

    return render_template("index.html", cidades=cidades)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
