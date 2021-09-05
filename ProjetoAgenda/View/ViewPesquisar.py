from Validacao.Validacao import Validacao
class ViewPesquisar:
     def __init__(self,agenda):
          self.agenda = agenda
          validar = Validacao()
          opcaoPesquisa = input("Escolha uma das opçoes: \n\n1: Pesquisar por nome: \n2: Pesquisar por telefone: \n3: Pesquisar por email: \n4: Pesquisar Todos: \n")
          while(opcaoPesquisa.isdigit()==False):
               print("Digite apenas numeros...")
               opcaoPesquisa = input("\nEscolha uma das opçoes: \n\n1: Pesquisar por nome: \n2: Pesquisar por telefone: \n3: Pesquisar por email: \n4: Pesquisar Todos: \n")
          opcaoPesquisa = int(opcaoPesquisa)
          if(opcaoPesquisa==1):
               print("\n")
               pesquisa = input("Digite o nome: ")
               print("\n")
               agenda.pesquisarContatoNome(pesquisa)
               print("\n")
               opcao = 0
               
          elif(opcaoPesquisa==2):
               print("\n")
               pesquisa = input("Digite o telefone: ")
               print("\n")
               agenda.pesquisarContatoTel(pesquisa)
               opcao = 0
          elif(opcaoPesquisa==3):
               print("\n")
               pesquisa = input("Digite o email: ")
               print("\n")
               agenda.pesquisarContatoEmail(pesquisa)
               print("\n")
               opcao = 0
          elif(opcaoPesquisa==4):
               print("\n")
               agenda.pesquisarTodosContatos()
               print("\n")
               opcao = 0
               
