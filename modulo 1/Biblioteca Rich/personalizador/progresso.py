from rich.progress import Progress
from time import sleep

def barra_progresso_simples(texto, isArquivo=False):
    """
    Exibe uma barra de progresso simples.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido na barra.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    
    with Progress() as progress:
        tarefa = progress.add_task(f"[cyan]{texto}", total=100)
        for i in range(100):
            sleep(0.05)
            progress.update(tarefa, advance=1)


def barra_progresso_texto(texto, isArquivo=False):
    """
    Exibe uma barra de progresso com uma mensagem de carregamento e o texto final.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido após o progresso.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    
    with Progress() as progress:
        tarefa = progress.add_task(f"[green]Carregando o texto...", total=100)
        for i in range(100):
            sleep(0.05)
            progress.update(tarefa, advance=1)
    
    print(f"texto: {texto}")
