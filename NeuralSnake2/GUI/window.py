from tkinter import *;

class Window(object):
    def __init__(self):
        self._root = Tk()
        self._root.title("NeuralNetwork 2")
        self._root.geometry("600x400")
        self._root.resizable(False, False)

        self._canvas = Canvas(self._root, width=400, height=400, bg="white")
        self._canvas.pack(side="left")

    def run(self):
        self._root.mainloop()