"""
"""

def check_rows(board: list)-> bool:
    """
    Check if in rows are the same numbers
    """
    for i in board:
        numbers = []
        for j in i:
            if (j != "*") and (j != ' '):
                numbers.append(int(j))
        for j in numbers:
            numbers = numbers[1:]
            if j in numbers:
                return False
    return True

def check_columns(board: list)-> bool:
    """
    Check if in colnmns are the same numbers
    """
    new_board = []
    for i in range(len(board)):
        new_board.append('')
    for i in board:
        for j in range(len(i)):
            new_board[j] = i[j] + new_board[j]
    return check_rows(new_board)

def check_colored_cells(board: list)-> bool:
    """
    Check if in colored cells are the same numbers
    """
    pass


def validate_board(board: list)-> bool:
    """
    Check if board is ready for game
    """
    pass
