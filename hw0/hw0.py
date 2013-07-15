# Please fill out this stencil and submit using the provided submission script.

## Problem 1
def myFilter(L, num):
    """
    input:  list of numbers and a number.
    output: list of numbers not containing a multiple of num.

    >>> myFilter([1,2,4,5,7], 2)
    [1, 5, 7]
    """
    return [ x for x in L if x % num != 0 ]


## Problem 2
def myLists(L):
    """
    input:  list L of non-negative integers.
    output: output: a list of lists: for every element x in L create a 
            list containing 1; 2; : : : ; x.

    >>> myLists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    """
    return [ [x for x in range(1, y+1)] for y in L ]

## Problem 3
def myFunctionComposition(f, g): 
    """
    input: two functions f and g, represented as dictionaries, such that g o f 
           exists.
    output: dictionary that represents a function g o f

    >>> g = {'a':'apple', 'b':'banana'}
    >>> f = {0:'a', 1:'b'}
    >>> myFunctionComposition(f,g)
    {0: 'apple', 1: 'banana'}
    """
    return { k : g[f[k]] for k in f.keys() }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)

## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    """
    Input: list of numbers
    Output: sum of numbers in the list
    >>> mySum([])
    0
    >>> mySum([1,2,3])
    6
    """
    current = 0
    for x in L:
        current += x
    return current

## Problem 7
def myProduct(L):
    """
    Input: list of numbers
    Output: product of numbers in the list
    
    >>> myProduct([])
    1
    >>> myProduct([2,4,4])
    32
    """
    current = 1
    for x in L:
        current = current * x
    return current

## Problem 8
def myMin(L):
    """
    Input: list of numbers
    Output: minimum number in the list

    >>> myMin([2, -1, 4])
    -1
    """
    current = float('Inf')
    for x in L:
        if (x < current):
            current = x
    return current

## Problem 9
def myConcat(L):
    """
    Input: list of strings
    Output: concatenation of all the strings in L

    >>> myConcat(["foo", "bar", "baz"])
    'foobarbaz'
    """
    current = ''
    for x in L:
        current += x
    return current

## Problem 10
def myUnion(L): 
    """
    Input: list of sets
    Output: the union of all sets in L

    >>> myUnion([{1,2},{3,4},{5,6}])
    {1, 2, 3, 4, 5, 6}
    """
    current = set()
    for x in L:
        current |= x
    return current

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Tests done")
