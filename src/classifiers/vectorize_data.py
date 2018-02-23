import sklearn
import numpy as np
import pandas as pd
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def get_shape(arr):
    '''
    Return shape of array
    '''
    array = np.array(arr)
    return array.shape

def count_vectorize(training, normalize='tfidf'):
    '''
    Vectorizes the training text data.

    Inputs:
    training -- a Bunch object, utilize bunch_training method in bunch_data.py
    normalize -- indicates type of normalization applied
        'tf' -- term frequency (unweighted counts)
        'tfidf' -- term frequency times inverse document-frequency (weighted counts)

    Outputs:
    Numpy array of vectorized training data
    '''
    training_df = pd.DataFrame(training.data)
    training_df.astype('U').values.ravel()
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(training_df.astype('U').values.ravel())
    if normalize is 'tf':
        tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    elif normalize is 'tfidf':
        tf_transformer = TfidfTransformer(use_idf=True).fit(X_train_counts)
    else:
        raise ValueError('Invalid parameter input.')
    X_train = tf_transformer.transform(X_train_counts)
    return X_train
