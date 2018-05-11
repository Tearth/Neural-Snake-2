from copy import *
from field import *
from constants import *


class Board(object):
    def __init__(self):
        self._needToUpdate = True;

        self._fields = [Field.NONE] * Constants.BOARD_WIDTH
        for i in range(Constants.BOARD_WIDTH):
            self._fields[i] = [Field.NONE] * Constants.BOARD_HEIGHT

        self._objects = {}

    def initBoard(self, canvas):
        fieldWidth = canvas.winfo_width() / Constants.BOARD_WIDTH
        fieldHeight = canvas.winfo_height() / Constants.BOARD_HEIGHT

        for x in range(Constants.BOARD_WIDTH):
            for y in range(Constants.BOARD_HEIGHT):
                fieldPositionX = x * fieldWidth
                fieldPositionY = y * fieldHeight
                color = self.getFieldColor(self._fields[x][y])
                
                rectId = canvas.create_rectangle(fieldPositionX, fieldPositionY, fieldPositionX + fieldWidth, fieldPositionY + fieldHeight, fill=color, outline="lightgray")
                self._objects["{0}|{1}".format(x, y)] = rectId

    def update(self, fields):
        for x in range(Constants.BOARD_WIDTH):
            for y in range(Constants.BOARD_HEIGHT):
                if(self._fields[x][y] != fields[x][y]):
                    self._fields[x][y] = fields[x][y]
                    self._needToUpdate = True

    def draw(self, canvas):
        if(len(self._objects) == 0):
            self.initBoard(canvas)

        if(not self._needToUpdate):
            return

        for x in range(Constants.BOARD_WIDTH):
            for y in range(Constants.BOARD_HEIGHT):
                color = self.getFieldColor(self._fields[x][y])
                rectId = self._objects["{0}|{1}".format(x, y)]

                if(color != canvas.itemcget(rectId, "fill")):
                    canvas.itemconfig(rectId, fill=color)

        self._needToUpdate = False

    def getFieldColor(self, field):
        if   field == Field.NONE:   return "white"
        elif field == Field.HEAD:   return "violet"
        elif field == Field.BODY:   return "blue"
        elif field == Field.FOOD:   return "green"
        elif field == Field.WALL:   return "red"