#Hyperdimensional Authorship Detection Program
#Written by Ellis Weglewski
#Identifies the Author based on 3-word sequences and first letter of line projected on to 100-dimension MAP hypervectors


#Libraries
import random
import numpy as np
import re
from numpy.linalg import norm
from operator import *
from sklearn.metrics.pairwise import cosine_similarity

#####TEXT PRE-PROCESSING#####
frost = open(r"forester.txt", "r", encoding="utf8")
rob = frost.read()
robfrost = rob.strip()
robfrost = robfrost[:45000]
robfrostt = robfrost[:2500]
frost.close

shake = open(r"shakespeare.txt", "r", encoding="utf8")
speare = shake.read()
shakespeare = speare.strip()
shakespeare = shakespeare[:45000]
shakespearee = shakespeare[:2500]
shake.close()

mel = open(r"melville.txt", "r", encoding="utf8")
ville = mel.read()
melville = ville.strip()
melville = melville[:45000]
melvillee = melville[:2500]
mel.close()

tolk = open(r"tolkien.txt", "r", encoding="utf8")
ien = tolk.read()
tolkien = ien.strip()
tolkien = tolkien[:45000]
tolkienn = tolkien[:2500]
tolk.close()

lautr = open(r"lautreamont.txt", "r", encoding="utf8")
eamont = lautr.read()
lautreamont = eamont.strip()
lautreamont = lautreamont[:45000]
lautreamontt = lautreamont[:2500]
lautr.close()

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
    vector_c = generator(100)
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
rho = permute_generator(100)

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alpha    = {"a": generator(100),
            "b": generator(100),
            "c": generator(100),
            "d": generator(100),
            "e": generator(100),
            "f": generator(100),
            "g": generator(100),
            "h": generator(100),
            "i": generator(100),
            "j": generator(100),
            "k": generator(100),
            "l": generator(100),
            "m": generator(100),
            "n": generator(100),
            "o": generator(100),
            "p": generator(100),
            "q": generator(100),
            "r": generator(100),
            "s": generator(100),
            "t": generator(100),
            "u": generator(100),
            "v": generator(100),
            "w": generator(100),
            "x": generator(100),
            "y": generator(100),
            "z": generator(100),
            "A": generator(100),
            "B": generator(100),
            "C": generator(100),
            "D": generator(100),
            "E": generator(100),
            "F": generator(100),
            "G": generator(100),
            "H": generator(100),
            "I": generator(100),
            "J": generator(100),
            "K": generator(100),
            "L": generator(100),
            "M": generator(100),
            "N": generator(100),
            "O": generator(100),
            "P": generator(100),
            "Q": generator(100),
            "R": generator(100),
            "S": generator(100),
            "T": generator(100),
            "U": generator(100),
            "V": generator(100),
            "W": generator(100),
            "X": generator(100),
            "Y": generator(100),
            "Z": generator(100),
            "è": generator(100),
            "œ": generator(100),
            "_": generator(100),
            "1": generator(100),
            "2": generator(100),
            "3": generator(100),
            "4": generator(100),
            "5": generator(100),
            "6": generator(100),
            "7": generator(100),
            "8": generator(100),
            "9": generator(100),
            "0": generator(100),
            "Ë": generator(100),
            "ë": generator(100),
            "é": generator(100),
            "â": generator(100),
            "ñ": generator(100),
            "ô": generator(100),
            " ": generator(100),
            "!": generator(100),
            '"': generator(100),
            "#": generator(100),
            "$": generator(100),
            "%": generator(100),
            "&": generator(100),
            "'": generator(100),
            "(": generator(100),
            ")": generator(100),
            "*": generator(100),
            "+": generator(100),
            ",": generator(100),
            "-": generator(100),
            ".": generator(100),
            "/": generator(100),
            ":": generator(100),
            ";": generator(100),
            "<": generator(100),
            "=": generator(100),
            ">": generator(100),
            "?": generator(100),
            "@": generator(100),
            "[": generator(100),
            "]": generator(100),
            "^": generator(100),
            "_": generator(100),
            "`": generator(100),
            "{": generator(100),
            "}": generator(100),
            "|": generator(100),
            "~": generator(100),
            "—": generator(100),
            "‘": generator(100),
            "’": generator(100),
            "“": generator(100),
            "”": generator(100),
            "æ": generator(100),
            "£": generator(100),
            "ç": generator(100),
            "\n": generator(100),
            "\\": generator(100),
            "\ufeff": generator(100)
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
    i = 0
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
    i = 0
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
    i = 0
    return vector_o

def encode_author2(word_vectors):
    i = 0
    vector_o = []
    while i < len(word_vectors):
        if i == 0:
            vector_o = word_vectors[0]
            print(vector_o)
            i += 1
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
    #while i < len(text)-2:
    #    j = slice(i, i + 3)
    #    prepared_text.append(text[j])
    #    i += 1
    print(prepared_text)
    word_vectors = []
    ngram_vectors = []
    vector_o = []
    i = 0
    while i < len(prepared_text):
        word_vectors.append(encode_word(prepared_text[i]))
        i += 1
    i = 0
    while i < len(word_vectors) - 2:
        ngram_vectors.append(encode_sequence([word_vectors[i], word_vectors[i+1], 
                                              word_vectors[i+2]]))
        i += 1
    i = 0
    vector_o = encode_author2(ngram_vectors)
    return vector_o


#ENCODE AUTHORS#
a1 = encode(robfrost)
a2 = robfrostt
a3 = encode(shakespeare)
a4 = encode(melville)
a5 = melvillee
a6 = shakespearee
a5 = encode(tolkien)
a8 = encode(lautreamont)
a9 = lautreamontt
a10 = tolkienn

author_vectors = [a1, a3, a4, a5, a8]

author_names = ["forester", "shakespeare", "melville", "tolkien", "lautreamont"]


#Identifier
#Takes in profile vectors and finds the closest match via cosine similarity
def identify(text):
    i = 1
    j = 0
    input_text = encode(text)
    while (i < len(author_vectors)) and (j < len(author_vectors)):
        a = np.dot(input_text, author_vectors[j])/(norm(input_text)*norm(author_vectors[j])) 
        b = np.dot(input_text, author_vectors[i])/(norm(input_text)*norm(author_vectors[i]))
        print(a)
        print(b)
        if a < b:
            print("hi")
            j = i
            i += 1
            print(j)
        else:
            print("yo")
            i += 1
    print(j+1)
    return j


def double_identify(text):
    i = 0
    j = []
    while i <= 10:
        j.append(identify(text))
        i += 1
    i = max(set(j), key=j.count)
    print(author_names[i])

def main():
    print("Enter text to identify author: \n")
    i = 0
    print(a1)
    print(a8)
    while i < 1:
        inp = input()
        if inp == "":
            break
        if inp == "1":
            double_identify(a2)
        if inp == "2":
            double_identify(a6)
        if inp == "3":
            double_identify(a5)
        if inp == "4":
            double_identify(a10)
        if inp == "5":
            double_identify(a9)
        else:
            double_identify(inp)



if __name__ == "__main__":
    main() 
