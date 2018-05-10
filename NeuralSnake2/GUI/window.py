from tkinter import *
from random import randint

class Window(object):
    def __init__(self, board, fps):
        self._root = Tk()
        self._root.title("NeuralNetwork 2")
        self._root.geometry("600x400")
        self._root.resizable(False, False)

        self._canvas = Canvas(self._root, width=400, height=400, bg="white")
        self._canvas.pack(side="left")

        self._fpsText = StringVar()
        self._fpsLabel = Label(self._root, text="FPS: 0", textvariable=self._fpsText)
        self._fpsLabel.pack()

        self._refreshTime = int(1000 / fps)
        self._expectedFps = fps
        self._currentFps = 0
        self._fpsCounter = 0

        self._board = board

    def run(self):
        self._root.after(100, self.update)
        self._root.after(100, self.updateFps)
        self._root.mainloop()
        
    def update(self):
        self._fpsCounter += 1

        self._board.draw(self._canvas)
        self._root.after(self._refreshTime, self.update)

    def updateFps(self):
        self._root.after(1000, self.updateFps)

        self._currentFps = self._fpsCounter
        self._fpsCounter = 0

        self._fpsText.set("FPS: " + str(self._currentFps))