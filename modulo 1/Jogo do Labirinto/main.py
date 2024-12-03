import argparse
from aventura_pkg.utils import menu, imprime_instrucoes
from aventura_pkg.labirinto import iniciar_listener

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", help="Nome do jogador", default="Jogador")
    args = parser.parse_args()

    while True:
        opcao = menu()
        match opcao:
            case "1":
                print(f"Iniciando o jogo para {args.name}...")
                iniciar_listener()
            case "2":
                imprime_instrucoes()
            case "3":
                print("Saindo do jogo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
