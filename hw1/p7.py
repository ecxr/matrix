import itertools
from GF2 import one

def vecSumGF2(v):
    """
    input: GF2 vector v
    output: GF2 sum of all elements in v
    
    >>> vecSumGF2([one, 0, one, one])
    one
    >>> vecSumGF2([one, one, one, one])
    0
    """
    res = 0;
    for i in range(0, len(v)):
        if res == 0 and v[i] == one:
            res = one
        elif res == one and v[i] == one:
            res = 0
    return res

def vecDotProductGF2(v1, v2):
    """
    input: 2 GF2 vectors v1, v2
    output: dot-product of v1 and v2

    >>> vecDotProductGF2([0, one, 0, one, one], [one, 0, one, one, one])
    0
    >>> vecDotProductGF2([one, one, one, one, 0], [one, 0, one, one, 0])
    one
    """
    res = []
    for i in range(0, len(v1)):
        if v1[i] == one and v2[i] == one:
            res.append(one)
        else:
            res.append(0)
    return vecSumGF2(res)
        

a = [one, one, 0, 0]
b = [one, 0, one, 0]
c = [one, one, one, one]

#get the index of each of the elements of the above vectors
ind = [x for (x,y) in enumerate(a)] 

for L in range(0, len(a)+1):# first for loop
    for subset in itertools.combinations(ind, L):
        result = [0,0,0,0]
        for item in subset:
            result[item-1] = one #iterate to get different values of x
        # Now calculate the dot product of (a, result), (b, result), (c, result) 
        # and use an if loop to check if each of the dot products are equal to 1
        if vecDotProductGF2(result, a) == one and \
           vecDotProductGF2(result, b) == one and \
           vecDotProductGF2(result, c) == one:
            print(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("tests done!")
