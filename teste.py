import sqlite3

conn = sqlite3.connect('adega.db')
cursor = conn.cursor()

# Listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print(tabelas)

conn.close()
