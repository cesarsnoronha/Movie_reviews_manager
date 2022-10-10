import funcjson

# Funções relacionadas ao login

def login():  # return usuario  #usuario_ativo = login()
    usuario = input(f'Digite seu usuário: ')
    senha = input(f'Digite sua senha: ') #decorativa
    usuarios_cadastrados = funcjson.lendo_users_json()
    for item_usuario in usuarios_cadastrados:
        if usuario == item_usuario['Name']:
            print(f'login realizado corretamente')

            return item_usuario
    print(f'Usuário não cadastrado')
def buscar_usuario():
    usuario = input(f'Digite o usuário para busca: ')
    usuarios_cadastrados = funcjson.lendo_users_json()
    for lista_de_usuarios in usuarios_cadastrados:
        if usuario == lista_de_usuarios['Name']:
            print(f'{lista_de_usuarios}')
        else:
            print(f'Usuário não cadastrado')
