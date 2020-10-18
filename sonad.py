#! /usr/bin/env python3
# coding=utf-8
import os
import argparse
from typing import List
from random import sample


def get_lemmad_filepath() -> str:
    """Returns the filepath of the desired list of lemmad to use."""
    # Default lemmad file path
    default_path = os.path.abspath('lemmad.txt')
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='File containing lemmad', default=default_path)
    args = parser.parse_known_args()

    for arg in args:
        if isinstance(arg, argparse.Namespace):
            arg_dict = vars(arg)
            if 'file' in arg_dict.keys():
                return arg_dict['file']
    return default_path


def clean_phrase(phrase: str) -> str:
    """Cleans a returned phrase according to specifications"""
    mapping = {
        'ä': '2',
        'ö': '4',
        'õ': '6',
        'ü': 'y',
        'ž': 'zh',
        'š': 'sh'
    }
    for char, rep in mapping.items():
        if char in phrase:
            phrase = phrase.replace(char, rep)
    return phrase


def generate_phrase(n_phrases: int = 6, n_words: int = 6, char_limit: int = None,
                    n_attempts: int = 50) -> List[str]:
    """Generates passphrase"""
    phrases = []
    if char_limit is not None:
        for n in range(n_attempts):
            if len(phrases) >= n_phrases:
                return phrases
            phrase = clean_phrase('-'.join(sample(selected_words, n_words)))
            if len(phrase) <= char_limit:
                phrases.append(phrase)
    else:
        for n in range(n_phrases):
            phrase = clean_phrase('-'.join(sample(selected_words, n_words)))
            phrases.append(phrase)
    return phrases


fpath = get_lemmad_filepath()
with open(fpath, 'r') as f:
    lines = [x.strip() for x in f.readlines()]

dice_per_word = 5
dice_faces = 6
# Determine number of words to sample
total_words = dice_faces ** dice_per_word
assert len(lines) >= total_words

selected_words = sorted(sample(lines, total_words))


generated = generate_phrase(n_phrases=6, n_words=3, char_limit=30, n_attempts=1000)
print('\n'.join(generated))
