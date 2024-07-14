from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import datetime
from database import init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar flash messages

# Inicializa o banco de dados
init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM estoque')
    produtos = cursor.fetchall()

    cursor.execute('SELECT * FROM vendas')
    vendas = cursor.fetchall()

    conn.close()
    return render_template('index.html', produtos=produtos, vendas=vendas)

@app.route('/add', methods=['POST'])
def add_produto():
    produto = request.form['produto']
    quantidade = int(request.form['quantidade'])
    preco = float(request.form['preco'])

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estoque (produto, quantidade, preco) VALUES (?, ?, ?)', (produto, quantidade, preco))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/venda', methods=['POST'])
def registrar_venda():
    produto = request.form['produto']
    quantidade = int(request.form['quantidade'])

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, quantidade, preco FROM estoque WHERE produto = ?', (produto,))
    resultado = cursor.fetchone()

    if resultado:
        id_produto, estoque_atual, preco = resultado
        if quantidade > estoque_atual:
            flash('Quantidade maior que o estoque disponível!', 'error')
            return redirect('/cont_estoque')

        novo_estoque = estoque_atual - quantidade
        cursor.execute('UPDATE estoque SET quantidade = ? WHERE id = ?', (novo_estoque, id_produto))

        cursor.execute('INSERT INTO vendas (produto, quantidade, preco, data_venda) VALUES (?, ?, ?, ?)',
                       (produto, quantidade, preco, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()
    return redirect('/cont_estoque')

@app.route('/instrucoes')
def instrucoes():
    return render_template('instrucoes.html')

@app.route('/prod')
def lista_produtos():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM estoque')
    produtos = cursor.fetchall()

    conn.close()
    return render_template('prod.html', produtos=produtos)

@app.route('/forn')
def lista_fornecedores():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM fornecedores')
    fornecedores = cursor.fetchall()

    conn.close()
    return render_template('forn.html', fornecedores=fornecedores)

@app.route('/fornecedor', methods=['POST'])
def registrar_fornecedor():
    nome = request.form['nome']
    contato = request.form['contato']
    email = request.form['email']

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO fornecedores (nome, contato, email) VALUES (?, ?, ?)', (nome, contato, email))
    
    conn.commit()
    conn.close()

    return redirect('/forn')

@app.route('/lojas')
def lista_lojas():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM lojas')
    lojas = cursor.fetchall()

    conn.close()
    return render_template('lojas.html', lojas=lojas)

@app.route('/loja', methods=['POST'])
def registrar_loja():
    nome = request.form['nome']
    endereco = request.form['endereco']
    contato = request.form['contato']

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO lojas (nome, endereco, contato) VALUES (?, ?, ?)', (nome, endereco, contato))
    
    conn.commit()
    conn.close()

    return redirect('/lojas')

@app.route('/entradas')
def lista_entradas():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM entradas')
    entradas = cursor.fetchall()

    conn.close()
    return render_template('entradas.html', entradas=entradas)

@app.route('/entrada', methods=['POST'])
def registrar_entrada():
    produto = request.form['produto']
    quantidade = int(request.form['quantidade'])
    preco = float(request.form['preco'])

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO estoque (produto, quantidade, preco) VALUES (?, ?, ?) ON CONFLICT(produto) DO UPDATE SET quantidade = quantidade + ?',
                   (produto, quantidade, preco, quantidade))
    
    cursor.execute('INSERT INTO entradas (produto, quantidade, preco, data_entrada) VALUES (?, ?, ?, ?)',
                   (produto, quantidade, preco, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    conn.close()

    return redirect('/entradas')

@app.route('/saidas')
def lista_saidas():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM saidas')
    saidas = cursor.fetchall()

    conn.close()
    return render_template('saidas.html', saidas=saidas)

@app.route('/saida', methods=['POST'])
def registrar_saida():
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    data_saida = request.form['data_saida']

    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO saidas (descricao, valor, data_saida) VALUES (?, ?, ?)', 
                   (descricao, valor, data_saida))
    
    conn.commit()
    conn.close()

    return redirect('/saidas')

@app.route('/cont_estoque')
def cont_estoque():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM estoque')
    estoque = cursor.fetchall()
    
    conn.close()
    return render_template('cont_estoque.html', estoque=estoque)

@app.route('/dashboard')
def dashboard():
    estoque = buscar_estoque()
    vendas = buscar_vendas()
    saidas = buscar_saidas()
    
    # Teste simples
    print(f"Estoque: {estoque}")
    print(f"Vendas: {vendas}")
    print(f"Saídas: {saidas}")

    return render_template('dash_vg.html', estoque=estoque, vendas=vendas, saidas=saidas)


@app.route('/dash_estoque')
def dash_estoque():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM estoque')
    total_produtos = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM entradas')
    total_entradas = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM saidas')
    total_saidas = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM vendas')
    total_vendas = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM estoque WHERE quantidade < 5')
    produtos_baixo_estoque = cursor.fetchall()

    conn.close()

    return render_template('dash_estoque.html',
                           total_produtos=total_produtos,
                           total_entradas=total_entradas,
                           total_saidas=total_saidas,
                           total_vendas=total_vendas,
                           produtos_baixo_estoque=produtos_baixo_estoque)

@app.route('/dash_resultados')
def dash_resultados():
    return render_template('dash_resultados.html')

@app.route('/auxiliar')
def auxiliar():
    return render_template('auxiliar.html')

def buscar_estoque():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estoque")
    estoque = cursor.fetchall()
    conn.close()
    return estoque

def buscar_vendas():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    conn.close()
    return vendas

def buscar_saidas():
    conn = sqlite3.connect('adega.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM saidas")
    saidas = cursor.fetchall()
    conn.close()
    return saidas

if __name__ == '__main__':
    app.run(debug=True)
