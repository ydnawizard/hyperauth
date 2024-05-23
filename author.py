#Hyperdimensional Authorship Detection Program
#Written by Ellis Weglewski
#Identifies the Author based on 3-word sequences projected on to 300 dimensional MAP hypervectors


#Libraries
import random
import string
import numpy as np
import re
from numpy.linalg import norm
from operator import *

#####TEXT PRE-PROCESSING#####
frost = open(r"C:\Users\Andy\projects\python\robfrost.txt", "r", encoding="utf8")
rob = frost.read()
robfrost = re.sub('\W+',' ', rob )

frostt = open(r"C:\Users\Andy\projects\python\robfrost_half.txt", "r", encoding="utf8")
robb = frost.read()
robfrostt = re.sub('\W+',' ', rob )

shake = open(r"C:\Users\Andy\projects\python\shakespeare.txt", "r", encoding="utf8")
speare = shake.read()
shakespeare = re.sub('\W+',' ', speare )

#####BASIC VECTOR FUNCTIONS#####

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
    vector_c = generator(300)
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

#Permutation Matrix generator
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

#####ENCODING BLOCK#####

#Generate a fixed permutation matrix
rho = permute_generator(300)

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alpha    = {"a": generator(300),
            "b": generator(300),
            "c": generator(300),
            "d": generator(300),
            "e": generator(300),
            "f": generator(300),
            "g": generator(300),
            "h": generator(300),
            "i": generator(300),
            "j": generator(300),
            "k": generator(300),
            "l": generator(300),
            "m": generator(300),
            "n": generator(300),
            "o": generator(300),
            "p": generator(300),
            "q": generator(300),
            "r": generator(300),
            "s": generator(300),
            "t": generator(300),
            "u": generator(300),
            "v": generator(300),
            "w": generator(300),
            "x": generator(300),
            "y": generator(300),
            "z": generator(300),
            "A": generator(300),
            "B": generator(300),
            "C": generator(300),
            "D": generator(300),
            "E": generator(300),
            "F": generator(300),
            "G": generator(300),
            "H": generator(300),
            "I": generator(300),
            "J": generator(300),
            "K": generator(300),
            "L": generator(300),
            "M": generator(300),
            "N": generator(300),
            "O": generator(300),
            "P": generator(300),
            "Q": generator(300),
            "R": generator(300),
            "S": generator(300),
            "T": generator(300),
            "U": generator(300),
            "V": generator(300),
            "W": generator(300),
            "X": generator(300),
            "Y": generator(300),
            "Z": generator(300),
            "è": generator(300),
            "œ": generator(300),
            "_": generator(300),
            "1": generator(300),
            "2": generator(300),
            "3": generator(300),
            "4": generator(300),
            "5": generator(300),
            "6": generator(300),
            "7": generator(300),
            "8": generator(300),
            "9": generator(300),
            "0": generator(300),}


#Word Encoder
#Takes in a text sequence and generates a profile vector
def encode_word(word):
    i = 0
    j = 0
    chars = list(word)
    vector_o = []
    while i < len(word):
        if i == 0:
            if len(word) == 1:
                vector_o = alpha[chars[0]]
                print(word)
                i += 1
            else:
                vector_o = bind(alpha[chars[0]], permute(alpha[chars[1]], rho, 1))
                print(word)
                i += 2
        else:
            vector_o = bind(vector_o, permute(alpha[chars[i]], rho, 1))
            print(word)
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
            print(vector_o)
            i += 2
        else: 
            vector_o = bundle(vector_o, permute(words[i], rho, 1))
            print("i")
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
            print(vector_o)
            i += 2
        else:
            vector_o = bundle(vector_o, permute(ngrams[i], rho, 1))
            print(i)
            i += 1
    return vector_o

#Main Encoder
#Takes in text, n, and d, and outputs a d-dimensional author profile vector composed n-grams
def encode(text):
    i = 0
    prepared_text = text.split()
    print(prepared_text)
    word_vectors = []
    ngram_vectors = []
    vector_o = []
    while i < len(prepared_text):
        word_vectors.append(encode_word(prepared_text[i]))
        i += 1
    i = 0
    while i < len(word_vectors):
        if len(word_vectors) % 2 == 0:
            ngram_vectors.append(encode_sequence([word_vectors[i], word_vectors[i+1], 
                                                  word_vectors[i+2], word_vectors[i+3]]))
            i += 4
        else:
            ngram_vectors.append(encode_sequence([word_vectors[i], word_vectors[i+1],
                                                  word_vectors[i+2]]))
            i += 3
    vector_o = encode_author(ngram_vectors)
    return vector_o



def main():
    #inp = input()
    #x = generator(int(inp))
    #y = generator(int(inp))
    #print(x)
    #a = encode_word("hello")
    #b = encode_word("asdfasd")
    #c = encode_word("lodestar")
    #abc = encode_sequence([a,b,c])
    #acb = encode_sequence([a,c,b])
    #cba = encode_sequence([c,b,a])
    #print(np.dot(abc, acb)/(norm(abc)*norm(acb)))
    #print(np.dot(abc, cba)/(norm(abc)*norm(cba)))
    #a1 = encode_author([abc, acb])
    #a2 = encode_author([abc, cba])
    #print(np.dot(a1, a2)/(norm(a1)*norm(a2)))

    a1 = encode(robfrost)
    a2 = encode(robfrostt)
    a3 = encode(shakespeare)
    print(np.dot(a1, a2)/(norm(a1)*norm(a2)))
    print(np.dot(a1, a3)/(norm(a1)*norm(a3)))



if __name__ == "__main__":
    main()
