from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options) - 1)]

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
    d = {}
    for (i,s) in enumerate(strlist):
      words = s.split()
      for word in words:
        if word not in d:
          d[word] = {i}
        else:
          d[word].add(i)
    return d


def ii2(strlist):
  return {word:index for (index,line) in enumerate(strlist) for word in line.split()}


## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    result = set()
    for q in query:
      if q in inverseIndex:
        result |= inverseIndex[q]
    return result

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    result = set()
    for q in query:
      if q in inverseIndex:
        if result == set(): 
          result = inverseIndex[q].copy()
        else:
          result.intersection_update(inverseIndex[q])
          if result == set(): return set()
      else:
        return set()
    return result 
