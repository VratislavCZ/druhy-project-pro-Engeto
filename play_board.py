# soubor board.py

# Helpful game board
def helping_board():
    for i in range(3):
        print("+---+---+---+")
        for j in range(3):
            print(f"| {i * 3 + j + 1} ", end="")
        print("|")
    print("+---+---+---+")

# Game board during the game
def printing_board(board):
    print("+---+---+---+")
    for i in range(3):
        print("| {} | {} | {} |".format(*board[i*3:i*3+3]))
        print("+---+---+---+")