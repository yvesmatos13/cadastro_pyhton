from curses.ascii import isdigit
from wsgiref.validate import validator
from cadastro import Cadastro
from validadores import Validador

def main():
    
    usuario = Cadastro.usuario()
    if usuario['codigo'] == 0:
        login_acesso = input("login: ")
        senha_acesso = input("senha: ")
        if login_acesso == usuario['login'] and senha_acesso == usuario['senha']:
            pessoa = Cadastro.pessoa()
            print(pessoa)
        else:
            print("Usuário ou senha invalido")
    elif usuario['codigo'] == 400:
        print(usuario)


main()

