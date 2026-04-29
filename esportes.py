import json
import os
import main

def salvar_esporte(email, esporte_nome):
    """Salva o esporte selecionado do usuário no JSON"""
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario["email"] == email:
            usuario["esporte"] = esporte_nome
            break
    
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)

def ver_esportes_marcados(email_usuario):

    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario["email"] == email_usuario:
            esporte = usuario.get("esporte", "Nenhum esporte marcado")
            print(f"\n{'_'*50}")
            print(f"Esporte marcado: {esporte}")
            print(f"{'_'*50}\n")
            return
    
    print("Usuário não encontrado!")

def menu_usuario(email_usuario):
    while True:
        print( "_" * 50 )
        print("MENU\n")
        print( "_" * 50 )
        print("\n[1] Ver esportes marcados")
        print("[2] Marcar esporte")
        print("[0] Sair\n")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            ver_esportes_marcados(email_usuario)
        elif escolha == "2":
            print("\nMarcar esporte:") 
            selecionar_esporte(email_usuario)
        elif escolha == "0":
            print("Saindo do menu. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

ESPORTES_INDIVIDUAIS = {
    1: "Atletismo",
    2: "Atletismo Paralímpico",
    3: "Judô",
    4: "Judô Paralímpico",
    5: "Natação",
    6: "Natação Paralímpica",
    7: "Tênis de Mesa",
    8: "Tênis de Mesa em Cadeira de Rodas"
}     

ESPORTES_COLETIVOS = {
    1: "Basquete",
    2: "Basquete de Cadeira de Rodas",
    3: "Futebol",
    4: "Futebol de 5",
    5: "Futsal",
    6: "Handebol",
    7: "Vôlei",
    8: "Vôlei Sentado"
}

def selecionar_esporte(email_usuario):
    print("\nSELECIONE O ESPORTE")
    print("[1] Esportes Individuais")
    print("[2] Esportes Coletivos")
    tipo = input("Escolha: ")
    
    if tipo == "1":
        esportes = ESPORTES_INDIVIDUAIS
    elif tipo == "2":
        esportes = ESPORTES_COLETIVOS
    else:
        print("Opção inválida!")
        return
    
    print("\nOpções disponíveis:")
    for numero in esportes:
        print(f"[{numero}] {esportes[numero]}")
    
    esporte_escolhido = int(input("Escolha um esporte: "))
    
    if esporte_escolhido in esportes:
        nome_esporte = esportes[esporte_escolhido]
        print(f"Você escolheu: {nome_esporte}")
        
        # Salva o esporte no JSON
        salvar_esporte(email_usuario, nome_esporte)
        print("Esporte salvo com sucesso!")
    else:
        print("Opção inválida!")


    