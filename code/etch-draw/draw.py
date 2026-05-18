import CHARS

CANVAS_WIDTH = 75
CANVAS_HEIGHT = 20

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """Returns a multiline string of the line drawn in canvasData."""
    canvasStr = ''

    """canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # Add the line character for this point to canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += CHARS.UP_DOWN
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += CHARS.LEFT_RIGHT
            elif cell == set(['S', 'D']):
                canvasStr += CHARS.DOWN_RIGHT
            elif cell == set(['A', 'S']):
                canvasStr += CHARS.DOWN_LEFT
            elif cell == set(['W', 'D']):
                canvasStr += CHARS.UP_RIGHT
            elif cell == set(['W', 'A']):
                canvasStr += CHARS.UP_LEFT
            elif cell == set(['W', 'S', 'D']):
                canvasStr += CHARS.UP_DOWN_RIGHT
            elif cell == set(['W', 'S', 'A']):
                canvasStr += CHARS.UP_DOWN_LEFT
            elif cell == set(['A', 'S', 'D']):
                canvasStr += CHARS.DOWN_LEFT_RIGHT
            elif cell == set(['W', 'A', 'D']):
                canvasStr += CHARS.UP_LEFT_RIGHT
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CHARS.CROSS
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'  # Add a newline at the end of each row.
    return canvasStr


def make_move(command):
    """Process a single WASD move command."""
    global canvas, cursorX, cursorY

    if canvas == {}:
        if command in ('W', 'S'):
            canvas[(cursorX, cursorY)] = set(['W', 'S'])
        elif command in ('A', 'D'):
            canvas[(cursorX, cursorY)] = set(['A', 'D'])

    if command == 'W' and cursorY > 0:
        canvas[(cursorX, cursorY)].add(command)
        cursorY = cursorY - 1
    elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
        canvas[(cursorX, cursorY)].add(command)
        cursorY = cursorY + 1
    elif command == 'A' and cursorX > 0:
        canvas[(cursorX, cursorY)].add(command)
        cursorX = cursorX - 1
    elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
        canvas[(cursorX, cursorY)].add(command)
        cursorX = cursorX + 1
    else:
        return

    if (cursorX, cursorY) not in canvas:
        canvas[(cursorX, cursorY)] = set()

    if command == 'W':
        canvas[(cursorX, cursorY)].add('S')
    elif command == 'S':
        canvas[(cursorX, cursorY)].add('W')
    elif command == 'A':
        canvas[(cursorX, cursorY)].add('D')
    elif command == 'D':
        canvas[(cursorX, cursorY)].add('A')


def load(filename):
    """Load a saved drawing from file by replaying the moves string."""
    global canvas, cursorX, cursorY, moves

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            moves_str = f.readline().strip()
    except:
        return

    if not moves_str:
        return

    canvas = {}
    cursorX = 0
    cursorY = 0

    for char in moves_str:
        if char == 'C':
            canvas = {}
            continue
        if char in ('W', 'A', 'S', 'D'):
            make_move(char)

    moves = list(moves_str)


moves = []
load('pic.txt')
while True:  # Main program loop.
    # Draw the lines based on the data in canvas:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD keys to move, C to clear, '
        + 'F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        break
    elif response == 'C':
        canvas = {}  # Erase the canvas data.
        moves.append('C')  # Record this move.
    elif response == 'F':
        # Save the canvas string to a text file:
        try:
            filename = 'pic.txt' 

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)
        make_move(command)
