import sklearn
import sklearn.datasets
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from geolang.src.classifiers.bunch_data import bunch_training

def get_shape(arr):
    '''
    Return shape of an array
    '''
    array = np.array(arr)
    return array.shape

def count_vectorize(training):
    '''
    Vectorizes the training text data.

    Inputs:
    training -- a Bunch object, utilize bunch_training method in bunch_data.py

    Outputs:
    X_train -- Numpy array of vectorized training data
    count_vect -- count vectorizer object
    tf_transformer -- transformer object
    '''
    training_df = pd.DataFrame(training.data)
    training_df.astype('U').values.ravel()
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(training_df.astype('U').values.ravel())
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    return X_train_tfidf, count_vect, tfidf_transformer
