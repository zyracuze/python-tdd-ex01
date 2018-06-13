from unittest import TestCase

import game

class GameTest(TestCase) :

	def test_join(self) :
	    """Player may join a game og Pig"""

	    pig = game.Pig('Player A','Player B','Player C')
	    self.assertEqual(pig.get_players(), ('Player A','Player B','Player C'))
