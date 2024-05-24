#Hyperdimensional Authorship Detection Program
#Written by Ellis Weglewski
#Identifies the Author based on 3-word sequences and first letter of line projected on to 1000-dimension MAP hypervectors


#Libraries
import random
import numpy as np
import re
from numpy.linalg import norm
from operator import *

#####TEXT PRE-PROCESSING#####
frost = open(r"C:\Users\Andy\projects\python\robfrost.txt", "r", encoding="utf8")
rob = frost.read()
robfrost = re.sub('\W+',' ', rob )

frostt = open(r"C:\Users\Andy\projects\python\robfrost_half.txt", "r", encoding="utf8")
robb = frostt.read()
robfrostt = re.sub('\W+',' ', rob )

shake = open(r"C:\Users\Andy\projects\python\shakespeare.txt", "r", encoding="utf8")
speare = shake.read()
shakespeare = re.sub('\W+',' ', speare )

shakee = open(r"C:\Users\Andy\projects\python\shakespeare_half.txt", "r", encoding="utf8")
spearee = shakee.read()
shakespearee = re.sub('\W+',' ', spearee )

dicki = open(r"C:\Users\Andy\projects\python\dickinson.txt", "r", encoding="utf8")
nson = dicki.read()
dickinson = re.sub('\W+',' ', nson )

dickii = open(r"C:\Users\Andy\projects\python\dickinson_half.txt", "r", encoding="utf8")
nsonn = dickii.read()
dickinsonn = re.sub('\W+',' ', nsonn )

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
    vector_c = generator(1000)
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
rho = permute_generator(1000)

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alpha    = {"a": generator(1000),
            "b": generator(1000),
            "c": generator(1000),
            "d": generator(1000),
            "e": generator(1000),
            "f": generator(1000),
            "g": generator(1000),
            "h": generator(1000),
            "i": generator(1000),
            "j": generator(1000),
            "k": generator(1000),
            "l": generator(1000),
            "m": generator(1000),
            "n": generator(1000),
            "o": generator(1000),
            "p": generator(1000),
            "q": generator(1000),
            "r": generator(1000),
            "s": generator(1000),
            "t": generator(1000),
            "u": generator(1000),
            "v": generator(1000),
            "w": generator(1000),
            "x": generator(1000),
            "y": generator(1000),
            "z": generator(1000),
            "A": generator(1000),
            "B": generator(1000),
            "C": generator(1000),
            "D": generator(1000),
            "E": generator(1000),
            "F": generator(1000),
            "G": generator(1000),
            "H": generator(1000),
            "I": generator(1000),
            "J": generator(1000),
            "K": generator(1000),
            "L": generator(1000),
            "M": generator(1000),
            "N": generator(1000),
            "O": generator(1000),
            "P": generator(1000),
            "Q": generator(1000),
            "R": generator(1000),
            "S": generator(1000),
            "T": generator(1000),
            "U": generator(1000),
            "V": generator(1000),
            "W": generator(1000),
            "X": generator(1000),
            "Y": generator(1000),
            "Z": generator(1000),
            "è": generator(1000),
            "œ": generator(1000),
            "_": generator(1000),
            "1": generator(1000),
            "2": generator(1000),
            "3": generator(1000),
            "4": generator(1000),
            "5": generator(1000),
            "6": generator(1000),
            "7": generator(1000),
            "8": generator(1000),
            "9": generator(1000),
            "0": generator(1000),
            "Ë": generator(1000),
            "ë": generator(1000)}


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


#ENCODE AUTHORS#
a1 = encode(robfrost)
a2 = robfrostt
a3 = encode(shakespeare)
a4 = encode(dickinson)
a5 = dickinsonn
a6 = shakespearee

author_vectors = [a1, a3, a4]

author_names = ["robfrost", "shakespeare", "dickinson"]


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



if __name__ == "__main__":
    main() 
