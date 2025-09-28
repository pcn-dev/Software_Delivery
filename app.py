import os

restaurantes = [{'nome':'Hiatari', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Boa', 'categoria':'Italiana','ativo':True},
                {'nome':'Domdinho', 'categoria':'Hamburgueria', 'ativo': True}]


def exibir_nome_do_programa():
    '''Essa função serve para exibir o nome estilizado do programa na tela'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚██
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    '''Essa função serve para exibir as opções em que o usuário pode escolher'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''Essa função serve para exibir o subtítulo de "Finalizando o app"'''
    exibir_subtitulo('Finalizando o app')


def voltar_menu():
    '''Essa função serve para apertar qualquer tecla para voltar ao menu principal

    Inputs:
    - Qualquer tecla

    Outputs:
    -Retorna ao menu principal

    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    '''Essa função serve para mostrar ao usuario que a opção dele é inválida e voltar ao menu principal
    
    Outputs:
    -Retorna ao menu principal
    
    '''
    print('Opção inválida!\n')
    voltar_menu()


def exibir_subtitulo(texto):
    '''Essa função serve para exibir o subtítulo da opção que o usuário escolher
    
    Inputs:
    -texto: str - O texto do subtítulo
    
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    -Nome do restaurante
    -Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro dos novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante que deseja cadastrar {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()


def lista_restaurante():
    '''Essa função serve para listar todos os restaurantes já cadastrados
    
    Outputs:
    -Exibe a lista de restaurantes na tela
    
    '''
    exibir_subtitulo('Listagem dos restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    print()
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_menu()

def alternar_estado_restaurante():
    '''Essa função serve para alternar estado de restaurante, podendo estar Ativado ou Desativado
    
    Inputs:
    -Nome do restaurante para alterar o estado

    Outputs:
    -Exibe mensagem indincando o sucesso da operação
    
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_escontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_escontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_restaurante} foi ativo com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            print(mensagem)
    if not restaurante_escontrado:
        print('O restaurante não foi encontrado.')


    voltar_menu()

def escolher_opcao():
    '''Essa função serve para analisar a escolha que o usuário fez
    
    Inputs:
    -Opção para tal função

    Outputs:
    -Executar a tal opção escolhida pelo usuário
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():
    '''Essa função serve para exibir tudo do sistema'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()