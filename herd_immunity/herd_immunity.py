import random
import time
import copy

class pop():
    """
    One of the many grateful denizens of Willopolis
    """
    def __init__(self, x, y):
        self.vax = False
        self.infected = False
        self.cured = False
        self.dead = False
        self.contagious = 0
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

    def infect(self, contag):
        """
        :return: Infects an uninfected living pop who has not had the disease
        """
        if not self.cured and not self.dead and not self.infected:
            self.infected = True
            self.contagious = contag
        return self

    def cure(self):
        """
        :return: Cures an infected pop
        """
        if self.infected:
            self.infected = False
            self.cured = True
            self.contagious = False
        return self

    def kill(self):
        """
        :return: Kills an infected pop
        """
        if self.infected:
            self.infected = False
            self.dead = True
            self.contagious = False
        return self

    def notContage(self):
        self.contagious = False

class disease():
    def __init__(self, infect, vaxresist, lethality, curability, contagtime):
        self.infectiousness = infect
        self.resistance = infect * vaxresist
        self.lethality = lethality
        self.curability = curability
        self.contagtime = contagtime

    def infect(self, pop):
        if pop.vax == False:
            if random.random() < self.infectiousness:
                pop.infect(self.contagtime)
        else:
            if random.random() < self.resistance:
                pop.infect(self.contagtime)

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

def adjinfect(board, row, col):
    adj = 0
    adj2 = []
    if row > 0:
        if (board[row-1][col].contagious > 0) and board[row-1][col].infected:
            adj += 1
            adj2.append("U")
    if row < len(board) - 1:
        if (board[row+1][col].contagious > 0) and board[row+1][col].infected:
            adj += 1
            adj2.append("D")
    if col < len(board[0]) - 1:
        if (board[row][col+1].contagious > 0) and board[row][col+1].infected:
            adj += 1
            adj2.append("R")
    if col > 0:
        if (board[row][col-1].contagious > 0) and board[row][col-1].infected:
            adj += 1
            adj2.append("L")
    return adj

def oneStep(oldboard, disease):
    board = copy.deepcopy(oldboard)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if random.random() < disease.curability:
                disease.cure(board[row][col])
            if random.random() < disease.lethality:
                disease.kill(board[row][col])
            if adjinfect(oldboard, row, col) > 0 and random.random() < disease.infectiousness:
                disease.infect(board[row][col])
            if oldboard[row][col].contagious > 0:
                board[row][col].contagious -= 1
    return board

def runSim(board, disease):
    pzerrow = random.choice(range(0, len(board)))
    pzercol = random.choice(range(0, len(board[0])))
    board[pzerrow][pzercol].infect(disease.contagtime)
    while True:
        printBoard(testboard)
        board = oneStep(board, disease)
        time.sleep(2)
        print("")

flu = disease(.9, .2, 0, .2, 3)
testboard = vaxedBoard(0, 8, 8)
runSim(testboard, flu)