##FUNCTIONS FOR WRITING RESULTS TO FILE##

def writer(to_write, method, counter, chunk_size):
    from main import author_names
    name = str(method + '_hamming')
    j = 0
    if counter == 0:
        hamming = open(r'results/' + name +'.txt', "w", encoding = "utf8")
    else:
        hamming = open(r'results/' + name +'.txt', "a", encoding = "utf8")
    hamming.write('hamming distance between ' + method + ' ' + author_names[j] + ' chunk and author profile vectors at chunk size ' + str(chunk_size) + ': \n')
    j += 1
    for i in to_write:
        hamming.write(i + '\n')

