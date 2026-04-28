import re
import json
import os

dados_usuarios = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(dados_usuarios) or os.path.getsize(dados_usuarios) == 0:
        return []
    with open(dados_usuarios, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(dados_usuarios, "w") as f:
        json.dump(usuarios, f, indent=4)

def criar_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if not nome:
            print("O nome não pode ser vazio. Tente novamente.\n")
            continue
        if not nome.replace(" ", "").isalpha():
            print("O nome só pode conter letras. Tente novamente.\n")
            continue
        if len(nome) < 3:
            print("O nome deve ter no mínimo 3 caracteres. Tente novamente.\n")
            continue
        if len(nome) > 100:
            print("O nome deve ter no máximo 100 caracteres. Tente novamente.\n")
            continue
        return nome

def criar_email():
    while True:
        email = input("Digite seu email: ").strip()
        if not email:
            print("O email não pode ser vazio. Tente novamente.\n")
            continue
        padrao_email = r'^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$'
        if not re.match(padrao_email, email):
            print("Email inválido. Tente novamente.\n")
            continue
        return email

def criar_senha():
    while True:
        senha = input("Digite sua senha: ")
        if not senha:
            print("A senha não pode ser vazia. Tente novamente.\n")
            continue
        if len(senha) < 6:
            print("A senha deve ter pelo menos 6 caracteres. Tente novamente.\n")
            continue
        return senha

def selecionar_modalidade():
    while True:
        print("Selecione sua modalidade:")
        print("[1] Masculino")
        print("[2] Feminino")
        print("[0] voltar\n")
        modalidade = input("Escolha uma opção: ")
        if modalidade == "1":
            return "Masculino"
        elif modalidade == "2":
            return "Feminino"
        elif modalidade == "0":
            return None
        else:
            print("Opção inválida. Tente novamente.\n")
    
def escolher_funcao():
    while True:
        print("Escolha sua função:")
        print("[1] Atleta")
        print("[2] Técnico")
        print("[0] voltar\n")
        funcao = input("Escolha uma opção: ")
        if funcao == "1":
            return "Atleta"
        elif funcao == "2":
            return "Técnico"
        elif funcao == "0":
            return None
        else:
            print("Opção inválida. Tente novamente.\n")


def fazer_cadastro():
    print( "_" * 50 )
    print("FAÇA SEU CADASTRO\n")
    print( "_" * 50 )

    nome = criar_nome()
    
    while True:
        email = criar_email()
        senha = criar_senha()
        modalidade = selecionar_modalidade()
        
        if modalidade is None:
            continue
        
        funcao = escolher_funcao()
        
        if funcao is None:
            continue
        
        usuarios = carregar_usuarios()
        usuarios.append({
            "nome": nome,
            "email": email,
            "senha": senha,
            "esporte": "",
            "modalidade": modalidade,
            "funcao": funcao
        })
        salvar_usuarios(usuarios)

        print("Cadastro realizado com sucesso!")
        break

