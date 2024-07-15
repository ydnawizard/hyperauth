#Hyperdimensional Authorship Detection
#Witten by Ellis (Andy) Weglewski
from encode import encode
from authors import *
from methods import encode_punct_and_length
from methods import encode_pos
from writer import writer

profile_size=10000
dim = 120

authors = [forester,shakespeare,melville,tolkien,lautreamont,caroll]

author_names = ["forester","shakespeare","melville","tolkien","lautreamont","caroll"]


chunk_size = 10000

def main():
    j = 0
    chunk_size = 10000
    from identify import identify
    pl_authors = authors
    pos_authors = authors
    #punct_and_length_profiles = encode_punct_and_length(pl_authors)
    pos_profiles = encode_pos(pos_authors)
    while chunk_size >= 8000:
        forester_chunk = forester[:chunk_size]
        shakespeare_chunk = shakespeare[:chunk_size]
        melville_chunk = melville[:chunk_size]
        tolkien_chunk = tolkien[:chunk_size]
        lautreamont_chunk = lautreamont[:chunk_size]
        caroll_chunk = caroll[:chunk_size]
        author_chunks = [forester_chunk, shakespeare_chunk, melville_chunk, tolkien_chunk, lautreamont_chunk, caroll_chunk]
        #punct_and_length_chunks = encode_punct_and_length(author_chunks)
        pos_chunks = encode_pos(author_chunks)
        pos_profile_vectors = []
        for i in pos_profiles:
            i = encode(i)
            pos_profile_vectors.append(i)
        for i in pos_chunks:
            to_write = identify(i, pos_profile_vectors)
            print(to_write)
            writer(to_write, 'part of speech tagged', j, chunk_size)
            j += 1
            """
        j -= len(authors)
        punct_and_length_profile_vectors = []
        for i in punct_and_length_profiles:
            i = encode(i)
            punct_and_length_profile_vectors.append(i)
        for i in punct_and_length_chunks:
            to_write = identify(i, punct_and_length_profile_vectors)
            print(to_write)
            writer(to_write, 'punct and word length', j, chunk_size)
            j += 1
        j += len(authors)
        """
        chunk_size = chunk_size - 200
        print(chunk_size)


if __name__ == "__main__":
    main()

