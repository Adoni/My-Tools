#coding:utf8
import numpy

class simple_embedding_cluster_viewer:
    def __init__(self, file_name, coding_type):
        self.vocab, self.vectors=read_vectors(file_name,coding_type)

    def get_closest_words(self, word, count=10):
        if type(word) is str:
            word=word.decode('utf8')
        if word not in self.vocab:
            return []
        word_vec=self.vectors[self.vocab.index(word)]
        closest_words=numpy.sum((self.vectors-word_vec)**2,axis=1).argsort()
        return map(lambda x:self.vocab[x],closest_words[1:count+1])

    def __getitem__(self,word):
        if type(word) is str:
            word=word.decode('utf8')
        if word not in self.vocab:
            return None
        return self.vectors[self.vocab.index(word)]


def read_vectors(file_name, coding_type='utf8', as_dict=False, decode=False):
    ##MODE:
    ##DICT: return the vectors as dict
    ##LIST: return two lists
    vocab=[]
    vectors=[]
    vector_file=open(file_name)
    vocab_count,vector_size=map(lambda x:int(x),vector_file.readline()[:-1].split(' '))
    for line in vector_file:
        if decode:
            line=line.decode(coding_type)
        line=line[:-1].split(' ')
        word=line[0]
        while '' in line:
            line.remove('')
        if not len(line)-1==vector_size:
            continue
        vector=map(lambda x:float(x),line[1:])
        vocab.append(word)
        vectors.append(vector)
    vectors=numpy.array(vectors)
    if as_dict:
        return dict(zip(vocab,vectors))
    else:
        return vocab,vectors

if __name__=='__main__':
    viewer=simple_embedding_cluster_viewer('/Users/sunxiaofei/2012-1-embedding.data','utf8')
    while 1:
        word=raw_input('Word: ')
        print ' '.join(viewer.get_closest_words(word))
