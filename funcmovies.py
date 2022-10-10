# Funções relacionadas aos filmes
def consultando_filme(data):  # return opcao_seguida
    rodando_menu = True
    while rodando_menu:
        tamanho = len(data)
        opcao_seguida = input(f"Temos {tamanho} filmes disponíveis, escreva um número de 0 a {tamanho} "
                              f"para escolher o filme: ")
        try:
            opcao_seguida = int(opcao_seguida) - 1
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= tamanho:
            rodando_menu = False
            return opcao_seguida, data
        else:
            print(f'Espera-se uma opção seguida com valor inteiro entre 1 e {tamanho}\n')
def imprimir_filme(opcao_seguida,data):
    titulo = data[opcao_seguida]['Series_Title']
    ano = data[opcao_seguida]['Released_Year']
    nota = data[opcao_seguida]['Metrics']['IMDB_Rating']
    director = data[opcao_seguida]['Director']
    genero = data[opcao_seguida]['Genre']
    votos = data[opcao_seguida]['Metrics']["No_of_Votes"]

    print(f'O filme escolhido é o filme {titulo}, esse é um filme de {ano}, produzido por {director}.\n'
          f'Seus generos são {genero} e sua nota no IMDB é {nota} com {votos} votos')
def imprimir_overview_filme(opcao_seguida,data):
    titulo = data[opcao_seguida]['Series_Title']
    overview = data[opcao_seguida]['Overview']

    print(f'Exibindo o overview para o filme {titulo}:\n'
          f'{overview}')
def editando_filme(filme_seguido,data):
    print('A opção edição de filme foi escolhida')
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'titulo (Escreva 1)\n'
                              f'Ano (Escreva 2)\n'
                              f'Nota (Escreva 3)\n'
                              f'Diretor (Escreva 4)\n'
                              f'Genero (Escreva 5)\n'
                              f'Número de votos (Escreva 6)\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 6:
            rodando_menu = False
            if opcao_seguida == 1:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                data[filme_seguido]['Series_Title'] = input(f'Digite o novo Título')

            if opcao_seguida == 2:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                data[filme_seguido]['Released_Year'] = input(f'Digite o novo Ano')

            if opcao_seguida == 3:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                data[filme_seguido]['Metrics']['IMDB_Rating'] = input(f'Digite a nova nota')

            if opcao_seguida == 4:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                data[filme_seguido]['Director'] = input(f'Digite o novo Diretor')

            if opcao_seguida == 5:  # Salvar de uma lista para um JSON os grupos de trabalho (Escreva 5)
                data[filme_seguido]['Genre'] = input(f'Digite o novo gênero')

            if opcao_seguida == 6:  # Fechar o program (Escreva 6)
                data[filme_seguido]['Metrics']["No_of_Votes"] = input(f'Digite o novo número de votos')

            imprimir_filme(filme_seguido)
            return filme_seguido
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 6\n')
def add_review(filme_seguido,data):
    nota = data[filme_seguido]['Metrics']['IMDB_Rating']
    n_votos = data[filme_seguido]['Metrics']["No_of_Votes"]
    titulo = data[filme_seguido]['Series_Title']

    rodando_menu = True
    while rodando_menu:
        nova_nota = input(f'Qual nota você deseja adicionar ao filme {titulo}: ')

        try:
            nova_nota = int(nova_nota)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 0 <= nova_nota <= 10:
            rodando_menu = False
            data[filme_seguido]['Metrics']['IMDB_Rating'] = (nota*n_votos/(n_votos+1) + nova_nota/(n_votos+1))
            data[filme_seguido]['Metrics']["No_of_Votes"] = n_votos + 1

            return data
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 0 e 10\n')