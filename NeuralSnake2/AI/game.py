from field import *
from random import *
from constants import *
from vector2d import *

class Game(object):
    def __init__(self):
        self.boardfields = [Field.NONE] * Constants.BOARD_WIDTH
        for i in range(Constants.BOARD_WIDTH):
            self.boardfields[i] = [Field.NONE] * Constants.BOARD_HEIGHT

        self.initBoard()
        self.initSnake()
        self.initFood()

    def initBoard(self):
        for x in range(Constants.BOARD_WIDTH):
            self.boardfields[x][0] = Field.WALL
            self.boardfields[x][Constants.BOARD_HEIGHT - 1] = Field.WALL

        for y in range(Constants.BOARD_HEIGHT):
            self.boardfields[0][y] = Field.WALL
            self.boardfields[Constants.BOARD_WIDTH - 1][y] = Field.WALL

    def initSnake(self):
        self._head = self.getRandomPosition() 
        self.boardfields[self._head.x][self._head.y] = Field.HEAD
        
    def initFood(self):
        for i in range(Constants.FOOD_COUNT):
            self.addFood()

    def addFood(self):
        foodPositionFound = False
        while not foodPositionFound:
            foodPosition = self.getRandomPosition()
            if(self.boardfields[foodPosition.x][foodPosition.y] == Field.NONE):
                self.boardfields[foodPosition.x][foodPosition.y] = Field.FOOD
                foodPositionFound = True

    def getRandomPosition(self):
        return vector2d(randint(1, Constants.BOARD_WIDTH - 1), randint(1, Constants.BOARD_HEIGHT - 2))