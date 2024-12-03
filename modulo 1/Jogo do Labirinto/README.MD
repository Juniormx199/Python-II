# Aventura no Labirinto

Este é um jogo simples de aventura no labirinto, onde o jogador deve se movimentar pelo labirinto usando as teclas de direção.

## Como Jogar

- Use as teclas 'w', 'a', 's', 'd' para mover o jogador.
- O objetivo é chegar à saída do labirinto.

## Como Executar

1. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o jogo:
   ```bash
   python main.py --name "Jogador"
   ```

## Dependências

- rich
- pynput
