from rich import print
from rich.layout import Layout

def layoutCimaBaixo(texto, isArquivo=False):
    """
    Exibe o texto em um layout de cima para baixo, com a parte superior mostrando "Texto:".

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()
    
    layout = Layout()
    layout.split_column(
        Layout(name="cima", size=1),
        Layout(name="baixo")
    )
    layout["cima"].update('Texto:')
    layout["baixo"].update(texto)
    print(layout)


def layoutEsquerdaDireita(texto, isArquivo=False):
    """
    Exibe o texto em um layout de esquerda para direita, com a parte esquerda mostrando "Texto:".

    Parâmetros:
    texto (str): Texto ou caminho para o arquivo a ser exibido.
    isArquivo (bool): Se True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        with open(texto, "r") as arquivo:
            texto = arquivo.read()

    layout = Layout()
    layout.split_row(
        Layout(name="esquerda", size=7),
        Layout(name="direita")
    )
    layout["esquerda"].update('Texto:')
    layout["direita"].update(texto)
    print(layout)
