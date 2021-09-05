from Validacao.Validacao import Validacao
class ViewDeletar:
     def __init__(self,agenda):
          self.agenda = agenda
          validar = Validacao()
          agenda.pesquisarTodosContatos()
          print("\n")
          idContato =input("Insira o id: ")
          while(validar.formatarID(idContato)==False):
               idContato = input("Digite o seu ID: ")
          agenda.deletarContato(idContato)
          agenda.pesquisarTodosContatos()
          print("\n")
          
               
               
     
