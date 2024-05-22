#Hyperdimensional Authorship Detection Program
#Written by Ellis Weglewski
#Identifies the Author based on 3-word sequences projected on to 10000 dimensional MAP hypervectors


#Libraries
import random
import fileinput
import numpy as np
from numpy.linalg import norm
from operator import *

#Import Texts for Analysis
davinci = 'davinci.txt'
shakespeare = 'romeo.txt'

#Orthogonal MAP Vector Generator
#Takes in a desired dimensionality and returns a MAP vector
def generator(dim):
    vector = []
    x = random.randint(1,2)
    i=0
    while i < dim and len(vector) <= dim:
        if x == 2:
            vector.append(1)
            x = random.randint(1,2)
            i+= 1
        else:
            vector.append(-1)
            x = random.randint(1,2)
            i+= 1
    output = np.array(vector)
    return output

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alphabet = {"a": generator(10000),
            "b": generator(10000),
            "c": generator(10000),
            "d": generator(10000),
            "e": generator(10000),
            "f": generator(10000),
            "g": generator(10000),
            "h": generator(10000),
            "h": generator(10000),
            "i": generator(10000),
            "j": generator(10000),
            "k": generator(10000),
            "l": generator(10000),
            "m": generator(10000),
            "n": generator(10000),
            "o": generator(10000),
            "p": generator(10000),
            "q": generator(10000),
            "r": generator(10000),
            "s": generator(10000),
            "t": generator(10000),
            "u": generator(10000),
            "v": generator(10000),
            "w": generator(10000),
            "x": generator(10000),
            "y": generator(10000),
            "z": generator(10000)}

#Vector Bundler
#Takes in two vectors and performs thresholded component-wise addition
def bundle(vector_a, vector_b):
    vector_c = generator(10000)
    vector_o = []
    i=0
    while i < len(vector_a) and i < len(vector_b):
        if vector_a[i] == vector_b[i]:
            vector_o.append(vector_a[i])
            i+=1
        else:
            vector_o.append(vector_c[i])
            i+=1
    output = np.array(vector_o)
    print(countOf(output, 1))
    print(output)
    return output

#Vector Binder
#Takes in two vectors and performs component-wise multiplication
def bind(vector_a, vector_b):
    vector_o = []
    i=0
    j=0
    while i < len(vector_a) and i < len(vector_b):
        j = vector_a[i] * vector_b[i]
        vector_o.append(j)
        i+=1
    output = np.array(vector_o)
    print(output)
    return output

#Permutation Matrix Declaration
#Takes in n returns a permutation matrix of size nxn
def permute_generator(n):
    rho = np.eye(n)
    np.random.shuffle(rho)
    print(rho)
    return rho


#Vector Permuter
#Takes in a vector and a permutation matrix, then mutiplies the vector by the permutation matrix
def permute(vector, rho):
    vector_p = np.matmul(vector, rho)
    return vector_p


def main():
    inp = input()
    x = generator(int(inp))
    y = generator(int(inp))
    print(x)
    rho = permute_generator(int(inp))
    print(permute(x, rho))


if __name__ == "__main__":
    main()
