class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'
        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0,W):
            s += " " + str(col%10)
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        for row in range(self.height - 1, -1, -1):
            if self.data[row][col] == " ":
                self.data[row][col] = ox
                return

    def clear(self):
        for col in range(1, self.width):
            for row in range(1, self.height):
                self.data[row][col] = " "

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, c):
        if self.data[0][c] != " ":
            return False
        else:
            return True

    def isFull(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if self.data[row][col] == " ":
                    return False
        return True

    def delMove(self, c):
        for row in range(0, self.height):
            if self.data[row][c] != " ":
                self.data[row][c] = " "
                break

    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and D[row][col+1] == ox and D[row][col+2] == ox and D[row][col+3] == ox:
                    return True
        for col in range(0,W):
            for row in range(0,H-3):
                if D[row][col] == ox and D[row+1][col] == ox and D[row+2][col] == ox and D[row+3][col] == ox:
                    return True
        for row in range(0,W-3):
            for col in range(0,H-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
        for row in range(0,W-3):
            for col in range(3,H):
                if D[row][col] == ox and D[row+1][col-1] == ox and D[row+2][col-2] == ox and D[row+3][col-3] == ox:
                    return True
        return False

    def hostGame(self):
        print self
        while True:
            x_move = -1
            while(self.allowsMove(x_move) == False):
                x_move = input()
            self.addMove(x_move, "X")
            print self
            if self.winsFor("X"):
                print "X Wins!"
                break
            o_move = -1
            while(self.allowsMove(o_move) == False):
                o_move = input()
            self.addMove(o_move, "O")
            print self
            if self.winsFor("O"):
                print "O Wins!"
                break


game = Board(7,6)
game.hostGame()



