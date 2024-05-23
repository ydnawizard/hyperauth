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

#####BASIC FUNCTIONS#####

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
    return output

#Permutation Matrix Declaration
#Takes in n returns a permutation matrix of size nxn
def permute_generator(n):
    rho = np.eye(n)
    np.random.shuffle(rho)
    return rho

#Vector Permuter
#Takes in a vector, a permutation matrix, and n, then mutiplies the vector by the permutation matrix n times
def permute(vector, rho, n):
    i = 1
    vector_o = vector
    while i <= n:
        vector_o = np.matmul(vector_o, rho)
        i += 1
    return vector_o

#Word Slicer
#Isolates text sequences between space chars

#####ENCODING BLOCK#####

#Generate a fixed permutation matrix
rho = permute_generator(10000)

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alpha    = {"a": generator(10000),
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


#Word Encoder
#Takes in a text sequence and generates a profile vector
def encode_word(word):
    i = 0
    chars = list(word)
    vector_o = []
    while i < len(word):
        if i == 0:
            vector_o = bind(alpha[chars[0]], permute(alpha[chars[1]], rho, 1))
            i += 2
        else:
            vector_o = bind(vector_o, permute(alpha[chars[i]], rho, 1))
            i += 1
    return vector_o

#Word Sequence Encoder
#Takes in a word vector sequence and generates a n-gram vector
def encode_sequence(words):
    i = 0
    vector_o = []
    while i < len(words):
        if i == 0:
            vector_o = bundle(words[0], permute(words[1], rho, 1))
            i += 2
        else: 
            vector_o = bundle(vector_o, permute(words[i], rho, 1))
            i += 1
    return vector_o

#Author Encoder
#Takes in an array of three letter sequence profile vectors and generates
#an author profile vector
def encode_author(ngrams):
    i = 0
    vector_o = []
    while i < len(ngrams):
        if i == 0:
            vector_o = bundle(ngrams[0], permute(ngrams[1], rho, 1))
            i += 2
        else:
            vector_o = bundle(vector_o, permute(ngrams[i], rho, 1))
            i += 1
    return vector_o


def main():
    inp = input()
    x = generator(int(inp))
    y = generator(int(inp))
    print(x)
    a = encode_word("hello")
    b = encode_word("asdfasd")
    c = encode_word("lodestar")
    abc = encode_sequence([a,b,c])
    acb = encode_sequence([a,c,b])
    cba = encode_sequence([c,b,a])
    print(np.dot(abc, acb)/(norm(abc)*norm(acb)))
    print(np.dot(abc, cba)/(norm(abc)*norm(cba)))
    a1 = encode_author([abc, acb])
    a2 = encode_author([abc, cba])
    print(np.dot(a1, a2)/(norm(a1)*norm(a2)))



if __name__ == "__main__":
    main()
