#Hyperdimensional Authorship Detection Program
#Written by Ellis (Andy) Weglewski
#Identifies the Author based on 3-word sequences and first letter 
#of line projected on to dim-dimension BSC hypervectors

#Libraries
import random
import numpy as np
import re
import string
from numpy.linalg import norm
from operator import *
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance

#####TEXT PRE-PROCESSING#####
#All text files are opened for reading and then the
#a substring of length profile_size is taken for encoding
#the profile vector. Another substring of length
#chunk_size is taken to call for identification.

profile_size = 10000
chunk_size = 10000

#Hornblower - C.S. Forester
forester = open(r"forester.txt", "r", encoding="utf8")
forester = forester.read()
forester = forester.strip()
forester = forester[:profile_size]
forester_chunk = forester[:chunk_size]

#Collection of Shakespeare works
shakespeare = open(r"shakespeare.txt", "r", encoding="utf8")
shakespeare = shakespeare.read()
shakespeare = shakespeare.strip()
shakespeare = shakespeare[:profile_size]
shakespeare_chunk = shakespeare[:chunk_size]

#Moby Dick - Herman Melville
melville = open(r"melville.txt", "r", encoding="utf8")
melville = melville.read()
melville = melville.strip()
melville = melville[:profile_size]
melville_chunk = melville[:chunk_size]

#The Silmarillion - J.R.R Tolkien
tolkien = open(r"tolkien.txt", "r", encoding="utf8")
tolkien = tolkien.read()
tolkien = tolkien.strip()
tolkien = tolkien[:profile_size]
tolkien_chunk = tolkien[:chunk_size]

#Maldoror - Comte de Lautreamont
lautreamont = open(r"lautreamont.txt", "r", encoding="utf8")
lautreamont = lautreamont.read()
lautreamont = lautreamont.strip()
lautreamont = lautreamont[:profile_size]
lautreamont_chunk = lautreamont[:chunk_size]

#Alice in Wonderland - Lewis Caroll
caroll = open(r"caroll.txt", "r", encoding="utf8")
caroll = caroll.read()
caroll = caroll.strip()
caroll = caroll[:profile_size]
caroll_chunk = caroll[:chunk_size]

#####BASIC VECTOR FUNCTIONS#####

#Orthogonal BSC Vector Generator
#Takes in a desired dimensionality and returns a MAP vector
def generator(dim):
    vector_o = []
    x = random.randint(1,2)
    i=0
    while i < dim and len(vector_o) <= dim:
        if x == 2:
            vector_o.append(1)
            x = random.randint(1,2)
            i+= 1
        else:
            vector_o.append(0)
            x = random.randint(1,2)
            i+= 1
    output = np.array(vector_o)
    return output


#Vector Bundler
#Takes in two vectors and performs thresholded component-wise addition
def bundle(vector_a, vector_b):
    vector_c = generator(dim)
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
        if vector_a[i] == vector_b[i]:
            vector_o.append(0)
            i+=1
        else:
            vector_o.append(1)
            i+=1
    vector_o = np.array(vector_o)
    return vector_o

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
    vector_o = np.array(vector_o)
    return vector_o



#####ENCODING BLOCK#####

#Define constant for vector size
dim = 10

#Generate a fixed permutation matrix
rho = permute_generator(dim)

