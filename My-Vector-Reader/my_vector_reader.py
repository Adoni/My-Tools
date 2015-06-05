import numpy

def vector_reader(file_name, coding_type, as_dict=False):
    ##MODE:
    ##DICT: return the vectors as dict
    ##LIST: return two lists
    words=[]
    vectors=[]
    vector_file=open(file_name)
    words_count,vector_size=map(lambda x:int(x),vector_file.readline()[:-1].split(' '))
    for line in vector_file:
        line=line.decoding(coding_type)[:-1].split(' ')
        word=line[0]
        vector=map(lambda x:float(x),line[1:])
        if not len(vector)==vector_size:
            continue
        words.append(word)
        vectors.append(vector)
    vectors=numpy.array(vectors)
    if as_dict:
        return dict(zip(words,vectors))
    else:
        return words,vectors
