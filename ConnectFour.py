import numpy as np
import sys

board = np.array([["-","-","-","-","-","-"],["-","-","-","-","-","-"], ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"], ["-","-","-","-","-","-"], ["-","-","-","-","-","-"],
                  ["-","-","-","-","-","-"]])

def playGame():
    go = True
    print("Welcome to my Connect Four game! The game will now start...")

    player = "X"
    spotsFilled = 0

    while(go):
        printBoard(board)
        invalid = True
        while(invalid):
            choice = str(input("Which column does Player " + player + " choose?"))
            choice = choice.upper()
            if (choice != "A" and choice != "B" and choice != "C" and choice!= "D" and choice != "E" and choice != "F" and choice != "G"):
                print("Your choice must be one of the columns above.")
            else:
                if (choice == "A"):
                    choice = 0
                elif (choice == "B"):
                    choice = 1
                elif (choice == "C"):
                    choice = 2
                elif (choice == "D"):
                    choice = 3
                elif (choice == "E"):
                    choice = 4
                elif (choice == "F"):
                    choice = 5
                else:
                    choice = 6

                if (board[choice][5] != "-"):
                    print("This column is full. Please choose another.")
                else:
                    i = 0
                    while (i < 6):
                        if (board[choice][i] == "-"):
                            board[choice][i] = player
                            spotsFilled += 1
                            i = 6
                        i += 1
                    invalid = False
        #alternates players each loop
        if (player == "X"):
            player = "O"
        else:
            player = "X"

        #TEST FOR ALL POSSIBLE WIN CONDITIONS

        #Vertical win
        numCons = 1
        for i in range(7):
            for k in range(5):
                if (board[i][k] != "-" and board[i][k] == board[i][k+1]):
                    numCons += 1
                else:
                    numCons = 1
                if (numCons == 4):
                    winner = board[i][k]
                    printBoard(board)
                    print("Player " + winner + " has connected four vertically!")
                    go = False
                if (go and k == 4):
                    numCons = 1

        #Horizontal win
        numCons = 1
        for k in range(6):
            for i in range(6):
                if (board[i][k] != "-" and board[i][k] == board[i+1][k]):
                    numCons += 1
                else:
                    numCons = 1
                if (numCons == 4):
                    winner = board[i][k]
                    printBoard(board)
                    print("Player " + winner + " has connected four horizontally!")
                    go = False
                if (go and i == 5):
                    numCons = 1

        #Diagonal win
        #Positively sloped(/)i++k++
        numCons = 1
        for i in range(6):
            for k in range(5):
                j = i
                l = k
                while(j < 6 and l < 5):
                    if (board[j][l] != "-" and board[j][l] == board[j + 1][l + 1]):
                        numCons += 1
                    else:
                        numCons = 1
                    if (numCons == 4):
                        winner = board[j][l]
                        printBoard(board)
                        print("Player " + winner + " has connected four diagonally!")
                        go = False
                    if (go and j == 5):
                        numCons = 1
                    j += 1
                    l += 1

        #Negatively sloped(\)i++k--
        numCons = 1
        for i in range(6):
            for k in range(5):
                j = i
                l = k
                while (j < 6 and l < 5):
                    if (board[j][l] != "-" and board[j][l] == board[j + 1][l - 1]):
                        numCons += 1
                    else:
                        numCons = 1
                    if (numCons == 4):
                        winner = board[j][l]
                        printBoard(board)
                        print("Player " + winner + " has connected four diagonally!")
                        go = False
                    if (go and j == 5):
                        numCons = 1
                    j += 1
                    l -= 1

        if (spotsFilled >= 42):
            printBoard(board)
            print("The board is now full. Draw.")
            go = False


def printBoard(board):
    i = 0
    print("  A   B   C   D   E   F   G")
    print("_____________________________")
    k = 5
    while(k >= 0):
        print("| " + str(board[i][k]) + " | " + str(board[i+1][k]) + " | " + str(board[i+2][k]) +
              " | " + str(board[i+3][k]) + " | " + str(board[i+4][k]) + " | " + str(board[i+5][k]) +
              " | " + str(board[i+6][k]) + " |")
        print("_____________________________")
        k -= 1

if __name__ == "__main__":
    playGame()
