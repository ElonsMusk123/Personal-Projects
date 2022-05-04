import numpy as np
import random

payout = 1.5

class Player:
    name = ""
    balance = 0.0
    wager = 0.0
    winCount = 0
    lossCount = 0
    winnings = 0.0
    choice = 0
    playing = False

    #def __init__(self, _name, _bal, _wag, _WC, _LC, _win, _choice, _play):
     #   self.name = _name
      #  self.balance = _bal
       # self.wager = _wag
        #self.winCount = _WC
        #self.lossCount = _LC
        #self.winnings = _win
        #self.choice = _choice
        #self.playing = _play

    def setName(self, _name):
        self.name = _name

    def getName(self):
        return self.name

    def setBalance(self, _bal):
        self.balance = _bal

    def getBalance(self):
        return self.balance

    def setWager(self, _wag):
        self.wager = _wag

    def getWager(self):
        return self.wager

    def getWinCount(self):
        return self.winCount

    def getLossCount(self):
        return self.lossCount

    def getWinnings(self):
        return self.winnings

    def setChoice(self, _choice):
        self.choice = _choice

def playGame():
    valid = False
    while (not valid):
        try:
            val = int(input("How many players are playing? "))
        except ValueError:
            print("Your answer must be a number.")
        else:
            valid = True;
    cycle = [Player() for i in range(val)]

    for i in range(len(cycle)):
        cycle[i].name = str(input("Enter player #" + str((i+1)) + "'s name. "))
        valid = False
        while (not valid):
            try:
                cycle[i].balance = float(input("How much money does this player have? "))
            except ValueError:
                print("Your balance must be a number.")
            else:
                if (cycle[i].balance <= 0):
                    print("Your balance must be greater than 0.")
                else:
                    valid = True
        cycle[i].playing = True

    playersOut = 0
    go = True

    while(go):
        for j in range(len(cycle)):
            if (cycle[j].playing):
                valid = False
                while(not valid):
                    try:
                        cycle[j].wager = float(input("How much would " + cycle[j].name + " like to bet?" +
                                                " Balance: " + str(cycle[j].balance) + " "))
                    except ValueError:
                        print("Your wager must be a number.")
                    else:
                        if (cycle[j].wager > cycle[j].balance):
                            print("You cannot bet more than your available balance.")
                        elif(cycle[j].wager <= 0):
                            print("Your wager must be greater than 0.")
                        else:
                            valid = True
                valid = False
                while (not valid):
                    try:
                        cycle[j].choice = int(input("Do you choose heads or tails? (Enter 1 for heads and 0 for tails) "))
                    except ValueError:
                        print("You must enter 1 or 0 only.")
                    else:
                        if (not(cycle[j].choice == 1 or cycle[j].choice == 0)):
                            print("You must enter 1 or 0 only.")
                        else:
                            valid = True
                result = flipCoin(cycle[j].wager, cycle[j].choice)
                if result == 0:
                    print("Sorry, you lost $" + str(cycle[j].wager))
                    cycle[j].lossCount += 1;
                    cycle[j].balance -= cycle[j].wager
                    cycle[j].winnings -= cycle[j].wager
                else:
                    print("Congrats! You won $" + str(result))
                    cycle[j].winnings += result
                    cycle[j].winCount += 1
                    cycle[j].balance += result
                if cycle[j].balance == 0:
                    print("Your balance is now empty.")
                    var = 0
                else:
                    valid = False
                    while (not valid):
                        try:
                            var = int(input("Would you like to bet again?(1 for yes, 0 for no) "))
                        except ValueError:
                            print("You must enter 1 or 0 only.")
                        else:
                            if (not (cycle[j].choice == 1 or cycle[j].choice == 0)):
                                print("You must enter 1 or 0 only.")
                            else:
                                valid = True
                if var == 0:
                    cycle[j].playing = False
                    playersOut += 1
                    if (cycle[j].winnings >= 0):
                        print("Cashing out..."  + str(cycle[j].name) + " won $" + str(cycle[j].winnings))
                    else:
                        print("Cashing out..." + str(cycle[j].name) + " lost $" + str(-(cycle[j].winnings)))
                else:
                    print(cycle[j].name + " will be in the next round.")
        if playersOut == len(cycle):
            print("The game has now concluded. Thanks for playing!")
            print("")
            for m in cycle:
                print(str(m.name) + " stats: ")
                print("Win Count: " + str(m.getWinCount()))
                print("Loss Count: " + str(m.getLossCount()))
                print("Winnings: " + str(m.getWinnings()))
                print("")
            go = False

def flipCoin(_wager, _choice):
    var = random.random()
    var = int(var * 100)
    if (var % 2 == 0):
        print("Heads")
    else:
        print("Tails")
    if ((var % 2 == 0) and _choice == 1) or ((var % 2 == 1) and _choice == 0):
        return _wager * payout
    return 0


if __name__ == "__main__":
    playGame()
