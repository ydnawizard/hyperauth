from main import *
from encode import *
from scipy.spatial import distance

def identify(text, profiles):
    i = 0
    j = 0
    input_text=encode(text)
    print(input_text)
    hamming_distances = []
    while j < len(profiles):
        a = distance.hamming(input_text, profiles[i])
        b = distance.hamming(input_text, profiles[j])
        if a > b:
            hamming_distances.append(str(b) + ' ' + author_names[j])
            print(b)
            i = j
            j += 1
        else:
            hamming_distances.append(str(b) + ' ' + author_names[j])
            print(b)
            j += 1
    return hamming_distances
