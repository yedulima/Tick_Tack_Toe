'''

░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ██╗░░░██╗███████╗██╗░░░░░██╗░░██╗░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░██║██╔════╝██║░░░░░██║░░██║██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║  ╚██╗░██╔╝█████╗░░██║░░░░░███████║███████║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║  ░╚████╔╝░██╔══╝░░██║░░░░░██╔══██║██╔══██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ░░╚██╔╝░░███████╗███████╗██║░░██║██║░░██║
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
                                   by Carlos Eduardo
'''

from modules import *
import random
import os

if __name__ == '__main__':
    empty = ' '
    board = [
        [empty, empty, empty],
        [empty, empty, empty],
        [empty, empty, empty]
    ]

    labels = 9

    players = ['x', 'o']
    player = random.choice(players)

    os.system('clear')

    while labels:
        showBoard(board)
        while True:
            try:
                op = int(input("Número de 1 a 9: "))
            except:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                input()
            else:
                break

        verify, new_board = markInBoard(board, op, player)

        if verify:
            labels -= 1
            board = new_board
            win_check = checkWinner(board, player)

            if win_check:
                showBoard(board)
                break

            player = swapPlayer(player, players)

        os.system('clear')

    print("Game over")