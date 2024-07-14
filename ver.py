import sqlite3

conn = sqlite3.connect('adega.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM vendas')
vendas = cursor.fetchall()

print(vendas)

conn.close()
