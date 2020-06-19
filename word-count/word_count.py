
import unittest

def count_words(phrase):  
    counts = {}
    for word in ''.join(
            map(lambda c: c.lower() if c.isalnum() else ' ', phrase)).split():
        try:
            counts[word] = counts[word] + 1
        except KeyError:
            counts[word] = 1
    return counts