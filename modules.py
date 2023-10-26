def showBoard(board: list) -> None:
    for line in range(3):
        for column in range(3):
            if column != 2:
                print(board[line][column], end=' | ')
                continue
            print(''.join(board[line][column]))
        print('-'*10)

def swapPlayer(current_player: str, players: list) -> str:
    player_index = players.index(current_player)

    if players[player_index] == players[-1]:
        return players[0]
    return players[-1]

def returnNumberOfNumBoard(num: int) -> tuple:
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

def markInBoard(board: list, num: int, player: str) -> tuple:
    line, column = returnNumberOfNumBoard(num)

    if line == 404 or board[line][column] != ' ':
        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        input()
        return False, '_'

    board[line][column] = player

    return True, board

def checkWinner(board: list, player: str) -> bool:
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