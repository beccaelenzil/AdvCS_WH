import random
from Connect4_Will import *
import copy
import sys

class basicPlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        col = -1
        while b.allowsMove(col) == False:
            col = random.randrange(b.width)
        return col

class smartPlayer(basicPlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basicPlayer.__init__(self, ox)

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s

    def oppCh(self):
        if self.ox == "X":
            return "O"
        else:
            return "X"

    def canWin(self, loc, Board, ox):
        testBoard = copyBoard(Board)
        testBoard.addMove(loc, ox)
        outcome = testBoard.winsFor(ox)
        if outcome:
            return True
        else:
            return False

    def scoresFor(self, Board):
        vals = [50] * Board.width
        for i in range(Board.width):
            if not Board.allowsMove(i):
                vals[i] = -1
            elif self.canWin(i, Board, self.ox):
                vals[i] = 100
            else:
                looses = False
                testBoard = copyBoard(Board)
                testBoard.addMove(i, self.ox)
                for j in range(Board.width):
                    if self.canWin(j, testBoard, self.oppCh()):
                        looses = True
                if looses:
                    vals[i] = 0
        return vals

    def nextMove(self, Board):
        vals = self.scoresFor(Board)
        maxVal = max(vals)
        indices = []
        for i in range(Board.width):
            if vals[i] == maxVal:
                indices.append(i)
        return random.choice(indices)

def playGame(playerX, playerO):
    """
    playerX should be 'basic', 'smart' or 'human'
    playerO should be 'basic', 'smart' or 'human'
    """
    if playerX == 'smart':
        pX = smartPlayer('X')
    elif playerX == 'basic':
        pX = basicPlayer('X')
    elif playerX != 'human':
        print "Player X should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()
    if playerO == 'smart':
        pO = smartPlayer('O')
    elif playerO == 'basic':
        pO = basicPlayer('O')
    elif playerO != 'human':
        print "Player O should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()
    b = Board(7,6)
    # print b
    while True:
        x_move = -1
        while(b.allowsMove(x_move) == False):
            if pX == "human":
                x_move = input("Choose a Column: ")
            else:
                x_move = pX.nextMove(b)
                # print "X chose: ", x_move, "\n"
        b.addMove(x_move, "X")
        # print b
        if b.winsFor("X"):
            # print "X Wins!"
            return "X"
        elif b.isFull():
            # print "Draw"
            return "Draw"
        o_move = -1
        while(b.allowsMove(o_move) == False):
            if pO == "human":
                o_move = input("Choose a Column: ")
            else:
                o_move = pO.nextMove(b)
                # print "O chose: ", o_move, "\n"
        b.addMove(o_move, "O")
        # print b
        if b.winsFor("O"):
            # print "O Wins!"
            return "O"
        elif b.isFull():
            # print "Draw"
            return "Draw"

def trials(n):
    results = {"X":0, "O":0, "Draw":0}
    for i in range(n):
        results[playGame('smart', 'basic')] += 1
    print results

trials(10000)
