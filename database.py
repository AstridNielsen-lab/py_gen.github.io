import sqlite3

def init_db():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    
    # Criação da tabela de estoque
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    ''')
    
    # Criação da tabela de vendas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        data_venda TEXT NOT NULL
    )
    ''')

    # Criação da tabela de fornecedores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')    
    
    # Criação da tabela de lojas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lojas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        contato TEXT NOT NULL
    )
    ''')

    # Criação da tabela de entradas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        data_entrada TEXT NOT NULL
    )
    ''')
    
    # Criação da tabela de saídas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS saidas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_saida TEXT NOT NULL
    )
    ''')

    # Criação da tabela de controle de estoque
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS controle_estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        tipo_movimento TEXT NOT NULL,  -- 'entrada' ou 'saida'
        quantidade INTEGER NOT NULL,
        data_movimento TEXT NOT NULL
    )
    ''')

    # Criação da tabela de dashboard de vendas gerais
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dash_vg (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        total_vendas REAL NOT NULL,
        total_estoque REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
