import sqlite3

class BancoDados:
    def __init__(self):
        conexao = sqlite3.connect(r'C:\Users\unisanta\Desktop\ProjetoAgenda\Banco\agenda.db')
        conexao.execute('CREATE TABLE IF NOT EXISTS tb_agenda(id_contato INTEGER PRIMARY KEY AUTOINCREMENT, nm_nome VARCHAR(30), nm_telefone VARCHAR(30), nm_email VARCHAR(30))')
    
       
    def conectar(self):
        conexao = sqlite3.connect(r'C:\Users\unisanta\Desktop\ProjetoAgenda\Banco\agenda.db')
        
