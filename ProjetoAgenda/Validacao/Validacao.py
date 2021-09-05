import sqlite3
from Banco.BancoDados import BancoDados
conexao = sqlite3.connect(r'C:\Users\unisanta\Desktop\ProjetoAgenda\Banco\agenda.db')
cursor = conexao.cursor()

class Validacao:
    def __init__(self):
        print("")
 
    
    def formatarTelefone(self,tel):
        print(tel.isdigit())
        if(len(tel)== 11 and tel.isdigit()==True):
            return True
        elif(tel.isdigit()==False or  len(tel)!= 11):
            return False
            print("Digite só numeros com 11 digitos")
                
      
           
    def formatarNome(self,nome):
        if(len(nome)<30 and nome.isalpha()==True):
            return True
        else:
            return False
            print("Digite apenas letras com menos de 30 caracteres")
        
        
    def formatarEmail(self,email):
        contem = 0
        for x in range(len(email)):
            if(email[x]=='@'):
                contem = contem+1
        if(len(email)<40 and len(email)>10 and contem==1):
            return True
        else:
            return False
            print("Email tem que ter entre 10 e 40 caracteres e UM '@'")
        
    def formatarID(self,idContato):
        if(idContato.isdigit()==True):
            return True
        else:
            print("Digite apenas numeros\n")
            return False
            
        
        

