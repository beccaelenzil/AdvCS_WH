import random

class pop():
    """
    One of the many grateful denizens of WillOpoplis
    """
    def __init__(self, x, y):
        self.vax = False
        self.infected = False
        self.cured = False
        self.dead = False
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def vaccinate(self):
        """
        :return: Vaccinates a pop whp is unvaccinated
        """
        if not self.vax:
            self.vax = True
        return self

    def infect(self):
        """
        :return: Infects an uninfected living pop who has not had the disease
        """
        if not self.cured and not self.dead and not self.infected:
            self.infected = True
        return self

    def cure(self):
        """
        :return: Cures an infected pop
        """
        if self.infected:
            self.infected = False
            self.cured = True
        return self

    def kill(self):
        """
        :return: Kills an infected pop
        """
        if self.infected:
            self.infected = False
            self.dead = True
        return self

class disease():
    def __init__(self, infect, vaxresist, lethality, curability):
        self.infectiousness = infect
        self.resistance = vaxresist
        self.lethality = lethality
        self.curability = curability

    def infect(self, pop):
        if pop.vax == False:
            if random.random() < self.infectiousness:
                pop.infect()
        else:
            if random.random() < self.resistance:
                pop.infect()

    def cure(self, pop):
        if pop.infected:
            if random.random() < self.curability:
                pop.cure()

    def kill(self, pop):
        if pop.infected:
            if random.random() < self.lethality:
                pop.kill()

def createBoard(width, height):
    return [[pop(row, col) for col in range(width)] for row in range(height)]

def printBoard(board):
    for row in board:
        line = ''
        for col in row:
            if col.dead:
                line += 'D'
            elif col.infected:
                line += 'I'
            elif col.vax:
                line += 'V'
            else:
                line += 'O'
        print line

def vaxedBoard(vaxprop, width, height):
    return [[pop(row, col).vaccinate() if random.random() < vaxprop else pop(row, col) for col in range(width)] for row in range(height)]

def adjacent(board, row, col):
    

def oneStep(board, disease):
    for row in range(len(board)):
        for col in range(len(board[0])):
