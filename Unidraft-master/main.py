import cadastro
import login 
import esportes

def main():
    while True:
        print("_" * 50 )
        print("\nBem-vindo ao Unidraft!")
        print("_" * 50 )
        print("\n[1] Fazer cadastro")
        print("[2] Fazer login")
        print("[0] Sair\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastro.fazer_cadastro()
        elif escolha == "2":
            logado = login.fazer_login()
            if logado:
                esportes.menu_usuario(login.email_logado)
        elif escolha == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()