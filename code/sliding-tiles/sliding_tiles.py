import random

from sliding_tiles_utils import displayBoard, printInstructions

BLANK = "  "  # Note: This string is two spaces, not one.


def main():
    move = 1
    printInstructions()
    input("Press Enter to begin...")

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard, move)
        if playerMove == "QUIT":
            print("Thanks for playing!")
            break
        makeMove(gameBoard, playerMove)
        move += 1

        if gameBoard == getNewBoard():
            print(f"You won in {move} moves!")
            break


def getNewBoard():
    """Return a list of lists that represents a new tile puzzle."""
    return [
        ["1 ", "2 ", "3 ", "4 "],
        ["5 ", "6 ", "7 ", "8 "],
        ["9 ", "10", "11", "12"],
        ["13", "14", "15", BLANK],
    ]


def findBlankSpace(board):
    """Return a (row, col) tuple of the blank space's location."""
    for row in range(4):
        for col in range(4):
            if board[row][col] == BLANK:
                return (row, col)


def askForPlayerMove(board, num_moves):
    """Let the player select a tile to slide."""
    blank_row, blank_col = findBlankSpace(board)

    w = "W" if blank_row != 3 else " "
    a = "A" if blank_col != 3 else " "
    s = "S" if blank_row != 0 else " "
    d = "D" if blank_col != 0 else " "

    while True:
        print("Move {}".format(num_moves))
        print("                          ({})".format(w))
        print("Enter WASD (or QUIT): ({}) ({}) ({})".format(a, s, d))

        response = input("> ").upper()
        if response == "QUIT":
            return response
        if response in (w + a + s + d).replace(" ", ""):
            return response


def makeMove(board, move):
    """Carry out the given move on the given board."""
    row, col = findBlankSpace(board)

    if move == "W":
        board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
    elif move == "S":
        board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
    elif move == "A":
        board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
    elif move == "D":
        board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]


def makeRandomMove(board, lastMove=None):
    """Perform a slide in a random direction."""
    row, col = findBlankSpace(board)
    validMoves = []
    if row != 3 and lastMove != "S":
        validMoves.append("W")
    if col != 3 and lastMove != "D":
        validMoves.append("A")
    if row != 0 and lastMove != "W":
        validMoves.append("S")
    if col != 0 and lastMove != "A":
        validMoves.append("D")

    move = random.choice(validMoves)
    makeMove(board, move)

    return move


def getNewPuzzle(moves=100):
    """Get a new puzzle by making random slides from a solved state."""
    board = getNewBoard()

    lastMove = None
    for i in range(moves):
        lastMove = makeRandomMove(board, lastMove)
    return board


main()
