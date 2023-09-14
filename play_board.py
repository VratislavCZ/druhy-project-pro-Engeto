# soubor board.py

separator = "+---+---+---+"

# Helpful game board
def helping_board():
    for i in range(3):
        print(separator)
        for j in range(3):
            print(f"| {i * 3 + j + 1} ", end="")
        print("|")
    print(separator)

# Game board during the game
def printing_board(board):
    print(separator)
    for i in range(3):
        print("| {} | {} | {} |".format(*board[i*3:i*3+3]))
        print(separator)
