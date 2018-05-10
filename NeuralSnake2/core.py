from window import *
from board import *

class Core(object):
    def __init__(self):
        self._board = Board(15, 15)
        self._window = Window(self._board, 60)

    def run(self):
        self._window.run()