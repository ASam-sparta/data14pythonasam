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

# It will return a list of 7 random letters from a pool, 7 letters that are alphabetical
    def test_generate_tile_hand(self):
        self.assertEqual(len(self.game.generate_tile_hand()), 7)
        self.assertTrue(self._is_list_isalpha(self.game.generate_tile_hand()))

    def test_is_valid_word(self):
        self.assertTrue(self.game.is_valid_word("animal", ["test", "case", "does", "it", "work", "animal"]))
        self.assertFalse(self.game.is_valid_word("animal", ["test", "case", "does", "it", "work"]))
        self.assertFalse(self.game.is_valid_word("animal", [1, 2, 3, 4, 5]))
        self.assertIsNone(self.game.is_valid_word("animal", []))

    def test_replace_tiles(self):
        replaced_tiles = self.game.replace_tiles(["a", "b", "c", "d", "e"])
        self.assertTrue(self._is_list_isalpha(replaced_tiles))
        self.assertTrue(self._is_list_isalpha(self.game.replace_tiles(["A", "B", "C", "D", "E", "F"])))
        self.assertTrue(self._is_list_isalpha(self.game.replace_tiles([])))
        self.assertEqual(len(self.game.replace_tiles(replaced_tiles)), 7)


# if word is in generate tile hand,
# if the word exists
# input : word to test
# input : list of words
# output : boolean


# once a word has been made, replace only the used tiles # care
# input = string (ASD____)
# output = (ASDHJKL)

