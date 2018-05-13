from tkinter import *
from board import *
from random import *
from constants import *

class Window(object):
    def __init__(self):

        self._root = Tk()
        self._root.title("NeuralNetwork 2")
        self._root.geometry("600x400")
        self._root.resizable(False, False)

        self._canvas = Canvas(self._root, width=395, height=395, bg="white")
        self._canvas.grid(column=0,row=0,sticky=N,rowspan=50)

        # Input snake direction
        self._fpsText = StringVar()
        self._fpsLabel = Label(self._root, textvariable=self._fpsText,anchor="center",width="25")
        self._fpsLabel.grid(column=1,row=0,columnspan=2,sticky=N)

        self._inputTopText = StringVar()
        self._inputTopLabel = Label(self._root, textvariable=self._inputTopText)
        self._inputTopLabel.grid(column=1,row=1,sticky=N+W)

        self._inputRightText = StringVar()
        self._inputRightLabel = Label(self._root, textvariable=self._inputRightText)
        self._inputRightLabel.grid(column=1,row=2,sticky=N+W)

        self._inputBottomText = StringVar()
        self._inputBottomLabel = Label(self._root, textvariable=self._inputBottomText)
        self._inputBottomLabel.grid(column=1,row=3,sticky=N+W)

        self._inputLeftText = StringVar()
        self._inputLeftLabel = Label(self._root, textvariable=self._inputLeftText)
        self._inputLeftLabel.grid(column=1,row=4,sticky=N+W)

        # Input nearest food direction
        self._inputFoodTopText = StringVar()
        self._inputFoodTopLabel = Label(self._root, textvariable=self._inputFoodTopText)
        self._inputFoodTopLabel.grid(column=1,row=5,sticky=N+W)

        self._inputFoodRightText = StringVar()
        self._inputFoodRightLabel = Label(self._root, textvariable=self._inputFoodRightText)
        self._inputFoodRightLabel.grid(column=1,row=6,sticky=N+W)

        self._inputFoodBottomText = StringVar()
        self._inputFoodBottomLabel = Label(self._root, textvariable=self._inputFoodBottomText)
        self._inputFoodBottomLabel.grid(column=1,row=7,sticky=N+W)

        self._inputFoodLeftText = StringVar()
        self._inputFoodLeftLabel = Label(self._root, textvariable=self._inputFoodLeftText)
        self._inputFoodLeftLabel.grid(column=1,row=8,sticky=N+W)

        # Output snake direction
        self._outputTopText = StringVar()
        self._outputTopLabel = Label(self._root, textvariable=self._outputTopText)
        self._outputTopLabel.grid(column=2,row=1,sticky=N+W)

        self._outputRightText = StringVar()
        self._outputRightLabel = Label(self._root, textvariable=self._outputRightText)
        self._outputRightLabel.grid(column=2,row=2,sticky=N+W)

        self._outputBottomText = StringVar()
        self._outputBottomLabel = Label(self._root, textvariable=self._outputBottomText)
        self._outputBottomLabel.grid(column=2,row=3,sticky=N+W)

        self._outputLeftText = StringVar()
        self._outputLeftLabel = Label(self._root, textvariable=self._outputLeftText)
        self._outputLeftLabel.grid(column=2,row=4,sticky=N+W)

        self._refreshTime = int(1000 / Constants.FPS)
        self._currentFps = 0
        self._fpsCounter = 0

        self._board = Board()

    def run(self):
        self._root.after(100, self.update)
        self._root.after(100, self.updateFps)
        self._root.mainloop()
        
    def update(self):
        self._root.after(self._refreshTime, self.update)
        self._fpsCounter += 1

        if(self._board != None):
            self._board.draw(self._canvas)

    def updateFps(self):
        self._root.after(1000, self.updateFps)

        self._currentFps = self._fpsCounter
        self._fpsCounter = 0

        self._fpsText.set("FPS: " + str(self._currentFps))

    def updateBoard(self, boardState):
        self._board.update(boardState)

    def updateSessionInfo(self, sessionInfo):
        self._inputTopText.set("TOP: " + str(sessionInfo['input'][0]))
        self._inputRightText.set("RGH: " + str(sessionInfo['input'][1]))
        self._inputBottomText.set("BTM: " + str(sessionInfo['input'][2]))
        self._inputLeftText.set("LFT: " + str(sessionInfo['input'][3]))
        
        self._inputFoodTopText.set("F_TOP: " + str(sessionInfo['input'][4]))
        self._inputFoodRightText.set("F_RGH: " + str(sessionInfo['input'][5]))
        self._inputFoodBottomText.set("F_BTM: " + str(sessionInfo['input'][6]))
        self._inputFoodLeftText.set("F_LFT: " + str(sessionInfo['input'][7]))
        
        self._outputTopText.set("O_TOP: " + "{:.3f}".format(sessionInfo['output'][0]))
        self._outputRightText.set("O_RGH: " + "{:.3f}".format(sessionInfo['output'][1]))
        self._outputBottomText.set("O_BTM: " + "{:.3f}".format(sessionInfo['output'][2]))
        self._outputLeftText.set("O_LFT: " + "{:.3f}".format(sessionInfo['output'][3]))