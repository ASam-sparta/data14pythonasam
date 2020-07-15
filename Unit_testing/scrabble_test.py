from scrabble import ScrabbleGame
import unittest
# TEST DRIVEN DEVELOPMENT #

# Write unit tests first!!

# Class!

# Scrabble score calculator
# Return the score for a word according to Scrabble letter points
# Randomly generate 7 tile hand
    #user input

# Check that the word can be made using those tiles
# Once a word has been made, replace only the used tiles

class Scrabbletest(unittest.TestCase):
    game = ScrabbleGame()

# Returns true is the list is completely, false otherwise
    def _is_list_isalpha(self, list_to_check):
        all_alpha = True
        for letter in list_to_check:
            if not letter.isalpha:
                all_alpha = False
        return all_alpha

    def test_calculate_score(self):
        self.assertEqual(self.game.calculate_score("string"), 7)
        self.assertEqual(self.game.calculate_score("integer"), 8)
        self.assertEqual(self.game.calculate_score("oxyphenbutazone"), 41)
        self.assertEqual(self.game.calculate_score(""), None)

# It will return a list of 7 random letters from a pool, 7 letters that are alphabetical, also tests the pool size
    def test_generate_tile_hand(self):
        self.assertEqual(len(self.game.tile_hand(["A", "B", "C", "D", "E", "F"])), 7)
        self.assertEqual(len(self.game.tile_hand([])), 7)
        self.assertTrue(self._is_list_isalpha(self.game.tile_hand(["a", "b", "c", "d", "e"])))
        self.assertTrue(self._is_list_isalpha(self.game.tile_hand([])))

        scrabble = ScrabbleGame()
        pool_size = 98
        scrabble.tile_hand([])
        self.assertEqual(pool_size - 7, sum(scrabble.scrabble_pool.values()))
        pool_size = sum(scrabble.scrabble_pool.values())
        scrabble.tile_hand(["a", "b", "c", "d", "e"])
        self.assertEqual(pool_size - 2, sum(scrabble.scrabble_pool.values()))

        scrabble2 = ScrabbleGame()
        scrabble2.scrabble_pool = {"A": 4}
        returned_hand = scrabble2.tile_hand([])
        self.assertEqual(len(returned_hand), 4)
        self.assertEqual(0, sum(scrabble2.scrabble_pool.values()))

    def test_is_valid_word(self):
        self.assertTrue(self.game.is_valid_word("animal", ["test", "case", "does", "it", "work", "animal"]))
        self.assertFalse(self.game.is_valid_word("animal", ["test", "case", "does", "it", "work"]))
        self.assertFalse(self.game.is_valid_word("animal", [1, 2, 3, 4, 5]))
        self.assertIsNone(self.game.is_valid_word("animal", []))


    def test_shuffle_hand(self):
        self.assertTrue(self.game.shuffle_hand(["A", "B", "C", "D", "E", "F", "G"]))


