from window import *

class Core(object):
    def __init__(self):
        self._window = Window()

    def run(self):
        self._window.run()