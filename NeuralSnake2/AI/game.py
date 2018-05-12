from copy import *
from field import *
from random import *
from constants import *
from vector2d import *
from direction import *

class Game(object):
    def __init__(self):
        self.running = True
        self._hunger = Constants.HUNGER_LIMIT

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

        self._body = []
        
    def initFood(self):
        for i in range(Constants.FOOD_COUNT):
            self.addFood()

    def nextTurn(self, direction):
        if not self.running: return

        nextPosition = self._head

        if   direction == Direction.UP:     nextPosition += vector2d(0, -1)
        elif direction == Direction.RIGHT:  nextPosition += vector2d(1, 0)
        elif direction == Direction.DOWN:   nextPosition += vector2d(0, 1)
        elif direction == Direction.LEFT:   nextPosition += vector2d(-1, 0)

        if not self.checkIfMoveIsLegal(nextPosition) or self._hunger <= 0:
            self.running = False
        else:
            if self.boardfields[nextPosition.x][nextPosition.y] == Field.FOOD:
                self.addFood()
                self._hunger = Constants.HUNGER_LIMIT

            self.boardfields[self._head.x][self._head.y] = Field.BODY
            self._body.append(deepcopy(self._head))

            if not self.boardfields[nextPosition.x][nextPosition.y] == Field.FOOD:
                lastBodyPart = self._body[0]
                self.boardfields[lastBodyPart.x][lastBodyPart.y] = Field.NONE
                self._body.remove(lastBodyPart)

                self._hunger -= 1

            self.boardfields[nextPosition.x][nextPosition.y] = Field.HEAD
            self._head = nextPosition

    def addFood(self):
        foodPositionFound = False
        while not foodPositionFound:
            foodPosition = self.getRandomPosition()
            if(self.boardfields[foodPosition.x][foodPosition.y] == Field.NONE):
                self.boardfields[foodPosition.x][foodPosition.y] = Field.FOOD
                foodPositionFound = True

    def getRandomPosition(self):
        return vector2d(randint(1, Constants.BOARD_WIDTH - 2), randint(1, Constants.BOARD_HEIGHT - 2))

    def getSnakeLength(self):
        return len(self._body) + 1

    def getSnakeEyes(self):
        return [self.checkIfFieldIsLegal(self.boardfields[self._head.x][self._head.y - 1]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x + 1][self._head.y]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x][self._head.y + 1]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x - 1][self._head.y])]

    def checkIfMoveIsLegal(self, nextPosition):
        field = self.boardfields[nextPosition.x][nextPosition.y]
        return self.checkIfFieldIsLegal(field)

    def checkIfFieldIsLegal(self, field):
        return field == Field.NONE or field == Field.FOOD