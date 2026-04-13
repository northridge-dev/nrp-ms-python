def printInstructions():
    print("""Use the WASD keys to move the tiles
    back into their original order:
           1   2   3   4
           5   6   7   8
           9   10  11  12
           13  14  15   """)


def displayBoard(board):
    """Display the given board on the screen."""
    labels = [
        board[0][0],
        board[0][1],
        board[0][2],
        board[0][3],
        board[1][0],
        board[1][1],
        board[1][2],
        board[1][3],
        board[2][0],
        board[2][1],
        board[2][2],
        board[2][3],
        board[3][0],
        board[3][1],
        board[3][2],
        board[3][3],
    ]
    boardToDraw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
""".format(*labels)
    print(boardToDraw)
