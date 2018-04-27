import random
import numpy as np

# <codecell>


def shuffle_array(array):
    shuffled_array = np.random.permutation(array)
    return shuffled_array

def shuffle_two_arrays_in_unison(a,b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def sample_from_array(A, prop, num_rows=True):
    if num_rows==True:
        try:
            sampled_array = A[np.random.choice(A.shape[0], prop, replace=False)]
        except:
            sampled_array = A
    else:
        # proportion is a percentage
        sampled_array = A[np.random.choice(A.shape[0], int(A.shape[0]*prop), replace=False)]
    return sampled_array

def one_hot_encode(a):
    b = np.zeros((len(a), max(a)+1))
    b[np.arange(len(a)), a] = 1
    return b

def split_train_test(X,y, prop=2/3):
    X, y = shuffle_two_arrays_in_unison(X,y)
    X_train = X[0:int(len(X)*prop)]
    y_train = y[0:int(len(y)*prop)]
    X_test = X[int(len(X)*prop):]
    y_test = y[int(len(y)*prop):]
    return X_train, y_train, X_test, y_test