import numpy as np

def one_hot_encode_matrix(X, vocab_size):
    one_hot_encoded_lists = []
    for text_array in X:
        one_hot_encoded_lists.append(np.asarray([1 if word_id in text_array else 0 for word_id in range(vocab_size)]))
    one_hot_encoded_matrix = np.vstack(one_hot_encoded_lists)
    return one_hot_encoded_matrix