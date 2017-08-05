"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def testMinimax(self):
        print ('start to reload')
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        timeout=10
        self.time_left = 10
        self.TIMER_THRESHOLD = timeout
        self.game = isolation.Board(self.player1, self.player2)
        print ('run test')
        self.assertTrue(game_agent.MinimaxPlayer.get_move(self, self.game,self.time_left))
 #       self.assertTrue(game_agent.MinimaxPlayer.minimax(self, self.game, 3))


if __name__ == '__main__':
    unittest.main()
