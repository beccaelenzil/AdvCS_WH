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
        self.willInfect = False
        self.cured = False
        self.willCure = False
        self.dead = False
        self.willDie = False
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
    """
    :type: To kill, or not to kill, that is the question
    """
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
    """
    :return: 
    """
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

def getType(board, row, col):
    if board[row][col].dead:
        return 'D'
    elif board[row][col].cured:
        return "C"
    elif board[row][col].infected:
        return 'I'
    elif board[row][col].vax:
        return 'V'
    else:
        return 'O'

def vaxedBoard(vaxprop, width, height):
    return [[pop(row, col).vaccinate() if random.random() < vaxprop else pop(row, col) for col in range(width)] for row in range(height)]

def adjinfect(board, row, col):
    adj = 0
    if row > 0:
        if (board[row-1][col].contagious > 0) and board[row-1][col].infected:
            adj += 1
    if row < len(board) - 1:
        if (board[row+1][col].contagious > 0) and board[row+1][col].infected:
            adj += 1
    if col < len(board[0]) - 1:
        if (board[row][col+1].contagious > 0) and board[row][col+1].infected:
            adj += 1
    if col > 0:
        if (board[row][col-1].contagious > 0) and board[row][col-1].infected:
            adj += 1
    return adj

def oneStep(board, disease):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if random.random() < disease.curability:
                board[row][col].willCure = True
            if random.random() < disease.lethality:
                board[row][col].willDie = True
            if adjinfect(board, row, col) > 0 and random.random() < disease.infectiousness:
                board[row][col].willInfect = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col].willCure:
                disease.cure(board[row][col])
                board[row][col].willCure = False
                board[row][col].contagious = 0
            elif board[row][col].willDie:
                disease.kill(board[row][col])
                board[row][col].willDie = False
            elif board[row][col].willInfect:
                disease.infect(board[row][col])
                board[row][col].willInfect = False
            if board[row][col].contagious > 0:
                board[row][col].contagious -= 1
    return board

def runSim(board, disease):
    pzerrow = random.choice(range(0, len(board)))
    pzercol = random.choice(range(0, len(board[0])))
    board[pzerrow][pzercol].infect(disease.contagtime)
    while True:
        printBoard(board)
        board = oneStep(board, disease)
        time.sleep(2)
        print("")

"""
flu = disease(.9, .2, 0, .2, 5)
testboard = vaxedBoard(0, 8, 8)
runSim(testboard, flu)
"""