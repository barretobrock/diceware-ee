import unittest
from diceware import (
    read_raw_words,
    generate_phrase,
    sample_and_gen,
    clean_phrase
)


class TestCleanPhrase(unittest.TestCase):

    def setUp(self) -> None:
        self.words = read_raw_words()

    def test_default(self):
        phrase = clean_phrase(words=self.words[:2])
        self.assertIsInstance(phrase, str)
        # Test with character limit
        phrase = clean_phrase(words=self.words[4:8], char_limit=12)
        self.assertTrue(len(phrase) <= 12)

    def test_with_randcap(self):
        phrase = clean_phrase(words=self.words[:2], random_cap=True)
        self.assertIsInstance(phrase, str)
        self.assertNotEqual('Aids', phrase[:4])
        # Test with character limit
        phrase = clean_phrase(words=self.words[4:8], char_limit=12, random_cap=True)
        self.assertTrue(len(phrase) <= 12)


class TestSampleAndGen(unittest.TestCase):
    def setUp(self) -> None:
        self.words = read_raw_words()

    def test_sample_and_gen(self):
        result = sample_and_gen(word_list=self.words, n_words=30)
        self.assertEqual(30, len(result.split('-')))


class TestGeneratePhrases(unittest.TestCase):
    def setUp(self) -> None:
        self.words = read_raw_words()

    def test_gen_phrases(self):
        result = generate_phrase(word_list=self.words, n_phrases=10, n_words=5)
        self.assertEqual(10, len(result))
        # Test with character limit
        result = generate_phrase(word_list=self.words, n_phrases=10, n_words=5, char_limit=12)
        self.assertEqual(10, len(result))


if __name__ == '__main__':
    unittest.main()
