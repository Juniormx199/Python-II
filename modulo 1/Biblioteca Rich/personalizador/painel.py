from rich import print
from rich.panel import Panel

def painelSimples(texto, isArquivo=False):
    """
    Exibe o texto em um painel simples com a cor vermelha.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    
    print(Panel('[red]'+texto))


def painelComTitulo(texto, isArquivo=False):
    """
    Exibe o texto em um painel com título "Texto" e cor verde.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()

    print(Panel('[green]'+texto, title="Texto"))
