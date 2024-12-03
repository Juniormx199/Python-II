from pynput import keyboard
from pyamaze import maze, agent , textLabel

labirinto = maze(5, 5)
labirinto.CreateMaze()
agente = agent(labirinto)
passos = 0
texto = textLabel(labirinto, title="Nº passos", value=passos)
mapa = labirinto.maze_map

listener = None



# Função para iniciar o listener
def iniciar_listener():
    global listener
    def on_press(key):
        try:
            if key.char in ['w', 'a', 's', 'd']:
                verificaPosicao(key.char)
        except AttributeError:
            pass


    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    labirinto.run()
    print("Listener iniciado.")

def parar_listener():
    global listener
    if listener:
        listener.stop()
        print("Listener parado.")


def verificaPosicao(key):
    posicaoAtual = agente.position
    caminhosAtual = mapa[agente.position]

    match key:
        case 'w':  # Norte
            if caminhosAtual['N'] == 1:
                novaPosicao = (posicaoAtual[0] - 1, posicaoAtual[1])
                mudarPosicao(novaPosicao)
        case 's':  # Sul
            if caminhosAtual['S'] == 1:
                novaPosicao = (posicaoAtual[0] + 1, posicaoAtual[1])
                mudarPosicao(novaPosicao)
        case 'a':  # Oeste
            if caminhosAtual['W'] == 1:
                novaPosicao = (posicaoAtual[0], posicaoAtual[1] - 1)
                mudarPosicao(novaPosicao)
        case 'd':  # Leste
            if caminhosAtual['E'] == 1:
                novaPosicao = (posicaoAtual[0], posicaoAtual[1] + 1)
                mudarPosicao(novaPosicao)

def mudarPosicao(posicao):
    global passos 
    passos += 1
    texto.value = passos  
    agente.position = posicao
    if posicao == (1,1):
        parar_listener()
        return print('Você ganhou')
    