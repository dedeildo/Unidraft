import json
import os
import re

def carregar_usuarios():
    if not os.path.exists("usuarios.json") or os.path.getsize("usuarios.json") == 0:
        return []
    with open("usuarios.json", "r") as f:
        return json.load(f)

def pedir_email():
    while True:
        email = input("\nDigite seu email: ").strip()

        if not email:
            print("O email não pode ser vazio. Tente novamente.")
            continue

        padrao = r'^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$'
        if not re.match(padrao, email):
            print("Email inválido. Tente novamente.")
            continue

        usuarios = carregar_usuarios()
        emails_cadastrados = [u["email"] for u in usuarios]

        return email
    
def pedir_senha():
    while True:
        senha = input("Digite sua senha: ")

        if not senha:
            print("A senha não pode ser vazia. Tente novamente.")
            continue

        if len(senha) < 6:
            print("A senha deve ter pelo menos 6 caracteres. Tente novamente.")
            continue

        usuarios = carregar_usuarios()
        senhas_cadastradas = [u["senha"] for u in usuarios]

        return senha

def fazer_login():
    print("_" * 50)
    print("\nFAÇA SEU LOGIN\n")
    print("_" * 50)

    while True:
        email = pedir_email()
        senha = pedir_senha()

        usuarios = carregar_usuarios()

        for usuario in usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                print("\nLogin realizado com sucesso! Bem-vindo ao Unidraft!")
                
                # Importa esportes e chama o menu com o email do usuário
                import esportes
                esportes.menu_usuario(email)
                
                return True

        print("\nEmail ou senha incorretos. Tente novamente.")