#Assign atomic hypervectors to each character of
#the latin alphabet using the generator function
alpha    = {"a": generator(dim),
            "b": generator(dim),
            "c": generator(dim),
            "d": generator(dim),
            "e": generator(dim),
            "f": generator(dim),
            "g": generator(dim),
            "h": generator(dim),
            "i": generator(dim),
            "j": generator(dim),
            "k": generator(dim),
            "l": generator(dim),
            "m": generator(dim),
            "n": generator(dim),
            "o": generator(dim),
            "p": generator(dim),
            "q": generator(dim),
            "r": generator(dim),
            "s": generator(dim),
            "t": generator(dim),
            "u": generator(dim),
            "v": generator(dim),
            "w": generator(dim),
            "x": generator(dim),
            "y": generator(dim),
            "z": generator(dim),
            "A": generator(dim),
            "B": generator(dim),
            "C": generator(dim),
            "D": generator(dim),
            "E": generator(dim),
            "F": generator(dim),
            "G": generator(dim),
            "H": generator(dim),
            "I": generator(dim),
            "J": generator(dim),
            "K": generator(dim),
            "L": generator(dim),
            "M": generator(dim),
            "N": generator(dim),
            "O": generator(dim),
            "P": generator(dim),
            "Q": generator(dim),
            "R": generator(dim),
            "S": generator(dim),
            "T": generator(dim),
            "U": generator(dim),
            "V": generator(dim),
            "W": generator(dim),
            "X": generator(dim),
            "Y": generator(dim),
            "Z": generator(dim),
            "è": generator(dim),
            "œ": generator(dim),
            "_": generator(dim),
            "1": generator(dim),
            "2": generator(dim),
            "3": generator(dim),
            "4": generator(dim),
            "5": generator(dim),
            "6": generator(dim),
            "7": generator(dim),
            "8": generator(dim),
            "9": generator(dim),
            "0": generator(dim),
            "Ë": generator(dim),
            "ë": generator(dim),
            "é": generator(dim),
            "â": generator(dim),
            "ñ": generator(dim),
            "ô": generator(dim),
            "ù": generator(dim),
            " ": generator(dim),
            "!": generator(dim),
            '"': generator(dim),
            "#": generator(dim),
            "$": generator(dim),
            "%": generator(dim),
            "&": generator(dim),
            "'": generator(dim),
            "(": generator(dim),
            ")": generator(dim),
            "*": generator(dim),
            "+": generator(dim),
            ",": generator(dim),
            "-": generator(dim),
            ".": generator(dim),
            "/": generator(dim),
            ":": generator(dim),
            ";": generator(dim),
            "<": generator(dim),
            "=": generator(dim),
            ">": generator(dim),
            "?": generator(dim),
            "@": generator(dim),
            "[": generator(dim),
            "]": generator(dim),
            "^": generator(dim),
            "_": generator(dim),
            "`": generator(dim),
            "{": generator(dim),
            "}": generator(dim),
            "|": generator(dim),
            "~": generator(dim),
            "—": generator(dim),
            "‘": generator(dim),
            "’": generator(dim),
            "“": generator(dim),
            "”": generator(dim),
            "æ": generator(dim),
            "£": generator(dim),
            "ç": generator(dim),
            "\n": generator(dim),
            "\\": generator(dim),
            "\ufeff": generator(dim)
            }

#Initialize standard latin alphabet
#As a string for utilities in main
alpha_latin = list(string.ascii_lowercase)
#alpha_latin = alpha_latin.extend(['1','2','3','4','5','6','7','8','9'])

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
            vector_o = bind(vector_o, permute(alpha[chars[i]], rho, i))
            print(word)
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

#Word Sequence Encoder
#Takes in a word vector sequence and generates a n-gram vector
def encode_sequence(words):
    i = 0
    vector_o = []
    while i < len(words):
        if i == 0:
            vector_o = bind(words[0], permute(words[1], rho, 1))
            print(vector_o)
            i += 2
        else: 
            vector_o = bind(vector_o, permute(words[i], rho, i))
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

#Author Encoder
#Takes in an array of three letter sequence profile vectors and generates
#an author profile vector
def encode_author(word_vectors):
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
    vector_o = np.array(vector_o)
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
    i = 0
    while i < len(prepared_text):
        word_vectors.append(encode_word(prepared_text[i]))
        i += 1
    i = 0
    while i < len(word_vectors) - 3:
        ngram_vectors.append(encode_sequence([word_vectors[i], word_vectors[i+1], 
                                              word_vectors[i+2]]))
        i += 1
    i = 0
    vector_o = encode_author(ngram_vectors)
    vector_o = np.array(vector_o)
    return vector_o


###ENCODE AUTHORS####

