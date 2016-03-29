import random

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
                            return True
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
        return False

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
                            return True
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
        return False

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
        self.hv = hv

    def randPlay(self, board):
        """
        :return Plays a random legal move on the board
        """
        needsmove = True
        while needsmove:
            row = random.choice(range(board.height))
            col = random.choice(range(board.width))
            if board.legal(row, col):
                needsmove = False
        board.play(self.hv, row, col)







"""
test = Board(4)
test.playGame()
"""