import argparse
import personalizador.layout as layout
import personalizador.painel as painel
import personalizador.progresso as progresso
import personalizador.estilo as estilo

def main():
    modulos = {
        "layout": layout,
        "painel": painel,
        "progresso": progresso,
        "estilo": estilo,
    }

    funcoes = {
        "layout": ["layoutEsquerdaDireita", "layoutCimaBaixo"],
        "painel": ["painelComTitulo", "painelSimples"],
        "progresso": ["barra_progresso_simples", "barra_progresso_texto"],
        "estilo": ["italicRed", "underlineCyan"],
    }

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-t',
        '--texto', 
        type=str, 
        required=True,
        help="Informe o texto ou caminho do arquivo." 
    )

    parser.add_argument(
        '-a',
        '--arquivo',
        action= 'store_true',
        help="Se tem arquivo" 
    )

    parser.add_argument(
        "-m", 
        "--modulo",
        required=True,
        choices= modulos.keys(),
        help=f"Módulo disponível: {', '.join(modulos.keys())}",
    )

    parser.add_argument(
        "-f",
        "--funcao",
        required=True,
        help="Função do módulo que deseja acessar. "
        "Use uma das seguintes opções (dependendo do módulo):\n"
        f"{', '.join(f'{m}: {f}' for m, f in funcoes.items())}",
    )


    args = parser.parse_args()

    modulo = modulos[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == '__main__':
    main()