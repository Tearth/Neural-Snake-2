from field import *
from constants import *

class Game(object):
    def __init__(self):
        self.boardfields = [Field.NONE] * Constants.BOARD_WIDTH
        for i in range(Constants.BOARD_WIDTH):
            self.boardfields[i] = [Field.NONE] * Constants.BOARD_HEIGHT

        self.initBoard()

    def initBoard(self):
        for x in range(Constants.BOARD_WIDTH):
            self.boardfields[x][0] = Field.WALL
            self.boardfields[x][Constants.BOARD_HEIGHT - 1] = Field.WALL

        for y in range(Constants.BOARD_HEIGHT):
            self.boardfields[0][y] = Field.WALL
            self.boardfields[Constants.BOARD_WIDTH - 1][y] = Field.WALL