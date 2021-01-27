# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
tabuleiro = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
#import
import os

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letrasCorretas = []
        self.letrasErradas = []

    # Método para adivinhar a letra
    def verificaLetra(self, letra):
        if letra in self.palavra and letra not in self.letrasCorretas:
            self.letrasCorretas.append(letra)
        elif letra not in self.palavra and letra not in self.letrasErradas:
            self.letrasErradas.append(letra)
        else:
           return False
        return True

    # Método para verificar se o jogo terminou
    def gameOver(self):
        return self.gameWin() or len(self.letrasErradas) == 6


    # Método para verificar se o jogador venceu
    def gameWin(self):
        if '_' not in self.palavraSecreta():
            return True
        return False

    # Método para não mostrar a letra no board
    def palavraSecreta(self):
        rte = ''
        for letra in self.palavra:
            if letra not in self.letrasCorretas:
                rte += '_'

            else:
                rte += letra
        return rte

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        print(tabuleiro[len(self.letrasErradas)])
        print('\nPalavra: ', self.palavraSecreta())
        print('\nLetras Erradas: ',)
        for letra in self.letrasErradas:
            print(letra,)
            print()
        print('\nLetras Corretas: ',)
        for letra in self.letrasCorretas:
            print(letra,)
            print()


    # Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("Palavras.txt", "r") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()



# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.gameOver():
        game.status()
        palpite = input('digite o seu palpite: ')
        game.verificaLetra(palpite)


    # Verifica o status do jogo
    game.status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.gameWin():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
