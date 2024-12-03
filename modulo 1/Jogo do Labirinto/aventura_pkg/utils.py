from rich.console import Console

console = Console()

def imprime_instrucoes():
    """
    Imprime as instruções do jogo de forma formatada usando a biblioteca rich.
    """
    console.print("[bold blue]Instruções do Jogo[/bold blue]")
    console.print("Use as teclas 'w', 'a', 's', 'd' para mover o jogador pelo labirinto.")
    console.print("Objetivo: Chegar à saída do labirinto!")
    console.print("[green]Boa sorte, aventureiro(a)![green]")

def menu():
    """
    Exibe o menu principal do jogo.
    """
    console.print("[bold]Bem-vindo à Aventura no Labirinto![/bold]")
    console.print("1. [bold]Iniciar Jogo[/bold]")
    console.print("2. [bold]Instruções[/bold]")
    console.print("3. [bold]Sair[/bold]")
    escolha = input("Escolha uma opção: ")
    return escolha
