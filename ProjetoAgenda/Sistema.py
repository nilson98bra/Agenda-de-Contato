import sys
import time
import os
from Agenda.Agenda import Agenda
from Banco.BancoDados import BancoDados
from View.ViewDeletar import ViewDeletar
from View.ViewPesquisar import ViewPesquisar
from View.ViewUpdate import ViewUpdate
from View.ViewInserir import ViewInserir

Sair=0
banco = BancoDados()
agenda = Agenda(banco)
print("------------------------------------Agenda------------------------------------\n")
while(Sair==0):
    opcao = input("Escolha uma das opçoes: \n\n1: Inserir Contato\n2: Pesquisar Contato\n3: Mudar Contato\n4: Deletar Contato\n5: Sair\n\n")
    while(opcao.isdigit()==False):
        print("Digite apenas numeros...\n")
        opcao = input("Escolha uma das opçoes: \n\n1: Inserir Contato\n2: Pesquisar Contato\n3: Mudar Contato\n4: Deletar Contato\n5: Sair\n\n")
    opcao = int(opcao)
    while(opcao >= 1):
        
        if(opcao == 1):
            inserir = ViewInserir(agenda)
            opcao=0
             
        elif(opcao == 2):
            pesquisar = ViewPesquisar(agenda)
            opcao=0
                
        elif(opcao == 3):
             update = ViewUpdate(agenda)
             opcao=0
            
            
        elif(opcao == 4):
             deletar = ViewDeletar(agenda)
             opcao=0
             
        elif(opcao == 5):
            print("Muito Obrigado!")
            opcao=0
            sys.exit(0)
             
        elif(opcao > 5):
            
            print("Digite somenete as opcoes mostradas")
            opcao=0
                      
