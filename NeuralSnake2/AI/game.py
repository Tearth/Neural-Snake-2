from copy import *
from math import *
from field import *
from random import *
from constants import *
from vector2d import *
from direction import *

class Game(object):
    def __init__(self):
        self.running = True
        self.age = 0
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
        self._foods = []
        for i in range(Constants.FOOD_COUNT):
            self.addFood()

    def nextTurn(self, direction):
        if not self.running: return

        nextPosition = self._head

        if   direction == Direction.TOP:    nextPosition += vector2d(0, -1)
        elif direction == Direction.RIGHT:  nextPosition += vector2d(1, 0)
        elif direction == Direction.BOTTOM: nextPosition += vector2d(0, 1)
        elif direction == Direction.LEFT:   nextPosition += vector2d(-1, 0)

        if not self.checkIfMoveIsLegal(nextPosition) or self._hunger <= 0:
            self.running = False
        else:
            if self.boardfields[nextPosition.x][nextPosition.y] == Field.FOOD:
                self.removeFood(nextPosition)
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
            self.age += 1

    def addFood(self):
        foodPositionFound = False
        while not foodPositionFound:
            foodPosition = self.getRandomPosition()
            if(self.boardfields[foodPosition.x][foodPosition.y] == Field.NONE):
                self.boardfields[foodPosition.x][foodPosition.y] = Field.FOOD
                self._foods.append(foodPosition)
                foodPositionFound = True

    def removeFood(self, foodPosition):
        for food in self._foods:
            if(food == foodPosition):
                self._foods.remove(food)
                break;

    def getRandomPosition(self):
        return vector2d(randint(1, Constants.BOARD_WIDTH - 2), randint(1, Constants.BOARD_HEIGHT - 2))

    def getSnakeLength(self):
        return len(self._body) + 1

    def getSnakeEyes(self):
        return [self.checkIfFieldIsLegal(self.boardfields[self._head.x][self._head.y - 1]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x + 1][self._head.y]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x][self._head.y + 1]),
                self.checkIfFieldIsLegal(self.boardfields[self._head.x - 1][self._head.y])]

    def getNearestFoodDirection(self):
        nearestFood = None
        nearestFoodDistance = 999999

        for food in self._foods:
            dist = sqrt(pow(food.x - self._head.x, 2) + pow(food.y - self._head.y, 2))
            if(dist < nearestFoodDistance):
                nearestFoodDistance = dist
                nearestFood = food

        if nearestFood == None: return [False, False, False, False]
        else:
            return [nearestFood.y < self._head.y,
                    nearestFood.x > self._head.x,
                    nearestFood.y > self._head.y,
                    nearestFood.x < self._head.x]

    def checkIfMoveIsLegal(self, nextPosition):
        field = self.boardfields[nextPosition.x][nextPosition.y]
        return self.checkIfFieldIsLegal(field)

    def checkIfFieldIsLegal(self, field):
        return field == Field.NONE or field == Field.FOOD