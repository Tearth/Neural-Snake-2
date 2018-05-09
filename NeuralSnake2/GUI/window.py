from tkinter import *;

class Window(object):
    def __init__(self):
        self._root = Tk()
        self._root.title("NeuralNetwork 2")
        self._root.geometry("600x400")

    def run(self):
        self._root.mainloop()