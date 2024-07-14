import sqlite3
from datetime import datetime

conn = sqlite3.connect('adega.db')
cursor = conn.cursor()

# Adicionar uma venda manualmente
produto = "Vinho Tinto"
quantidade = 2
preco = 50.00
data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute('INSERT INTO vendas (produto, quantidade, preco, data_venda) VALUES (?, ?, ?, ?)', 
               (produto, quantidade, preco, data_venda))

conn.commit()
conn.close()
