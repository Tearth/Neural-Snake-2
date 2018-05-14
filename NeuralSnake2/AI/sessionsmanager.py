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
            do_next_generation = True
            for session in self._sessions:
                session.nextTurn()
                if(session.isRunning()):
                    do_next_generation = False

            if do_next_generation:
                new_sessions = []
                best = 0
                sum = 0
                
                sorted_sessions = self._sessions
                
                best_games = sorted_sessions[0:Constants.BEST_GAMES_BREED_COUNT]

                for i in range(Constants.RANDOM_GAMES_BREED_COUNT):
                    best_games.append(sorted_sessions[randint(Constants.BEST_GAMES_BREED_COUNT, len(sorted_sessions) - 1)])

                for session in best_games:
                    first_parent_index = randint(0, len(best_games) - 1)
                    second_parent_index = randint(0, len(best_games) - 1)

                    best = max(best, session.getScore())
                    sum += session.getScore()

                    first_parent = best_games[first_parent_index]
                    second_parent = best_games[second_parent_index]

                    genome = GenotypeOperators.breed(first_parent.genotype, second_parent.genotype)
                    genome_after_mutation = GenotypeOperators.mutate(genome)

                    new_sessions.append(Session(genome_after_mutation))
                self._sessions = new_sessions

                print("Avg: {0}\tMax: {1}".format(sum/len(self._sessions), best))
            sleep(self._refreshInterval)

    def getBoardState(self, boardIndex):
        return self._sessions[boardIndex].getBoardState()

    def getSessionInfo(self, boardIndex):
        return self._sessions[boardIndex].getSessionInfo()

    def stop(self):
        self.running = False