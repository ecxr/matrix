## Task 2
def dict2list(dct, keylist): return [dct[key] for key in dct.keys()]

def list2dict(L, keylist): return { keylist[k]:L[k] for k in range(len(keylist)) }


## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return list2dict(L, [i for i in range(len(L))])

