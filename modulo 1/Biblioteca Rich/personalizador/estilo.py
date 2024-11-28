from rich.console import Console
from rich.style import Style

def underlineCyan(texto, isArquivo=False):
    """
    Exibe o texto em ciano e sublinhado.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.

    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    console = Console()
    console.print(texto, style=Style.parse("cyan") + Style(underline=True))


def italicRed(texto, isArquivo=False):
    """
    Exibe o texto em vermelho e itálico.

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.

    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    console = Console()
    console.print(texto, style=Style.parse("red") + Style(italic=True))
