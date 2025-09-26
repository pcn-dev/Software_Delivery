import os

tarefas = []  # lista de tarefas

def exibir_paulo_tarefas():
    os.system('cls')
    print('''
   
    𝙋𝙖𝙪𝙡𝙤 𝙏𝙖𝙧𝙚𝙛𝙖𝙨
   
    ''')
   
def exibir_opcoes():
    print('1. Adicionar tarefa')
    print('2. Ver minhas tarefas')
    print('3. Excluir tarefa')
    print('4. Sair do app')
   
def subtitulo_opcao(texto):
    os.system('cls')
    print(texto)
   
def voltar_menu():
    input('\nDigite qualquer tecla para voltar ao menu de opções ')
    main()
   
def adicionar_tarefa():
    subtitulo_opcao('\nAdicionar uma tarefa\n')
    nome_da_tarefa = input('Digite o nome da tarefa que gostaria de adicionar: ')
    data_da_tarefa = input(f'Digite a data da tarefa ({nome_da_tarefa}): ')
    hora_da_tarefa = input(f'Digite a hora da tarefa ({nome_da_tarefa}): ')
    
    tarefa = {'nome': nome_da_tarefa, 'data': data_da_tarefa, 'hora': hora_da_tarefa}
    tarefas.append(tarefa)  # adiciona no fim da lista
    
    print(f'A tarefa ({nome_da_tarefa}), do dia {data_da_tarefa}, ás {hora_da_tarefa} hrs, foi registrada com sucesso!')
    voltar_menu()

def ver_tarefas():
    subtitulo_opcao('\nLista de tarefas\n')
    print(f"{'Nome da tarefa'.ljust(22)} | {'Data da tarefa'.ljust(20)} | {'Hora da tarefa'.ljust(20)}")
    
    if not tarefas:  # se a lista estiver vazia
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(f"- {tarefa['nome'].ljust(20)} | {tarefa['data'].ljust(20)} | {tarefa['hora'].ljust(20)}")
    
    voltar_menu()
   
def excluir_tarefa():
    subtitulo_opcao('\nExcluir tarefa\n')
    if not tarefas:
        print("Nenhuma tarefa cadastrada para excluir.")
    else:
        nome_tarefa_excluida = input('Digite o nome da tarefa que gostaria de excluir: ').lower()
        encontrada = False
        
        for tarefa in tarefas:
            if tarefa['nome'].lower() == nome_tarefa_excluida:
                tarefas.remove(tarefa)
                print(f"A tarefa ({tarefa['nome']}) foi excluída com sucesso!")
                encontrada = True
                break
        
        if not encontrada:
            print("Tarefa não encontrada.")
    
    voltar_menu()
   
def sair_app():
    subtitulo_opcao('\nSaindo do app...\n')
   
def opcao_invalida():
    print("\nOpção inválida! Tente novamente.")
    voltar_menu()
   
def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nDigite a opção que você gostaria de selecionar: '))
       
        if opcao_escolhida == 1:
            adicionar_tarefa()
        elif opcao_escolhida == 2:
            ver_tarefas()
        elif opcao_escolhida == 3:
            excluir_tarefa()
        elif opcao_escolhida == 4:
            sair_app()
        else:
            opcao_invalida()
       
    except:
        opcao_invalida()

def main():
    exibir_paulo_tarefas()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
