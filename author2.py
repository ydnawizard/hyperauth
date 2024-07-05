#Hyperdimensional Authorship Detection Program
#Written by Ellis (Andy) Weglewski
#Identifies the Author based on 3-word sequences and first letter 
#of line projected on to dim-dimension BSC hypervectors

#####LIBRARIES###############################################################################
import random
import numpy as np
import re
import string
from numpy.linalg import norm
from operator import *
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance

#####TEXT PRE-PROCESSING#####################################################################
#All text files are opened for reading and then the
#a substring of length profile_size is taken for encoding
#the profile vector.

profile_size = 10000

#Hornblower - C.S. Forester
forester = open(r"forester.txt", "r", encoding="utf8")
forester = forester.read()
forester = forester.strip()
forester = forester[:profile_size]

#Collection of Shakespeare works
shakespeare = open(r"shakespeare.txt", "r", encoding="utf8")
shakespeare = shakespeare.read()
shakespeare = shakespeare.strip()
shakespeare = shakespeare[:profile_size]

#Moby Dick - Herman Melville
melville = open(r"melville.txt", "r", encoding="utf8")
melville = melville.read()
melville = melville.strip()
melville = melville[:profile_size]

#The Silmarillion - J.R.R Tolkien
tolkien = open(r"tolkien.txt", "r", encoding="utf8")
tolkien = tolkien.read()
tolkien = tolkien.strip()
tolkien = tolkien[:profile_size]

#Maldoror - Comte de Lautreamont
lautreamont = open(r"lautreamont.txt", "r", encoding="utf8")
lautreamont = lautreamont.read()
lautreamont = lautreamont.strip()
lautreamont = lautreamont[:profile_size]

#Alice in Wonderland - Lewis Caroll
caroll = open(r"caroll.txt", "r", encoding="utf8")
caroll = caroll.read()
caroll = caroll.strip()
caroll = caroll[:profile_size]

#####ALPHABET################################################################################
#Initialize standard latin alphabet
#As a string for utilities in main
alpha_latin_lower = list(string.ascii_lowercase)
alpha_latin_upper = list(string.ascii_uppercase)
alpha_latin = alpha_latin_upper + alpha_latin_lower
punctuation = string.punctuation
#####BASIC VECTOR FUNCTIONS##################################################################

#GENERERATOR################################################
#Takes in a desired dimensionality and returns a BSC vector#
############################################################
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


#BUNDLE################################################################
#Takes in two vectors and performs thresholded component-wise addition#
#######################################################################
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

#BIND############################################################
#Takes in two vectors and performs component-wise XOR           #
#################################################################
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

#PERMUTE_GENERATOR###################################
#Takes in n returns a permutation matrix of size nxn#
#####################################################
def permute_generator(n):
    rho = np.eye(n)
    np.random.shuffle(rho)
    return rho

#PERMUTE#############################################################################
#Takes in a vector, a permutation matrix, and n, then mutiplies the vector by the permutatio##n matrix n times                                                                           #
#############################################################################################
def permute(vector, rho, n):
    i = 1
    vector_o = vector
    while i <= n:
        vector_o = np.matmul(vector_o, rho)
        i += 1
    vector_o = np.array(vector_o)
    return vector_o



#####ENCODING FUNCTIONS######################################################################

#Define constant for vector size
dim = 120

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
            "10": generator(dim),
            "11": generator(dim),
            "12": generator(dim),
            "13": generator(dim),
            "14": generator(dim),
            "15": generator(dim),
            "16": generator(dim),
            "17": generator(dim),
            "18": generator(dim),
            "19": generator(dim),
            "20": generator(dim),
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

#WORD ENCODER#############################################################
#Takes in a character vector sequence and generates a word profile vector#
##########################################################################
def encode_word(word):
    i = 0
    j = 0
    chars = list(word)
    vector_o = []
    while i < len(word):
        if i == 0:
            if len(word) == 1:
                vector_o = alpha[chars[0]]
                i += 1
            else:
                vector_o = bind(alpha[chars[0]], permute(alpha[chars[1]], rho, 1))
                i += 2
        else:
            vector_o = bind(vector_o, permute(alpha[chars[i]], rho, i))
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

#WORD SEQUENCE (N-GRAM) ENCODER########################################
#Takes in a word vector sequence and generates a n-gram profile vector#
#######################################################################
def encode_sequence(words):
    i = 0
    vector_o = []
    while i < len(words):
        if i == 0:
            vector_o = bind(words[0], permute(words[1], rho, 1))
            i += 2
        else: 
            vector_o = bind(vector_o, permute(words[i], rho, i))
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

