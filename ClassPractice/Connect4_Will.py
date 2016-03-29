class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    def __init__(self, width, height):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        w = self.width
        h = self.height
        self.data = [[' ']*w for row in range(h)]

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        h = self.height
        w = self.width
        s = ''   # the string to return
        for row in range(0, h):
            s += '|'
            for col in range(0, w):
                s += self.data[row][col] + '|'
            s += '\n'
        s += (2*w+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0, w):
            s += " " + str(col % 10)
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
        if self.data[0][c] != " " or c < 0 or c >= self.width:
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
        for col in range(0,W-3):
            for row in range(0,H-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
        for col in range(0,W-3):
            for row in range(3,H):
                if D[row][col] == ox and D[row-1][col+1] == ox and D[row-2][col+2] == ox and D[row-3][col+3] == ox:
                    return True
        return False

    def hostGame(self):
        print self
        while True:
            x_move = -1
            while(self.allowsMove(x_move) == False):
                x_move = input("Choose a Column: ")
            self.addMove(x_move, "X")
            print self
            if self.winsFor("X"):
                print "X Wins!"
                break
            o_move = -1
            while(self.allowsMove(o_move) == False):
                o_move = input("Choose a Column: ")
            self.addMove(o_move, "O")
            print self
            if self.winsFor("O"):
                print "O Wins!"
                break

def copyBoard(board):
    output = Board(board.width, board.height)
    for row in range(board.height):
        for col in range(board.width):
            output.data[row][col] = board.data[row][col]
    return output

def connectFour():
    width = 7
    height = 6
    game = Board(width, height)
    game.hostGame()

# connectFour()

# Connect Four Tests
"""
print "---------------------------------------------"
print "print a 7 x 6 board with the columns numbered"
print "---------------------------------------------\n"
b = Board(7,6)
print b

print " "
print "---------------------------------------------"
print "test addMove"
print "---------------------------------------------\n"
print "| | | | | | | |"
print "| | | | | | | |"
print "| | | | | | | |"
print "|X| | | | | | |"
print "|O| | | | | | |"
print "|X| | |O|O|O|O|"
print "---------------"
print " 0 1 2 3 4 5 6\n"
print "==\n"
b.addMove(0, 'X')
b.addMove(0, 'O')
b.addMove(0, 'X')
b.addMove(3, 'O')
b.addMove(4, 'O')  # cheating by letting O go again!
b.addMove(5, 'O')
b.addMove(6, 'O')
print b

print " "
print "---------------------------------------------"
print "test clear"
print "---------------------------------------------\n"
print "print an empty board"
b.clear()
print b

print " "
print "---------------------------------------------"
print "test allowsMove"
print "---------------------------------------------\n"
b = Board(2,2)
b.addMove(0, 'X')
b.addMove(0, 'O')
print b
print " "
print "b.allowsMove(-1) should be False == ",b.allowsMove(-1)
print "b.allowsMove(0) should be False == ",b.allowsMove(0)
print "b.allowsMove(1) should be True == ",b.allowsMove(1)
#print "b.allowsMove(2) should be False == ",b.allowsMove(2)

print " "
print "---------------------------------------------"
print "test isFull"
print "---------------------------------------------\n"
b = Board(2,2)
print b
print " "
print "b.isFull() should be False == ", b.isFull()
print " "
b.setBoard( '0011' )
print b
print " "
print "b.isFull() should be True == ", b.isFull()


print " "
print "---------------------------------------------"
print "test delMove"
print "---------------------------------------------\n"

b = Board(2,2)
b.setBoard( '0011' )
print b
print "after the following commands: \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(0) \n \
The board should look like: \n \
| | | \n \
|X| | \n \
-----\n \
 0 1 \n \
 == "
b.delMove(1)
b.delMove(1)
b.delMove(1)
b.delMove(0)
print b

print " "
print "---------------------------------------------"
print "test winsFor"
print "---------------------------------------------\n"


b = Board(7,6)
b.setBoard( '00102030' )
print "if b.setBoard( '00102030' ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '00102030' ), then b.winsFor('O') should be True == ",b.winsFor('O')

b = Board(7,6)
b.setBoard( '23344545515'  )
print "if b.setBoard( '23344545515'  ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '23344545515'  ), then b.winsFor('O') should be False == ",b.winsFor('O')

print " "
print "---------------------------------------------"
print "host game"
print "---------------------------------------------\n"

# play your game with a friend, tell me who you played with, and confirm that everything works

print "I played with ________"
print "Everything works!"
print "or"
print "It doesn't work"
"""
