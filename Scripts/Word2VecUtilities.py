from Scripts.SentencesIteratorForWV import SentencesIteratorForWV
from gensim.models.word2vec import Word2Vec
import numpy as np


class Word2VecUtilities(object):
    def create_word2vector_model(sentences, wv_size=150, min_count=0, num_iter=2):
        model = Word2Vec(SentencesIteratorForWV(sentences),
                         size=wv_size, min_count=min_count, workers=4, iter=num_iter)
        return model

    def create_embeddings_matrix(model, rev_vocab_dict):
        embeddings_matrix = np.asarray([model.wv.__getitem__(rev_vocab_dict[vocab_id])
                                        if rev_vocab_dict[vocab_id] in model.wv.vocab.keys()
                                        else np.zeros((50,)) for vocab_id in range(len(rev_vocab_dict))])
        return embeddings_matrix

    def save_word2vector_model(model, file_path_name):
        model.save(file_path_name)

    def load_word2vector_model(file_path_name):
        model = Word2Vec.load(file_path_name)
        return model
