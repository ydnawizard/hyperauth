##ENCODING METHODS##
import re
import nltk
import string

def encode_pos(pos_authors):
    j = 0
    inter = []
    translator = str.maketrans('','',string.punctuation)
    for i in pos_authors:
        i = i.translate(translator)
        i = i.split(' ')
        while i.count(' ') > 0:
            i.remove(' ')
        while i.count('') > 0:
            i.remove('')
        while i.count('\n') > 0:
            i.remove('\n')
        pos_authors[j] = str(i)
        j += 1
    j = 0
    for i in pos_authors:
        i = nltk.word_tokenize(i)
        i = nltk.pos_tag(i)
        pos_authors[j] = i
        j += 1
    j = 0
    for i in pos_authors:
        for k in i:
            k = list(k)
            k = k.pop(1)
            k = str(k)
            inter.append(k)
        pos_authors[j] = inter
        inter = []
        j += 1
    return(pos_authors)

def encode_punct_and_length(pl_authors):
    from dictionary import punctuation
    j = 0
    for i in pl_authors:
        i = re.split(r'(\W)', i)
        while i.count(' ') > 0:
            i.remove(' ')
        while i.count('') > 0:
            i.remove('')
        while i.count('\n') > 0:
            i.remove('\n')
        pl_authors[j] = i
        j += 1
    j = 0
    for i in pl_authors:
        jj = 0
        for k in i:
            if punctuation.find(k) == -1:
                k = len(k)
            i[jj] = str(k)
            jj += 1
        pl_authors[j] = str(i)
        j += 1
    return(pl_authors)
