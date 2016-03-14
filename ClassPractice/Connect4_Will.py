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

    def addmove(self, col, ox):
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








game = Board(7, 6)
game.addmove(3, "O")
game.addmove(2, "X")
game.addmove(2, "O")
game.addmove(6, "X")
print game
