import funcjson
import funclogin
import funcmovies

# Projeto de gerenciamneto de reviews de filmes.

usuario_ativo = 'nao'

# Funções do menu
def menu_login():

    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'o-----------------------Menu de login----------------------o\n'
                              f'o----------------------------------------------------------o\n'
                              f'Realizar login (Escreva 1)\n' #Feito
                              f'Criar uma conta (Escreva 2)\n'
                              f'Fechar (Escreva 3)\n'
                              f'o----------------------------------------------------------o\n' #Feito
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 3:
            rodando_menu = False
            if opcao_seguida == 1:  # Inserir um grupo de trabalho em uma lista (Escreva 3)
                usuario_ativo = funclogin.login()
                if usuario_ativo['admin']:
                    return menu_adm()
                else:
                    return menu_user()

            if opcao_seguida == 2:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                adm.create_account()
                return menu_login()

            if opcao_seguida == 3:  # Remover um grupo de trabalho em uma lista (Escreva 4)
                continue

            return opcao_seguida
        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 3\n')
def menu_user():
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'o----------------------Menu de Usuário---------------------o\n'
                              f'o----------------------------------------------------------o\n'
                              f'Buscar um filme (Escreva 1)\n'
                              f'Editar review para um filme (Escreva 2)\n'
                              f'Consultar overview (Escreva 3)\n'
                              f'Sair (Escreva 4)\n'
                              f'o----------------------------------------------------------o\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 5:
            rodando_menu = False

            if opcao_seguida == 1:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                funcmovies.imprimir_filme(funcmovies.consultando_filme(data))
                return menu_user()

            if opcao_seguida == 2:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                funcmovies.editando_filme(funcmovies.consultando_filme(data))
                return menu_user()

            if opcao_seguida == 3:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                funcmovies.imprimir_overview_filme(funcmovies.consultando_filme(data))
                return menu_user()

            if opcao_seguida == 4:  # Inserir um grupo de trabalho numa lista (Escreva 3)
                return menu_login()

        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 5\n')
def menu_adm():
    rodando_menu = True
    while rodando_menu:
        opcao_seguida = input(f'o----------------------------------------------------------o\n'
                              f'o-----------------------Menu de Admin----------------------o\n'
                              f'o----------------------------------------------------------o\n'
                              f'Buscar um usuário (Escreva 1)\n'
                              f'Deletar um usuário (Escreva 2)\n'
                              f'Adicionar um usuário (Escreva 3)\n'
                              f'Sair (Escreva 4)\n'
                              f'o----------------------------------------------------------o\n'
                              f'Selecione uma das opções acima digitando apenas o numero: ')

        try:
            opcao_seguida = int(opcao_seguida)
            it_is = True
        except ValueError:
            it_is = False

        if it_is and 1 <= opcao_seguida <= 4:
            rodando_menu = False
            if opcao_seguida == 1:
                funclogin.buscar_usuario()
                return menu_adm()

            if opcao_seguida == 2:
                adm.delete_user()
                return menu_adm()

            if opcao_seguida == 3:
                adm.create_account()
                return menu_adm()

            if opcao_seguida == 4:
                return menu_login()

        else:
            print(f'Espera-se uma opcao_seguida com valor inteiro entre 1 e 4\n')


# Classes
class usuario:
    def __init__(self, name, senha, id, movies_reviewed):
        self._name = name
        self._id = id
        self._movies_reviewed = movies_reviewed
        self._senha = senha
class adm(usuario):
    def print_funcionarios(data_users):
        print(data_users)

    @staticmethod
    def delete_user():
        usuarios_cadastrados = funcjson.lendo_users_json()
        passou_checagem = True
        print(f'Os usuários cadastrados são: \n')
        for lista_de_usuarios in usuarios_cadastrados:
            print(lista_de_usuarios['Name'])
        usuario = input(f'Digite o usuário que deseja deletar: ')

        for i in range(len(usuarios_cadastrados)):
            if usuario == usuarios_cadastrados[i]['Name']:
                del usuarios_cadastrados[i]
                funcjson.salvando_users_json(usuarios_cadastrados)
                print(f'usuário deletado')
                break

    @staticmethod
    def create_account():
        usuario = input(f'Digite seu usuário: ')
        usuarios_cadastrados = funcjson.lendo_users_json()
        passou_checagem = True
        for lista_de_usuarios in usuarios_cadastrados:
            if usuario == lista_de_usuarios['Name']:
                passou_checagem = False

        if passou_checagem:
            novo_usuario = {"Name": usuario,
                            "ID": (len(usuarios_cadastrados) + 1),
                            "movies_reviewed": [],
                            "admin": False}

            usuarios_cadastrados.append(novo_usuario)
            funcjson.salvando_users_json(usuarios_cadastrados)
        else:
            print(f'usuário já cadastrado')

if __name__ == '__main__':

    data = funcjson.lendo_filmes_json()
    menu_login()

