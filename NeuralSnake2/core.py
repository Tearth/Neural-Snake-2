from threading import *
from board import *
from sessionsmanager import *

class Core(Thread):
    def __init__(self, window):
        super().__init__()

        self._board = Board()
        self._window = window
        self._window.setBoard(self._board)
        
        self._refreshTime = int(1000 / Constants.FPS)
        self._sessionsManager = SessionsManager()
        
        self._window._root.after(100, self.update)

    def run(self):
        self._sessionsManager.start()

    def update(self):
        self._window._root.after(self._refreshTime, self.update)
        self._board.update(self._sessionsManager.getBoardState(0))

    def stop(self):
        self._sessionsManager.stop()