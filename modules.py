import os
import json

def menu() -> int:

    while True:
        os.system('clear')
        print('''
    ▀█▀ █ █▀▀ █▄▀   ▀█▀ ▄▀█ █▀▀ █▄▀   ▀█▀ █▀█ █▀▀
    ░█░ █ █▄▄ █░█   ░█░ █▀█ █▄▄ █░█   ░█░ █▄█ ██▄
        ''')
        for _ in ["[1] - Jogar", "[2] - Créditos", "[3] - Placar", "[0] - Sair"]:
            print(f"    {_}")
        try:
            choice = int(input("\n    Opção: ").strip())
        except:
            os.system('clear')
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            input()
        else:
            break

    return choice

def credits() -> None:
    os.system('clear')
    print('''
    █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀
    █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█
 
 Carlos Eduardo & Anderson Lucas
    ''')
    input()

def scoreBoard() -> None:
    os.system('clear')

    score = json.load(open('./score.json', 'r'))

    print(''' 
    █▀ █▀▀ █▀█ █▀█ █▀▀ █▄▄ █▀█ ▄▀█ █▀█ █▀▄
    ▄█ █▄▄ █▄█ █▀▄ ██▄ █▄█ █▄█ █▀█ █▀▄ █▄▀
    ''')

    print(' '*10, f'{"PLAYER": ^10}|{"WINS": ^10}')
    for player, points in score.items():
        print(' '*10, '-'*21)
        print(' '*10, f'{player: ^10}|{points: ^10}')

    input()

class tickTack:
    empty = ' '

    def __init__(self):
        self.board = [
            [tickTack.empty, tickTack.empty, tickTack.empty],
            [tickTack.empty, tickTack.empty, tickTack.empty],
            [tickTack.empty, tickTack.empty, tickTack.empty]
        ]
        self.players = ['X', 'O']
        self.player = self.players[0]
        self.score = json.load(open('./score.json', 'r'))
    
    def runGame(self) -> None:
        labels = 9

        while labels:
            os.system('clear')
            while True:
                try:
                    os.system('clear')
                    tickTack.showBoard(self)
                    op = int(input(f"Vez do {self.player}\nNúmero de 1 a 9: "))
                except:
                    os.system('clear')
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
                    os.system('clear')
                    self.score[self.player] += 1
                    json.dump(self.score, open('./score.json', 'w'))
                    if self.player == 'X':
                        print('''
    ░░█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█ █▀█   ▀▄▀   █▀▀ ▄▀█ █▄░█ █░█ █▀█ █░█
    █▄█ █▄█ █▄█ █▀█ █▄▀ █▄█ █▀▄   █░█   █▄█ █▀█ █░▀█ █▀█ █▄█ █▄█
                    ''')
                        input()
                        return
                    
                    print('''
    ░░█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█ █▀█   █▀█   █▀▀ ▄▀█ █▄░█ █░█ █▀█ █░█
    █▄█ █▄█ █▄█ █▀█ █▄▀ █▄█ █▀▄   █▄█   █▄█ █▀█ █░▀█ █▀█ █▄█ █▄█
                    ''')
                    input()
                    return

                self.player = tickTack.swapPlayer(self, self.player, self.players)
        os.system('clear')
        print('''

    █▀▀ █▀▄▀█ █▀█ ▄▀█ ▀█▀ █▀▀
    ██▄ █░▀░█ █▀▀ █▀█ ░█░ ██▄
        ''')
        input()
        

    def showBoard(self) -> None:
        tickTack.showScore(self)
        for line in range(3):
            for column in range(3):
                if column != 2:
                    print(f'{self.board[line][column]: ^5}', end=' | ')
                    continue
                print(f'{self.board[line][column]: ^5}')
            print('-'*20)

    def showScore(self) -> None:
        x = self.score['X']
        o = self.score['O']
        print(f'{"="*5}{"Score": ^10}{"="*5}\n{f"X: {x}  O: {o}": ^20}')

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