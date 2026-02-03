import os

def exibir_nome_do_programa(): 
    print("""
𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')  # limpa a tela no Windows
    # os.system('clear')  # descomente se estiver no Linux/Mac
    print('Finalizando o app')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')  # Corrigido: 'imput' → 'input'
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2: 
            print('Listar restaurantes')
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()  # Corrigido: estava 'finalizar_invalidade()' → 'opcao_invalida()'
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()