class Board():
    """ Board for Hex """
    def __init__(self, size):
        self.height = size
        self.width = size
        self.tiles = [["X"] * self.width for row in range(self.height)]

    def __repr__(self):
        height = self.height
        width = self.width
        output = ""
        output += " " * (height + 2)
        for col in range(width):
            output += str(col % 10) + " "
        output += "\n"
        for row in range(height):
            output += " " * (height - row)
            output += str(row % 10)
            output += " "
            for col in range(width):
                output += self.tiles[row][col] + " "
            output += "\n"
        return output

    def legal(self, row, col):
        if self.tiles[row][col] == "X":
            return True
        else:
            return False

    def play(self, piece, row, col):
        if self.legal(row,col):
            self.tiles[row][col] = piece
        else:
            return False


test = Board(6)
test.play("O", 2 ,2)
print test