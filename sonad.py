#! /usr/bin/env python3
# coding=utf-8
import os
import argparse
from random import sample
from diceware import generate_phrase

# Defaults
file_dir = os.path.dirname(__file__)
outpath = os.path.join(file_dir, 'output')
WORD_LIST_FPATH = os.path.join(file_dir, 'lemmad.txt')
N_PHRASES = 20
WORD_CNT = 3

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='sõnaloendi fail', default=WORD_LIST_FPATH)
parser.add_argument('-w', '--words', help='maksimum lubatud sõnad paroolis', default=WORD_CNT)
parser.add_argument('-p', '--phrases', help='mitu paroole tekitada', default=N_PHRASES)
parser.add_argument('-a', '--randcap', help='võimalda juhusliku suurtähtedega kirjutamine',
                    action='store_true', default=False)
parser.add_argument('-c', '--char', help='maksimum lubatud tähte paroolis', default=None)
args = parser.parse_args()

fpath = args.file
num_words = int(args.words)
num_phrases = int(args.phrases)
char_lim = int(args.char) if args.char is not None else None
rand_cap = args.randcap

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
phrases = generate_phrase(word_list=selected_words, n_phrases=num_phrases, n_words=num_words,
                          char_limit=char_lim, n_attempts=1000, joiner='_')

with open(outpath, 'w') as f:
    f.writelines(phrases)
print(f'New secrets written to {outpath}.')
