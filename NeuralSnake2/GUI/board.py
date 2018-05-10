from field import *

class Board(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._needToUpdate = True;

        self._fields = [Field.NONE] * width
        for i in range(self._width):
            self._fields[i] = [Field.NONE] * height

    def draw(self, canvas):
        if(not self._needToUpdate):
            return

        self._needToUpdate = False
        canvas.delete("all")

        fieldWidth = canvas.winfo_width() / self._width
        fieldHeight = canvas.winfo_height() / self._height

        for x in range(self._width):
            for y in range(self._height):
                fieldPositionX = x * fieldWidth
                fieldPositionY = y * fieldHeight
                color = self.getFieldColor(self._fields[x][y])

                canvas.create_rectangle(fieldPositionX, fieldPositionY, fieldPositionX + fieldWidth, fieldPositionY + fieldHeight, fill=color, outline="lightgray")

    def getFieldColor(self, field):
        if   field == Field.NONE:   return "white"
        elif field == Field.HEAD:   return "violet"
        elif field == Field.BODY:   return "blue"
        elif field == Field.FOOD:   return "green"
        elif field == Field.WALL:   return "red"