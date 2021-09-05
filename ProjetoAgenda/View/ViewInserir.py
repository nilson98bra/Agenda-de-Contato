from Validacao.Validacao import Validacao
validacao = Validacao()
class ViewInserir:
     def __init__(self,_agenda):
          nome =input("\nInsira o seu nome: ")
          nomeProvisiorio = ''
          for x in range(len(nome)):
               if(nome[x]!= " "):
                    nomeProvisiorio = nomeProvisiorio + nome[x]
          while(validacao.formatarNome(nomeProvisiorio)==False):
               nomeProvisiorio = ""
               print("Erro..\nNome em branco ou \nCom mais de 30 caracteres ou \nNome alem de letras")
               nome = input("\nInsira o seu nome: ")
               for x in range(len(nome)):
                    if(nome[x]!= " "):
                         nomeProvisiorio = nomeProvisiorio + nome[x]
          tel = input("Insira seu DDD + Telefone: ")
          if(validacao.formatarTelefone(tel)==False):
               x=1
               while(x==1):
                    if(validacao.formatarTelefone(tel)==False):
                         print("Digite só numeros com 11 digitos\n")   
                    tel = input("Insira seu DDD + Telefone: ")
                    if(validacao.formatarTelefone(tel)==False):
                         x=1
                    else:
                         x=0
                    
               
          email = input("Insira seu email: ")
          if(validacao.formatarEmail(email)==False):
               while(validacao.formatarEmail(email)==False):
                    print("Erro..\nMenor que 10 caracteres ou Maior que 40 ou contem mais de um @ ")
                    email = input("Insira seu email: ")
          tel = '(' + tel[0:2] + ')'  +   tel[2:]
          _agenda.inserirContato(nome.capitalize(),tel,email)
          print("Cadastrado\n")
       
       
        
