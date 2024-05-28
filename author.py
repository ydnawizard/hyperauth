#Hyperdimensional Authorship Detection Program
#Written by Ellis Weglewski
#Identifies the Author based on 3-word sequences and first letter of line projected on to 300-dimension MAP hypervectors


#Libraries
import random
import numpy as np
import re
from numpy.linalg import norm
from operator import *

#####TEXT PRE-PROCESSING#####
frost = open("robfrost.txt", "r", encoding="utf8")
rob = frost.read()
robfrost = re.sub('\W+',' ', rob )

frostt = open("robfrost_half.txt", "r", encoding="utf8")
robb = frostt.read()
robfrostt = re.sub('\W+',' ', rob )

shake = open(r"shakespeare.txt", "r", encoding="utf8")
speare = shake.read()
shakespeare = re.sub('\W+',' ', speare )

shakee = open(r"shakespeare_half.txt", "r", encoding="utf8")
spearee = shakee.read()
shakespearee = re.sub('\W+',' ', spearee )

dicki = open(r"dickinson.txt", "r", encoding="utf8")
nson = dicki.read()
dickinson = re.sub('\W+',' ', nson )

dickii = open(r"dickinson_half.txt", "r", encoding="utf8")
nsonn = dickii.read()
dickinsonn = re.sub('\W+',' ', nsonn )

tolk = open("tolkien.txt", "r", encoding="utf8")
ien = tolk.read()
tolkien = re.sub('\W+',' ', ien )

lautr = open("lautreamont.txt", "r", encoding="utf8")
eamont = lautr.read()
lautreamont = re.sub('\W+',' ', eamont )

lautrr = open("lautreamont_part.txt", "r", encoding="utf8")
eamontt = lautrr.read()
lautreamontt = re.sub('\W+',' ', eamontt )

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
            "0": generator(300),
            "Ë": generator(300),
            "ë": generator(300),
            "é": generator(300),
            "â": generator(300),
            "ñ": generator(300),
            "ô": generator(300),
            }


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
            i += 1
    return vector_o

#Author Encoder
#Takes in an array of three letter sequence profile vectors and generates
#an author profile vector
def encode_author1(ngrams):
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

def encode_author2(word_vectors):
    i = 0
    vector_o = []
    while i < len(word_vectors):
        if i == 0:
            vector_o = bundle(word_vectors[0], word_vectors[1])
            print(vector_o)
            i += 2
        else:
            vector_o = bundle(vector_o, word_vectors[i])
            print(vector_o)
            i += 1
    return vector_o

#Main Encoder
#Takes in text and outputs an author profile vector composed n-grams
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
    while i < len(word_vectors) - 2:
        ngram_vectors.append(encode_sequence([word_vectors[i], word_vectors[i+1],
                                              word_vectors[i+2]]))
        i += 1
    vector_o = encode_author2(ngram_vectors)
    return vector_o


#ENCODE AUTHORS#
a1 = encode(robfrost)
a2 = robfrostt
a3 = encode(shakespeare)
a4 = encode(dickinson)
a5 = dickinsonn
a6 = shakespearee
a7 = encode(tolkien)
a8 = encode(lautreamont)
a9 = lautreamontt

author_vectors = [a1, a3, a4, a7, a8]

author_names = ["robfrost", "shakespeare", "dickinson", "tolkien"]


#Identifier
#Takes in profile vectors and finds the closest match via cosine similarity
def identify(text):
    i = 1
    j = 0
    input_text = encode(text)
    identity = author_vectors[0]
    while i < len(author_vectors):
        if np.dot(input_text, identity)/(norm(input_text)*norm(identity)) < np.dot(input_text, author_vectors[i])/(norm(input_text)*norm(author_vectors[i])):
            identity = author_vectors[i]
            i += 1
            j = i
            print(j)
        else: 
            print(np.dot(input_text, identity)/(norm(input_text)*norm(identity)))
            print(np.dot(input_text, author_vectors[i])/(norm(input_text)*norm(author_vectors[i])))
            print(j)
            i += 1

#Namer
#Identity function returns a vector so a fucntion is need to translate the vector into a name
def namer(identity):
   i = 0
   while i < len(author_vectors):
       if np.dot(identity, author_vectors[i])/(norm(identity)*norm(author_vectors[i])) == 1:
           name = author_names[i]
           print(name)
           return name
       else:
           i += 1
        

def main():
    print("Enter text to identify author: \n")
    i = 0
    while i < 1:
        inp = input()
        if inp == "":
            break
        if inp == "1":
            identify(a2)
        if inp == "2":
            identify(a6)
        if inp == "3":
            identify(a5)
        if inp == "4":
            identify(a9)
        else:
            identify(inp)



if __name__ == "__main__":
    main() 
