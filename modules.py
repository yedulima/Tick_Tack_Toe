def showBoard(board: list) -> None:
    for line in range(3):
        for column in range(3):
            if column != 2:
                print(''.join(board[line][column]), end=' | ')
                continue
            print(''.join(board[line][column]))
        print('-'*10)

def returnNumberOfNumBoard(num: int) -> tuple:
    num_board = [
        [[7], [8], [9]],
        [[4], [5], [6]],
        [[1], [2], [3]]
    ]

    for line in range(3):
        for column in range(3):
            print(num_board[line][column][0], num_board[line][column][0] == num)
            if num_board[line][column][0] == num:
                return line, column
    
    return False, False # Not found

def markInBoard(board: list, num: int, player: str) -> tuple:
    line, column = returnNumberOfNumBoard(num)

    print(line, column)

    if line == False:
        print("Escolha inválida!")
        return False, 'unknow'
    
    board[line][column] = player

    return True, board

def checkWinner(board):
    pass