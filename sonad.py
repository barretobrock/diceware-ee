#! /usr/bin/env python3
# coding=utf-8
import os
import argparse
from typing import List
from random import sample, choice, randint

# Defaults
WORD_LIST_FPATH = os.path.abspath('lemmad.txt')
WORD_CNT = 3


def clean_phrase(words: List[str], joiner: str = '-',
                 symbols: str = '!@#$%^&*=+', char_limit: int = None) -> str:
    """Cleans a returned phrase according to specifications"""
    map_to = '224466yYzZsS'
    map_from = 'äÄöÖõÕüÜžŽšŠ'

    new_words = []
    for word in words:
        # Randomly capitalize, add a number & a symbol
        # Random capitalization weights
        weights = [str.lower] * 9 + [str.upper] * 1
        # Apply random caps
        word = ''.join(choice(weights)(c) for c in word)
        # Apply random number & symbol
        word += ''.join([str(randint(0, 9)), choice(list(symbols))])
        if char_limit is not None:
            if len(f'{joiner}'.join(new_words + [word])) <= char_limit:
                new_words.append(word)
            else:
                break
        else:
            new_words.append(word)

    phrase = f'{joiner}'.join(new_words).translate(str.maketrans(map_from, map_to))
    return phrase


def sample_and_gen(word_list: List[str], num_words: int, joiner: str, symbols: str,
                   char_limit: int = None) -> str:
    """Sample words and generate phrase"""
    sampled_words = sample(word_list, num_words)
    phrase = clean_phrase(sampled_words, joiner=joiner, symbols=symbols, char_limit=char_limit)
    return phrase


def generate_phrase(word_list: List[str], n_phrases: int = 6, num_words: int = 6, char_limit: int = None,
                    n_attempts: int = 50, joiner: str = '-', symbols: str = '!@#$%^&*=+'):
    """Generates passphrases"""
    phrases = []
    if char_limit is not None:
        for n in range(n_attempts):
            if len(phrases) >= n_phrases:
                break
            phrase = sample_and_gen(word_list, num_words, joiner, symbols, char_limit)
            if len(phrase) <= char_limit:
                phrases.append(phrase)
    else:
        for n in range(n_phrases):
            phrases.append(sample_and_gen(word_list, num_words, joiner, symbols))

    print('\n'.join(phrases))


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='File containing lemmad', default=WORD_LIST_FPATH)
parser.add_argument('-w', '--words', help='Number of words', default=WORD_CNT)
parser.add_argument('-c', '--char', help='Character limit', default=None)
args = parser.parse_args()

fpath = args.file
n_words = int(args.words)
char_lim = int(args.char) if args.char is not None else None

# Read in words
with open(fpath, 'r') as f:
    lines = [x.strip() for x in f.readlines()]

dice_per_word = 5
dice_faces = 6
# Determine number of words to sample
if fpath == WORD_LIST_FPATH:
    total_words = dice_faces ** dice_per_word
    assert len(lines) >= total_words
    selected_words = sorted(sample(lines, total_words))
else:
    # Using smaller, custom word list
    selected_words = sorted(lines)


# Generate phrases and print
generate_phrase(word_list=selected_words, n_phrases=20, num_words=n_words,
                char_limit=char_lim, n_attempts=1000, joiner='_')
