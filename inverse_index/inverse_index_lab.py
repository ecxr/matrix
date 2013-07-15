from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    docs = list(enumerate(strlist))
    dict = {}
    for (pos, doc) in docs:
        words = doc.split()
        for word in words:
            if word not in dict:
                dict[word] = set()
            dict[word].add(pos)
    return dict

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words

    >>> orSearch({'d': {1}, 'b': {0, 2, 3}, 'c': {0, 1, 2, 3}, 'x': {3}, 'a': {0, 1, 2}}, ['a', 'b']
    >>> {0, 1, 2, 3}
    """

    out = set()
    for q in query:
        if q in inverseIndex:
            out = out.union(inverseIndex[q])
    return out

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    out = set()
    for word in query:
        if word in inverseIndex:
            if len(out) == 0:
                out = inverseIndex[word]
            else:
                out = out.intersection(inverseIndex[word])
    return out

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# f = open('stories_small.txt')
# stories = list(f)
# makeInverseIndex(stories)
