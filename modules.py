import random
import os

class tickTack:
    empty = ' '

    def __init__(self, players):
        self.board = [
            [tickTack.empty, tickTack.empty, tickTack.empty],
            [tickTack.empty, tickTack.empty, tickTack.empty],
            [tickTack.empty, tickTack.empty, tickTack.empty]
        ]
        self.players = players
        self.player = players[0]
    
    def runGame(self) -> None:
        os.system('clear')

        labels = 9

        while labels:
            tickTack.showBoard(self)
            while True:
                try:
                    op = int(input("Número de 1 a 9: "))
                except:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    input()
                else:
                    break

            verify, new_board = tickTack.markInBoard(self, self.board, op, self.player)

            if verify:
                labels -= 1
                self.board = new_board
                win_check = tickTack.checkWinner(self, self.board, self.player)

                if win_check:
                    tickTack.showBoard(self)
                    print("AAA")
                    input()
                    break

                self.player = tickTack.swapPlayer(self, self.player, self.players)

            os.system('clear')

    def showBoard(self) -> None:
        for line in range(3):
            for column in range(3):
                if column != 2:
                    print(self.board[line][column], end=' | ')
                    continue
                print(''.join(self.board[line][column]))
            print('-'*10)

    def swapPlayer(self, current_player: str, players: list) -> str:
        player_index = players.index(current_player)

        if players[player_index] == players[-1]:
            return players[0]
        return players[-1]

    def returnNumberOfNumBoard(self, num: int) -> tuple:
        num_board = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]

        for line in range(3):
            for column in range(3):
                if num_board[line][column] == num:
                    return line, column
        
        return 404, False # Not found

    def markInBoard(self, board: list, num: int, player: str) -> tuple:
        line, column = tickTack.returnNumberOfNumBoard(self, num)

        if line == 404 or board[line][column] != ' ':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            input()
            return False, '_'

        board[line][column] = player

        return True, board

    def checkWinner(self, board: list, player: str) -> bool:
        # Diagonal direita
        if (board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player):
            return True

        # Diagonar esquerda
        elif (board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player):
            return True

        # Horizontal
        for line in range(3):
            if (board[line][0] == player) and (board[line][1] == player) and (board[line][2] == player):
                return True

        # Vertical
        for column in range(3):
            if (board[0][column] == player) and (board[1][column] == player) and (board[2][column] == player):
                return True

        return False