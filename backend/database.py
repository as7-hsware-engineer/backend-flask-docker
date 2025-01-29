import sqlite3

def create_database():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)''')
    conn.commit()
    conn.close()