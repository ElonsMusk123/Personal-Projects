board = [0 for i in range(9)]
k = 1
for i in range(len(board)):
    board[i] = k
    k+=1


def playGame():
    go = True
    print("Welcome to my TicTacToe game! The game will now start...")

    player = "X"
    spotsFilled = 0
    while(go):
        printBoard(board)
        invalid = True
        while(invalid):
            try:
                choice = int(input("Which spot does Player " + player + " choose?"))
            except ValueError:
                print("Your answer must be an integer.")
            else:
                if (choice < 1 or choice > 9):
                    print("Your choice must be between 1 and 9.")
                elif (board[choice-1] == "X" or board[choice-1] == "O"):
                    print("That spot is already taken.")
                else:
                    board[choice-1] = player
                    spotsFilled += 1
                    invalid = False

        if (player == "X"):
            player = "O"
        else:
            player = "X"

        #TEST FOR ALL POSSIBLE WIN CONDITIONS
        if (board[0] == board[1] and board[0] == board[2]):
            printBoard(board)
            go = False
            if (board[0] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[2] == board[5] and board[2] == board[8]):
            printBoard(board)
            go = False
            if (board[2] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[6] == board[7] and board[6] == board[8]):
            printBoard(board)
            go = False
            if (board[6] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[0] == board[3] and board[0] == board[6]):
            printBoard(board)
            go = False
            if (board[0] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[1] == board[4] and board[1] == board[7]):
            printBoard(board)
            go = False
            if (board[1] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[3] == board[4] and board[3] == board[5]):
            printBoard(board)
            go = False
            if (board[3] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[0] == board[4] and board[0] == board[8]):
            printBoard(board)
            go = False
            if (board[0] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")
        if (board[6] == board[4] and board[6] == board[2]):
            printBoard(board)
            go = False
            if (board[6] == "X"):
                print("PLayer X has won the game!")
            else:
                print("PLayer O has won the game!")


        if (spotsFilled == 9):
            print("The board is full. Draw.")
            go = False

def printBoard(board):
    i = 0
    while(i < 9):
        print(" " + str(board[i]) + " | " + str(board[i+1]) + " | " + str(board[i+2]))
        if(i < 6):
            print("___________")
        i += 3

if __name__ == "__main__":
    playGame()