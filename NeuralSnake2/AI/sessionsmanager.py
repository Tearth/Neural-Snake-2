from time import *
from threading import *
from session import *
from constants import *
from direction import *
from genotypeoperators import *

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
                if not session.isRunning():
                    self._sessions = sorted(self._sessions, key=lambda x: x.getScore(), reverse=True)
                    first_parent_index = randint(0, 1)
                    second_parent_index = randint(first_parent_index + 1, 3)

                    first_parent = self._sessions[first_parent_index]
                    second_parent = self._sessions[second_parent_index]

                    self._sessions.remove(session)

                    genome = GenotypeOperators.breed(first_parent.genotype, second_parent.genotype)
                    genome_after_mutation = GenotypeOperators.mutate(genome)

                    self._sessions.append(Session(genome))

            sleep(self._refreshInterval)

    def getBoardState(self, boardIndex):
        return self._sessions[boardIndex].getBoardState()

    def getSessionInfo(self, boardIndex):
        return self._sessions[boardIndex].getSessionInfo()

    def stop(self):
        self.running = False