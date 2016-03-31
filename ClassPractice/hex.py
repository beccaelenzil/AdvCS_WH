import random
import copy

class Board():
    """ Board for Hex """
    def __init__(self, size):
        self.height = size
        self.width = size
        self.tiles = [["O"] * self.width for row in range(self.height)]

    def __repr__(self):
        """
        :return: Prints the hex board
        """
        height = self.height
        width = self.width
        # makes the board print out diagonally
        output = ""
        output += " " * (height + 2)
        for col in range(width):
            output += str(col % 10) + " "
        output += "\n"
        # prints out the numbrz
        for row in range(height):
            output += " " * (height - row)
            output += str(row % 10)
            output += " "
            for col in range(width):
                output += self.tiles[row][col] + " "
            output += "\n"
        return output

    def legal(self, row, col):
        """
        :return: Checks to see if a move is legal
        """
        if self.tiles[row][col] == "O":
            return True
        else:
            return False

    def play(self, piece, row, col):
        """
        :return: places a piece of type piece on the board in the stated location
        """
        if self.legal(row,col):
            self.tiles[row][col] = piece
            return True
        else:
            return False

    def nodeCheck(self, type, row, col):
        # Assumes all neighbours are empty nodes
        # Checks to see if neighbors are the same as the node being checked
        """
          0  1
         2  O  3
           4  5
        """
        full = [False, False, False, False, False, False]
        try:
            if self.tiles[row-1][col-1] == type:
                full[0] = True
        except IndexError:
            full[0] = False
        try:
            if self.tiles[row-1][col] == type:
                full[1] = True
        except IndexError:
            full[1] = False
        try:
            if self.tiles[row][col-1] == type:
                full[2] = True
        except IndexError:
            full[2] = False
        try:
            if self.tiles[row][col+1] == type:
                full[3] = True
        except IndexError:
            full[3] = False
        try:
            if self.tiles[row+1][col] == type:
                full[4] = True
        except IndexError:
            full[4] = False
        try:
            if self.tiles[row+1][col+1] == type:
                full[5] = True
        except IndexError:
            full[5] = False
        return full

    def checkWinHz(self, type):
        """
        :return: Checks for a horizontal win for a piece of type 'type'
        """
        checked = [["N"] * self.width for row in range(self.height)]
        more = False
        for i in range(self.height):
            if self.tiles[i][0] == type:
                checked[i][0] = "Y"
                reps = self.nodeCheck(type, i, 0)
                if reps[3]:
                    checked[i][1] = "P"
                    more = True
                try:
                    if reps[5]:
                        checked[i+1][1] = "P"
                        more = True
                except IndexError:
                    True
        while more:
            more = False
            for row in range(self.height):
                for col in range(self.height):
                    if checked[row][col] == "P":
                        if col == self.width - 1:
                            return [True, "H"]
                        checked[row][col] = "Y"
                        reps = self.nodeCheck(type, row, col)
                        try:
                            if (reps[0] == True) and (checked[row-1][col-1] != "Y"):
                                checked[row-1][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[1] == True) and (checked[row-1][col] != "Y"):
                                checked[row-1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[2] == True) and (checked[row][col-1] != "Y"):
                                checked[row][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[3] == True) and (checked[row][col+1] != "Y"):
                                checked[row][col+1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[4] == True) and (checked[row+1][col] != "Y"):
                                checked[row+1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[5] == True) and (checked[row+1][col+1] != "Y"):
                                checked[row+1][col+1] = "P"
                                more = True
                        except IndexError:
                            True
        return [False, "N"]

    def checkWinVt(self, type):
        """
        :return: checks for a vertical win for a piece of type 'type'
        """
        checked = [["N"] * self.width for row in range(self.height)]
        more = False
        for i in range(self.width):
            if self.tiles[0][i] == type:
                checked[0][i] = "Y"
                reps = self.nodeCheck(type, 0, i)
                if reps[4] == True:
                    checked[1][i] = "P"
                    more = True
                try:
                    if reps[5] == True:
                        checked[1][i+1] = "P"
                        more = True
                except IndexError:
                    True
        while more == True:
            more = False
            for row in range(self.width):
                for col in range(self.width):
                    if checked[row][col] == "P":
                        if row == self.height - 1:
                            return [True, "V"]
                        checked[row][col] = "Y"
                        reps = self.nodeCheck(type, row, col)
                        try:
                            if (reps[0] == True) and (checked[row-1][col-1] != "Y"):
                                checked[row-1][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[1] == True) and (checked[row-1][col] != "Y"):
                                checked[row-1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[2] == True) and (checked[row][col-1] != "Y"):
                                checked[row][col-1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[3] == True) and (checked[row][col+1] != "Y"):
                                checked[row][col+1] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[4] == True) and (checked[row+1][col] != "Y"):
                                checked[row+1][col] = "P"
                                more = True
                        except IndexError:
                            True
                        try:
                            if (reps[5] == True) and (checked[row+1][col+1] != "Y"):
                                checked[row+1][col+1] = "P"
                                more = True
                        except IndexError:
                            True
        return [False, "N"]

    def playGame(self):
        """
        return: Plays a text based version of the game "Hex"
        """
        print("Player one is X, player 2 is W\nPlayer one goes first")
        print("X wants to connect horizontally, W wants to connect vertically\n")
        print self
        while True:
            allowed = False
            print "Player 1"
            p1row = int(input("Row: "))
            p1col = int(input("Column: "))
            allowed = self.legal(p1row, p1col)
            while not allowed:
                print("Illegal Move! Try again.")
                p1row = int(input("Row: "))
                p1col = int(input("Column: "))
                allowed = self.legal(p1row, p1col)
            self.play("X", p1row, p1col)
            print self
            if self.checkWinHz("X") == True:
                print("Player 1 Wins!")
                return
            allowed = False
            print "Player 2"
            p2row = int(input("Row: "))
            p2col = int(input("Column: "))
            allowed = self.legal(p2row, p2col)
            while not allowed:
                print("Illegal Move! Try again.")
                p2row = int(input("Row: "))
                p2col = int(input("Column: "))
                allowed = self.legal(p2row, p2col)
            self.play("W", p2row, p2col)
            print self
            if self.checkWinVt("W") == True:
                print("Player 2 Wins!")
                return