#AUTHOR ENCODER###########################################################
#Takes in an array of three letter sequence profile vectors and generates#
#an author profile vector                                                #
##########################################################################
def encode_author(word_vectors):
    i = 0
    vector_o = []
    while i < len(word_vectors):
        if i == 0:
            vector_o = word_vectors[0]
            i += 1
        else:
            vector_o = bundle(vector_o, word_vectors[i])
            i += 1
    vector_o = np.array(vector_o)
    return vector_o

#MAIN ENCODER###########################################################
#Takes in text and outputs an author profile vector composed of n-grams#
########################################################################
def encode(text):
    i = 0
    prepared_text = text.split()
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


###ENCODE AUTHORS############################################################################

#Run each profile_size author text through
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

#IDENTIFIER#################################################################
#Takes in profile vectors and finds the closest match via hamming distance #
############################################################################
def identify(text):
    i = 0
    j = 0
    input_text = encode(text)
    hamming_distances = []
    while j < len(author_vectors):
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

#####MAIN####################################################################################
#Generates author "chunks" which are shorter substrings of the profile_size author
#text strings. The length of these chunks is defined by chunk_size and the comparisons
#are made at 9 different intervals of descending chunk sizes until chunk size reaches 5000
#characters. The different comparison methods are: unmodified hamming, replacing every tenth #character with a random character (diluted) hamming, removing all characters except punctuat#ion marks hamming, and removing all punctuation marks hamming.
#############################################################################################
def main():
    chunk_size = 10000
    forester_chunk = forester[:chunk_size]
    shakespeare_chunk = shakespeare[:chunk_size]
    melville_chunk = melville[:chunk_size]
    tolkien_chunk = tolkien[:chunk_size]
    lautreamont_chunk = lautreamont[:chunk_size]
    caroll_chunk = caroll[:chunk_size]
    author_chunks = [forester_chunk, shakespeare_chunk, melville_chunk, tolkien_chunk, lautreamont_chunk, caroll_chunk]
    translator = str.maketrans('','',string.punctuation)
    count_chunks = author_chunks
    j = 0
    for i in count_chunks:
        i = i.translate(translator)
        i = i.split(' ')
        count_chunks[j] = i
        j += 1
    j = 0
    l = 0
    for i in count_chunks:
        for k in i:
            i[j]= len(k)
            j += 1
        j = 0
        count_chunks[l] = str(i)
        l += 1
    l = 0
    counted_chunk = []
    counted_chunks = []
    for i in count_chunks:
        j = 0
        while j < 30:
            counted_chunk.append(str(i.count(str(j))) + ' length ' + str(j) + ' strings')
            j += 1
        counted_chunks.append(counted_chunk)
        counted_chunk = []
        l += 1
    j = 0
    l = 0
    counted_chunk = [0] * 30
    for i in count_chunks:
        while j < 30:
            counted_chunk[j] = i.count(str(j)) + counted_chunk[j]
            j += 1
        j = 0
    j = 0
    print(counted_chunk)
    frequencies = open(r"frequencies.txt", "w", encoding = "utf8")
    for i in counted_chunks:
        while j < 30:
            frequencies.write((author_names[l]) + ' ' + str(i[j]) + '\n')
            j += 1
        j = 0
        l += 1
    j = 0
    frequencies = open(r"frequencies.txt", "a", encoding = "utf8")
    for i in counted_chunk:
        frequencies.write('global freq of ' + str(j) + ' ' + str((counted_chunk[j])) + '\n')
        j += 1 


