from window import *
from board import *

class Core(object):
    def __init__(self):
        self._window = Window(60)
        self._board = Board(10, 10);

    def run(self):
        self._window.run()