class hexAI():
    """Basic AI player"""
    def __init__(self, hv):
        """
        :return: initiates with a tile type
        """
        #The type of tile to be played
        self.hv = hv

class hexLv1(hexAI):
    """Really bad AI player"""
    def __init__(self, hv):
        hexAI.__init__(self, hv)

    def play(self, board):
        """
        :return Plays a random legal move on the board
        """
        needsmove = True
        while needsmove:
            # Picks a random square on the board that is a legal move
            row = random.choice(range(board.height))
            col = random.choice(range(board.width))
            if board.legal(row, col):
                needsmove = False
        # Plays the move
        board.play(self.hv, row, col)

class hexLv2(hexAI):
    """This one isn't as dumb"""
    def __init__(self, hv):
        hexAI.__init__(self, hv)
        self.lastmove = [0,0]

    def otherTile(self):
        """
        :return: The other type of tile
        """
        if self.hv == "H":
            return "V"
        else:
            return "H"

    def wins(self, board, row, col):
        """
        :return: Tells if you can win on that square this move
        """
        b = copy.deepcopy(board)
        b.play(self.hv, row, col)
        if self.hv == "H":
            if b.checkWinHz("H")[0]:
                return True
            else:
                return False
        if self.hv == "V":
            if b.checkWinVt("V")[0]:
                return True
            else:
                return False

    def opWins(self, board, row, col):
        """
        :return: Tels if the opponent will win on that square on the next move
        """
        b = copy.deepcopy(board)
        b.play(self.otherTile(), row, col)
        if self.otherTile() == "H":
            if b.checkWinHz("H")[0]:
                return True
            else:
                return False
        if self.otherTile() == "V":
            if b.checkWinVt("V")[0]:
                return True
            else:
                return False
        return False

    def emptyBetweenVD(self, board, row, col):
        # Checks if the tiles looking down are empty
        try:
            if (board.tiles[row+1][col] == "O") and (board.tiles[row+1][col+1] == "O") and (board.tiles[row+2][col] == "O") and (board.tiles[row+2][col+2] == "O") and (board.tiles[row+2][col+1] == "V"):
                return True
            else:
                return False
        except IndexError:
            return False

    def emptyBetweenVU(self, board, row, col):
        # Checks if the tiles looking up are empty
        try:
            if (board.tiles[row-1][col] == "O") and (board.tiles[row-1][col-1] == "O") and (board.tiles[row-2][col] == "O") and (board.tiles[row-2][col-2] == "O") and (board.tiles[row-2][col-1] == "V"):
                return True
            else:
                return False
        except IndexError:
            return False

    def emptyBetweenHL(self, board, row, col):
        # Checks if the tiles looking left are empty
        try:
            if (board.tiles[row][col-1] == "O") and (board.tiles[row-1][col-1] == "O") and (board.tiles[row][col-2] == "O") and (board.tiles[row-2][col-2] == "O") and (board.tiles[row-1][col-2] == "H"):
                return True
            else:
                return False
        except IndexError:
            return False

    def emptyBetweenHR(self, board, row, col):
        # Checks if the tiles looking right are empty
        try:
            if (board.tiles[row][col+1] == "O") and (board.tiles[row+1][col+1] == "O") and (board.tiles[row][col+2] == "O") and (board.tiles[row+2][col+2] == "O") and (board.tiles[row+1][col+2] == "H"):
                return True
            else:
                return False
        except IndexError:
            return False

    def defend(self, board, row, col):
        """
        :return: Trys to defend against an opponent attack
        """
        if self.hv == "H":
            if self.emptyBetweenVD(board, row, col):
                return True
            if self.emptyBetweenVU(board, row, col):
                return True
            return False
        if self.hv == "V":
            if self.emptyBetweenHL(board, row, col):
                return True
            if self.emptyBetweenHR(board, row, col):
                return True
            return False

    def nextToOther(self, board, row, col):
        """
        :return: The number of the other type of tile next to any square
        """
        Ot = self.otherTile()
        any = False
        count = 0
        try:
            if board.tiles[row-1][col-1] == Ot:
                count += 1
                any = True
        except IndexError:
            True
        try:
            if board.tiles[row-1][col] == Ot:
                count +=1
                any = True
        except IndexError:
            True
        try:
            if board.tiles[row][col-1] == Ot:
                count += 1
                any = True
        except IndexError:
            True
        try:
            if board.tiles[row+1][col] == Ot:
                count += 1
                any = True
        except IndexError:
            True
        try:
            if board.tiles[row+1][col+1] == Ot:
                count += 1
                any = True
        except IndexError:
            True
        try:
            if board.tiles[row][col+1] == Ot:
                count += 1
                any = True
        except IndexError:
            True
        return [any, count]

    def canBlockH(self, board, row, col):
        """
        :return: Tells us if a block is possible against H
        """
        try:
            if ((board.tiles[row][col-1] == "H") and (board.tiles[row+1][col] == "V")) or ((board.tiles[row-1][col-1] == "H") and (board.tiles[row-1][col] == "V")) or ((board.tiles[row+1][col+1] == "H") and (board.tiles[row+1][col] == "V")) or ((board.tiles[row][col+1] == "H") and (board.tiles[row-1][col] == "V")):
                return True
            else:
                return False
        except IndexError:
            return False

    def canBlockV(self, board, row, col):
        """
        :return: Tells us if a block is possible against V
        """
        try:
            if ((board.tiles[row-1][col-1] == "V") and (board.tiles[row][col-1] == "H")) or ((board.tiles[row-1][col] == "V") and (board.tiles[row][col+1] == "H")) or ((board.tiles[row+1][col] == "V") and (board.tiles[row][col-1] == "H")) or ((board.tiles[row+1][col+1] == "V") and (board.tiles[row][col+1] == "H")):
                return True
            else:
                return False
        except IndexError:
            return False

    def block(self, board, row, col):
        """
        :return: Tries to block an opponent's attack
        """
        if self.hv == "V":
            if self.canBlockH(board, row, col):
                return True
            return False
        if self.hv == "H":
            if self.canBlockV(board, row, col):
                return True
            return False

    def isOpposite(self, board, row, col):
        """
        :return: Checks if a move can break a potential path
        """
        Ot = self.otherTile()
        try:
            if (board.tiles[row-1][col] == Ot) and (board.tiles[row+1][col] == Ot) and self.nextToOther(board, row, col)[1] == 2:
                return True
            elif (board.tiles[row][col-1] == Ot) and (board.tiles[row][col+1] == Ot) and self.nextToOther(board, row, col)[1] == 2:
                return True
            elif (board.tiles[row-1][col-1] == Ot) and (board.tiles[row+1][col+1] == Ot) and self.nextToOther(board, row, col)[1] == 2:
                return True
            else:
                return False
        except IndexError:
            return False

    def play(self, board):
        """
        :return: Tries to not be a moron when playing
        """
        vals = [[0] * board.width for row in range(board.height)]
        optimals = []
        justBlocked = False
        for row in range(board.height):
            for col in range(board.width):
                adjacency = self.nextToOther(board, row, col)
                if board.tiles[row][col] != "O":
                    vals[row][col] = -100
                elif self.wins(board, row, col):
                    vals[row][col] = 100
                elif self.opWins(board, row, col):
                    vals[row][col] = 90
                elif self.block(board, row, col):
                    vals[row][col] = 85
                elif self.isOpposite(board, row, col):
                    vals[row][col] = 86
                elif self.defend(board, row, col):
                    vals[row][col] = 80
                elif adjacency[0]:
                    vals[row][col] = 70
                    if adjacency[1] == (2 or 3):
                        vals[row][col] += 5
                else:
                    vals[row][col] = 0
            optimals.append(max(vals[row]))
        optimal = max(optimals)
        indices = []
        for row in range(board.height):
            for col in range(board.width):
                if vals[row][col] == optimal:
                    indices.append([row, col])
        choice = random.choice(indices)
        self.lastmove = choice
        board.play(self.hv, choice[0], choice[1])


# Board(6).playGame()

"""
test = Board(4)
test.playGame()
"""
