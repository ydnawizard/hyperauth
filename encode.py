import numpy as np
from construct import bind 
from construct import bundle
from construct import permute

#encode_gram
#takes in a gram and exports a vector that represents it
def encode_gram(gram):
    from dictionary import alpha
    from dictionary import rho
    i = 0
    j = 0
    chars = gram
    vector_o = []
    while i < len(gram):
        if i == 0:
            if len(gram) == 1:
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

#encode_ngram
#takes in a sequence of grams and exports a vector representative of the sequence
def encode_ngram(sequence):
    from dictionary import rho
    i = 0
    vector_o = []
    while i < len(sequence):
        if i == 0:
            vector_o = bind(sequence[0], permute(sequence[1], rho, 1))
            i += 2
        else: 
            vector_o = bind(vector_o, permute(sequence[i], rho, i))
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

def encode_ngram_noperm(sequence):
    i = 0
    vector_o = []
    while i < len(sequence):
        if i == 0:
            vector_o = bind(sequence[0], sequence[1])
            i += 2
        else:
            vector_o = bind(vector_o, sequence[i])
            i += 1
    i = 0
    vector_o = np.array(vector_o)
    return vector_o

#encode_ngrams
#takes in a sequence of ngrams and exports a vector representative of the sequence
def encode_ngrams(ngrams):
    i = 0
    vector_o = []
    while i < len(ngrams):
        if i == 0:
            vector_o = ngrams[0]
            i += 1
        else:
            vector_o = bundle(vector_o, ngrams[i])
            i += 1
    vector_o = np.array(vector_o)
    return vector_o

#encode_text
def encode(text):
    i = 0
    prepared_text = text
    gram_vectors = []
    ngram_vectors = []
    vector_o = []
    i = 0
    while i < len(prepared_text):
        gram_vectors.append(encode_gram(prepared_text[i]))
        i += 1
    i = 0
    while i < len(gram_vectors) - 3:
        ngram_vectors.append(encode_ngram_noperm([gram_vectors[i], gram_vectors[i+1], 
                                              gram_vectors[i+2]]))
        i += 1
    i = 0
    vector_o = encode_ngrams(ngram_vectors)
    vector_o = np.array(vector_o)
    return vector_o