"""
    #INITIALIZE# 
    chunk_size = 10000
    while chunk_size >= 8000:
        j = 0
        #INITIALIZE CHUNKS#
        forester_chunk = forester[:chunk_size]
        shakespeare_chunk = shakespeare[:chunk_size]
        melville_chunk = melville[:chunk_size]
        tolkien_chunk = tolkien[:chunk_size]
        lautreamont_chunk = lautreamont[:chunk_size]
        caroll_chunk = caroll[:chunk_size]
        author_chunks = [forester_chunk, shakespeare_chunk, melville_chunk, tolkien_chunk, lautreamont_chunk, caroll_chunk]
        print('hamming')
        ###################################################################################
        #Writes hamming distance between author chunk and author profile vectors to a file#
        #Called hamming.txt.                                                              #
        ###################################################################################
        if chunk_size == 10000:
            hamming = open(r"hamming.txt", "w", encoding = "utf8")
        else:
            hamming = open(r"hamming.txt", "a", encoding = "utf8")
        for i in author_chunks:
            #PASS CHUNK TO IDENTIFY#
            to_write = identify(i)
            hamming.write('hamming distance between ' + (author_names[j]) + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
            hamming.write('\n'.join(to_write) + '\n')
            j += 1
        j = 9
        print('hamming_diluted')
        ###############################################################
        #Replaces every 10th character in a chunk with a random letter#
        #which has the effect of "diluting" the chunk                 #
        ###############################################################
        diluted_chunks = author_chunks
        for i in diluted_chunks:
            workable_chunk = list(i)
            while j < chunk_size:
                rand = random.randint(0,25)
                workable_chunk[j] = alpha_latin[rand]
                j += 10
        j = 0
        #################################################################################
        #Writes hamming distance between diluted author chunk and author profile vectors#
        #to a file called hamming_diluted.txt                                           #
        #################################################################################
        if chunk_size == 10000:
            hamming_diluted = open(r"hamming_diluted.txt", "w", encoding = "utf8")
        else:
            hamming_diluted = open(r"hamming_diluted.txt", "a", encoding = "utf8")
        for i in diluted_chunks:
            to_write = identify(i)
            hamming_diluted.write('hamming distance between diluted ' + (author_names[j]) + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
            hamming_diluted.write('\n'.join(to_write) + '\n')
            j += 1
        j = 0
        print('hamming_punct')
        ###################################
        #Removes letters from author chunk#
        #Making them (punc)tuation only   #
        ###################################
        punct_chunks = author_chunks
        for i in punct_chunks:
            workable_chunk = list(i)
            for j in alpha_latin:
                while workable_chunk.count(j) > 0:
                    workable_chunk.remove(j)
            i = workable_chunk
        j = 0
        #################################################################################
        #Writes hamming distance between diluted author chunk and author profile vectors#
        #to a file called hamming_diluted.txt                                           #
        #################################################################################
        if chunk_size == 10000:
            hamming_punct = open(r"hamming_punc.txt", "w", encoding = "utf8")
        else:
            hamming_punct = open(r"hamming_punc.txt", "a", encoding = "utf8")
        for i in punct_chunks:
            to_write = identify(i)
            hamming_punct.write('hamming distance between punc only ' + (author_names[j]) + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
            hamming_punct.write('\n'.join(to_write) + '\n')
            j += 1
            j = 0
        print('hamming_no_punct')
        ##################################################################
        #Writes hamming distance between author chunk with no punctuation#
        #and author profile vectors to a file called hamming_no_punc.txt #
        ##################################################################
        translator = str.maketrans('','',string.punctuation)
        no_punct_chunks = author_chunks
        for i in no_punct_chunks:
            i = i.translate(translator)
            i = i.split(' ')
        if chunk_size == 10000:
            hamming = open(r"hamming_no_punct.txt", "w", encoding = "utf8")
        else:
            hamming = open(r"hamming_no_punct.txt", "a", encoding = "utf8")
        for i in no_punct_chunks:
            to_write = identify(i)
            hamming.write('hamming distance between no punctuation ' + (author_names[j]) + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
            hamming.write('\n'.join(to_write) + '\n')
            j += 1
        j = 0
        print('wlength_hamming')
        wlength_chunks = author_chunks
        #######################################################
        #Splits chunks into word lengths and punctuation marks#
        #######################################################
        j = 0
        for i in wlength_chunks:
            i = re.split(r'(\W)', i)
            while i.count(' ') > 0:
                i.remove(' ')
            while i.count('') > 0:
                i.remove('')
            while i.count('\n') > 0:
                i.remove('\n')
            wlength_chunks[j] = i
            j += 1
        j = 0
        for i in wlength_chunks:
            jj = 0
            for k in i:
                if punctuation.find(k) == -1:
                    k = len(k)
                i[jj] = k
                jj += 1
            wlength_chunks[j] = str(i)
            j += 1
        j = 0
        if chunk_size == 10000:
            wlength_hamming = open(r"wlength_hamming.txt", "w", encoding = "utf8")
        else:
            wlength_hamming = open(r"wlength_hamming.txt", "a", encoding = "utf8")
        for i in author_chunks:
            #PASS CHUNK TO IDENTIFY#
            to_write = identify(i)
            wlength_hamming.write('hamming distance between wlength ' + (author_names[j]) + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
            wlength_hamming.write('\n'.join(to_write) + '\n')
            j += 1
        chunk_size = chunk_size - 200
        print(chunk_size)
"""


if __name__ == "__main__":
    main()
