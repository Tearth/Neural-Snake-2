from time import *
from threading import *
from session import *
from constants import *
from direction import *

class SessionsManager(Thread):
    def __init__(self):
        super().__init__()

        self._refreshInterval = Constants.SESSION_REFRESH_INTERVAL / 1000
        self._sessions = []
        self.running = True

        self.createInitialSessions()
    
    def createInitialSessions(self):
        for i in range(Constants.SESSIONS_COUNT):
            self._sessions.append(Session())

    def run(self):
        while self.running:
            for session in self._sessions:
                session.nextTurn()
            sleep(self._refreshInterval)

    def getBoardState(self, boardIndex):
        return self._sessions[boardIndex].getBoardState()

    def stop(self):
        self.running = False