# Please fill out this stencil and submit using the provided submission script.

from GF2 import one

def addn(v, w):
    return [v[i] + w[i] for i in range(len(v))]

def subn(v, w):
    return [v[i] - w[i] for i in range(len(v))]

def scaler_vector_mult(alpha, v): 
    return [alpha*i for i in v]

def zero_vec(D): return Vec(D, {})
#def zero_vec(D): return Vec(D, {d:0 for d in D})

def getitem(v,d): return v.f[d] if d in v.f else 0

def list2vec(L):
    return Vec(set(range(len(L))), {k:x for k,x in enumerate(L)})

#def list2vec(L):
#    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def list_dot(u, v): return sum([u[i] * v[i] for i in range(len(u))])
#def list_dot(u, v): return sum([x*y for (x,y) in zip(u,v)])

## Problem 1
p1_v = [-1, 3]
p1_u = [ 0, 4]
p1_v_plus_u =  [-1, 7]
p1_v_minus_u = [-1, -1]
p1_three_v_minus_two_u = [ -3, 1 ]

## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [1, 0, 6]
p2_v_minus_u = [3, -2, 4]
p2_two_v_minus_u = [5, -3, 9]
p2_v_plus_two_u = [0, 1, 7]

## Problem 3
# Write your answer using GF2's one instead of the number 1
v = [0, 1, 1]
u = [1, 1, 1]
#v + u
p3_vector_sum_1 = [one, 0, 0]
#v + u + u
p3_vector_sum_2 = [0, one, one]

## Problem 4
# Please express your solution as a set of the letters corresponding 
# to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

u_0010010 = {'e', 'c', 'd'}
u_0100010 = {'b', 'c', 'd', 'e'}

## Problem 5
# Use the same format as the previous problem

v_0010010 = {'c', 'd'}
v_0100010 = set()

## Problem 6
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1

## Problem 7
# use 'one' instead of '1'
x_gf2 = [one, 0, 0, 0]
#x_gf2 = [0, one, one, one]

## Problem 8
v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

