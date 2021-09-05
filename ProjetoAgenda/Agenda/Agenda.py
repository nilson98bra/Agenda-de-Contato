import sqlite3
from Contato.Contato import Contato
from Banco.BancoDados import BancoDados
conexao = sqlite3.connect(r'C:\Users\unisanta\Desktop\ProjetoAgenda\Banco\agenda.db')
cursor = conexao.cursor()

class Agenda:
   
    def __init__(self,_banco):
        self.banco = _banco
        print("")
        
    def inserirContato(self,nome,tel,email):
        contato = Contato(nome,tel,email)
        conexao.execute('INSERT INTO tb_agenda VALUES(NULL,?,?,?)',(contato.nome,contato.tel,contato.email))
        conexao.commit();
            
    def deletarContato(self,idContato):
        conexao.execute('DELETE FROM tb_agenda WHERE id_contato=?',(idContato,))
        conexao.commit();
        
    
    def pesquisarContatoNome(self,nome):
        cursor.execute("SELECT * FROM tb_agenda WHERE nm_nome LIKE ? ORDER BY nm_nome ASC",('%'+nome+'%',))
        resultado = cursor.fetchall()
        for linha in resultado:
             print(linha)
      
    def pesquisarContatoTel(self,tel):
        cursor.execute("SELECT * FROM tb_agenda WHERE nm_telefone = ? ORDER BY nm_nome ASC",(tel,))
        resultado = cursor.fetchall()
        for linha in resultado:
             print(linha)
        if(len(resultado)==0):
            print("\nNenhum contato encontrado\n")
        
    def pesquisarContatoEmail(self,email):
        cursor.execute("SELECT * FROM tb_agenda WHERE nm_email = ? ORDER BY nm_nome ASC",(email,))
        resultado = cursor.fetchall()
        for linha in resultado:
             print(linha)
        if(len(resultado)==0):
            print("\nNenhum contato encontrado\n")
             
    def pesquisarTodosContatos(self):
        cursor.execute("SELECT * FROM tb_agenda ORDER BY nm_nome ASC")
        resultado = cursor.fetchall()
        for linha in resultado:
             print(linha)
        if(len(resultado)==0):
            print("\nNenhum contato encontrado\n")

    def mudarNomeContato(self,idContato,novoNome):
        cursor.execute('UPDATE tb_agenda SET nm_nome = ? WHERE id_contato = ?',(novoNome,idContato,))
        print("id: ",idContato," Nome: ",novoNome)
        print("Nome Mudado")
        conexao.commit()


    def mudarTelContato(self,idContato,novoTel):
        cursor.execute('UPDATE tb_agenda SET nm_telefone = ? WHERE id_contato = ?',(novoTel,idContato,))
        print("Telefone Mudado")
        conexao.commit()
        
    def mudarEmailContato(self,idContato,novoEmail):
        cursor.execute('UPDATE tb_agenda SET nm_email = ? WHERE id_contato =?',(novoEmail,idContato))
        print("Email Mudado")
        conexao.commit()
   
            
       
        
            
