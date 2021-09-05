from Validacao.Validacao import Validacao
class ViewUpdate:
     def __init__(self,agenda):
          self.agenda = agenda
          validar = Validacao()
          opcaoUpdate = input("Escolha uma das opçoes: \n1: Mudar o nome: \n2: Mudar o telefone: \n3: Mudar o email: \n")
          while(opcao.isdigit()==False):
               print("Digite apenas numeros: ")
               opcaoUpdate = input("Escolha uma das opçoes: \n1: Mudar o nome: \n2: Mudar o telefone: \n3: Mudar o email: \n")
          if(opcaoUpdate == 1):
               agenda.pesquisarTodosContatos()
               print("\n")
               condicao = input("Digite o seu ID: ")
               while(validar.formatarID(condicao)==False):
                     condicao = input("Digite o seu ID: ")
                     
               novo = input("Digite o novo nome do contato: ")
               while(validar.formatarNome(novo)==False):
                    novo = input("Digite o novo nome do contato: ")
               condicao = int(condicao)   
               print("\n")
               agenda.mudarNomeContato(condicao,novo)
               print("\n")
               agenda.pesquisarTodosContatos()
               print("\n")
               opcao=0
               
          elif(opcaoUpdate == 2):
               
               agenda.pesquisarTodosContatos()
               print("\n")
               condicao = input("Digite o seu ID: ")
               while(validar.formatarID(condicao)==False):
                     condicao = input("Digite o seu ID: ")
              
               novo = input("Digite o novo telefone do contato: ")
               while(validar.formatarTelefone(novo)==False):
                    novo = input("Digite o novo telefone do contato: ")
               print("\n")
               agenda.mudarTelContato(condicao,novo)
               print("\n")
               agenda.pesquisarTodosContatos()
               print("\n")
               opcao=0
               
          elif(opcaoUpdate == 3):
               
               agenda.pesquisarTodosContatos()
               print("\n")
               condicao = input("Digite o seu ID: ")
               while(validar.formatarID(condicao)==False):
                     condicao = input("Digite o seu ID: ")
              
               novo = input("Digite o novo email do contato: ")
               while(validar.formatarEmail(novo)==False):
                    novo = input("Digite o novo email do contato: ")
               print("\n")
               agenda.mudarEmailContato(condicao,novo)
               print("\n")
               agenda.pesquisarTodosContatos()
               print("\n")
               opcao=0
        
 
