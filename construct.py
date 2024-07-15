##FUNCTIONS FOR CONSTRUCTING AND COMBINING HYPERVECTORL##

import numpy as np
import random

dim = 120
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

