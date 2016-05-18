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

    def infect(self):
        """
        :return: Infects an uninfected living pop who has not had the disease
        """
        if not self.cured and not self.dead and not self.infected:
            self.infected = True

    def cure(self):
        """
        :return: Cures an infected pop
        """
        if self.infected:
            self.infected = False
            self.cured = True

    def kill(self):
        """
        :return: Kills an infected pop
        """
        if self.infected:
            self.infected = False
            self.dead = True

class disease():
    def __init__(self, infect, vaxresist, lethality):
        self.infectiousness = infect
        self.resistance = vaxresist
        self.lethality = lethality

    def infect(self, pop):
        if pop.vax == False:
            if random.random() < self.infectiousness:
                pop.infect()
        else:
            if random.random() < self.resistance:
                pop.infect()

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
            line += str(col)
        print line