#Run each profile_size char author var through
#The encoding function
a1 = encode(forester)
a2 = encode(shakespeare)
a3 = encode(melville)
a4 = encode(tolkien)
a5 = encode(lautreamont)
a6 = encode(caroll)

#Pass encoded vectors into an array
author_vectors = [a1, a2, a3, a4, a5, a6]

#Create an array of author names corresponding to their
#Vector position in the author_vectors array
author_names = ["forester", "shakespeare", "melville", "tolkien", "lautreamont", "caroll"]

author_chunks = [forester_chunk, shakespeare_chunk, melville_chunk, tolkien_chunk, lautreamont_chunk, caroll_chunk]

#Identifier
#Takes in profile vectors and finds the closest match via cosine similarity
def identify(text):
    i = 0
    j = 0
    input_text = encode(text)
    hamming_distances = []
    while j < len(author_vectors):
#        a = np.dot(input_text, author_vectors[i])/(norm(input_text)*norm(author_vectors[i]))
#        b = np.dot(input_text, author_vectors[j])/(norm(input_text)*norm(author_vectors[j])
        a = distance.hamming(input_text, author_vectors[i])
        b = distance.hamming(input_text, author_vectors[j])
        if a > b:
            hamming_distances.append(str(b) + ' ' + author_names[j])
            i = j
            j += 1
        else:
            hamming_distances.append(str(b) + ' ' + author_names[j])
            j += 1
    identity = author_names[i]
    return hamming_distances

#Mode_Identifier
#Takes in a profile vector, runs identify on it 10 times
#and returns the most frequent author in the set.
def mode_identify(text):
    i = 0
    j = []
    k = 0
    while i <= 10:
        j.append(identify(text))
        i += 1
    iden = max(set(j), key=j.count)
    i = 0
    while i < len(j):
        if j[i] == iden:
            k += 1
        else:
            i += 1
    print(i/10)

def main():
    i = 0
    j = 0
    #Writes hamming distance between author chunk and author profile vectors to a file
    #Called hamming.txt
    hamming = open(r"hamming.txt", "w", encoding = "utf8")
    for i in author_chunks:
        to_write = identify(i)
        hamming.write('hamming distance between ' + (author_names[j]) + ' chunk and author profile vectors: \n')
        hamming.write('\n'.join(to_write) + '\n')
        j += 1
    j = 9
    #Replaces every 10th character in a chunk with a random letter
    #which has the effect of "diluting" the chunk
    #for i in author_chunks:
    #    workable_chunk = list(i)
    #    print(workable_chunk)
    #    while j < chunk_size:
    #        rand = random.randint(0,25)
    #        workable_chunk[j] = alpha_latin[rand]
    #        j += 10
    j = 0
    #Writes hamming distance between diluted author chunk and author profile vectors
    #to a file called hamming_diluted.txt
    #hamming_diluted = open(r"hamming_diluted.txt", "w", encoding = "utf8")
    #for i in author_chunks:
    #    to_write = identify(i)
    #    hamming_diluted.write('hamming distance between diluted ' + (author_names[j]) + ' chunk and author profile vectors: \n')
    #    hamming_diluted.write('\n'.join(to_write) + '\n')
    #    j += 1
    #j = 0
    #Removes letters from author chunk
    for i in author_chunks:
        workable_chunk = list(i)
        print(workable_chunk)
        while j < len(workable_chunk):
            if alpha_latin.count(workable_chunk[j]) > 0:
                workable_chunk = workable_chunk.pop(j)
                j += 1
            else:
                j += 1
        i = workable_chunk
    j = 0
    #Writes hamming distance between diluted author chunk and author profile vectors
    #to a file called hamming_diluted.txt
    hamming_punc = open(r"hamming_punc.txt", "w", encoding = "utf8")
    for i in author_chunks:
        to_write = identify(i)
        hamming_punc.write('hamming distance between punc only ' + (author_names[j]) + ' chunk and author profile vectors: \n')
        hamming_punc.write('\n'.join(to_write) + '\n')
        j += 1
    j = 0

if __name__ == "__main__":
    main()
