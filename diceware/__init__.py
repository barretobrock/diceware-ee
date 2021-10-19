from .phrases import (
    clean_phrase,
    generate_phrase,
    read_raw_words,
    sample_and_gen
)
from . import _version
__version__ = _version.get_versions()['version']
