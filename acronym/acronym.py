
from itertools import groupby
def abbreviate(words):
    words = words.replace("'", "")
    words = words.upper()
    return ''.join(next(b) for a, b in groupby(words, str.isalpha) if a)