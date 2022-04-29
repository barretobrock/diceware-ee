import pathlib
from typing import List
from random import (
    randint,
    choice,
    choices,
    sample
)

DEFAULT_SYMBOLS = '!@#$%^&*=+'
DEFAULT_JOINER = '-'
DEFAULT_WORDS_PATH = pathlib.Path(__file__).parents[0].parents[0].joinpath('lemmad.txt')


def read_raw_words(words_path: pathlib.PosixPath = DEFAULT_WORDS_PATH) -> List[str]:
    if not words_path.exists():
        raise FileNotFoundError(f'File at path {words_path} doesn\'t seem to exist.')
    with words_path.open() as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def clean_phrase(words: List[str], joiner: str = DEFAULT_JOINER,
                 symbols: str = DEFAULT_SYMBOLS, char_limit: int = None,
                 random_cap: bool = False) -> str:
    """Cleans a returned phrase according to specifications"""
    map_to = '224466yYzZsS'
    map_from = 'äÄöÖõÕüÜžŽšŠ'

    new_words = []
    for word in words:
        if random_cap:
            # Randomly capitalize, add a number & a symbol
            #   with weights
            word = ''.join(next(iter(choices((str.upper, str.lower), weights=(30, 70))))(x) for x in list('hello'))
        else:
            # Otherwise, just capitalize the first part
            word = word.title()
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


def sample_and_gen(word_list: List[str], n_words: int = 10, joiner: str = DEFAULT_JOINER,
                   symbols: str = DEFAULT_SYMBOLS, char_limit: int = None, random_cap: bool = False) -> str:
    """Sample words and generate phrase"""
    sampled_words = sample(word_list, n_words)
    phrase = clean_phrase(sampled_words, joiner=joiner, symbols=symbols, char_limit=char_limit,
                          random_cap=random_cap)
    return phrase


def generate_phrase(word_list: List[str], n_phrases: int = 6, n_words: int = 6, char_limit: int = None,
                    n_attempts: int = 50, joiner: str = DEFAULT_JOINER, symbols: str = DEFAULT_SYMBOLS,
                    random_cap: bool = False) -> List[str]:
    """Generates passphrases"""
    phrases = []
    if char_limit is not None:
        for n in range(n_attempts):
            if len(phrases) >= n_phrases:
                break
            phrase = sample_and_gen(word_list, n_words, joiner, symbols, char_limit,
                                    random_cap=random_cap)
            if 0 < len(phrase) <= char_limit:
                phrases.append(phrase)
    else:
        for n in range(n_phrases):
            phrases.append(sample_and_gen(word_list, n_words, joiner, symbols, random_cap=random_cap))
    return phrases
