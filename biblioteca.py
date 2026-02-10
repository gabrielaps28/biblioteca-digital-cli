import os

livros = [
    {'nome': '1984', 'genero': 'Distopia', 'disponivel': True},
    {'nome': 'Dom Casmurro', 'genero': 'Romance', 'disponivel': False},
    {'nome': 'O Hobbit', 'genero': 'Fantasia', 'disponivel': True}
]

def exibir_nome_do_programa():
    print("""
Bɪʙʟɪᴏᴛᴇᴄᴀ Dɪɢɪᴛᴀʟ
""")

def exibir_opcoes():
    print('1. Cadastrar livro')
    print('2. Listar livros')
    print('3. Emprestar / Devolver livro')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando aplicação')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_livro():
    exibir_subtitulo('Cadastro de novos livros')
    nome_do_livro = input('Digite o nome do livro: ')
    genero = input(f'Digite o gênero do livro "{nome_do_livro}": ')
    dados_do_livro = {'nome': nome_do_livro, 'genero': genero, 'disponivel': True}
    livros.append(dados_do_livro)
    print(f'O livro "{nome_do_livro}" foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_livros():
    exibir_subtitulo('Lista de livros')

    print(f'{"Livro".ljust(25)} | {"Gênero".ljust(20)} | Status')

    for livro in livros:
        nome = livro['nome']
        genero = livro['genero']
        status = 'Disponível' if livro['disponivel'] else 'Emprestado'
        print(f'- {nome.ljust(23)} | {genero.ljust(20)} | {status}')

    voltar_ao_menu_principal()

def alternar_estado_livro():
    exibir_subtitulo('Emprestar / Devolver livro')
    nome_livro = input('Digite o nome do livro: ')
    livro_encontrado = False

    for livro in livros:
        if nome_livro.strip().lower() == livro['nome'].strip().lower():
            livro_encontrado = True
            livro['disponivel'] = not livro['disponivel']
            mensagem = (
                f'O livro "{nome_livro}" está disponível.'
                if livro['disponivel']
                else f'O livro "{nome_livro}" foi emprestado.'
            )
            print(mensagem)

    if not livro_encontrado:
        print('Livro não encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_novo_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            alternar_estado_livro()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
