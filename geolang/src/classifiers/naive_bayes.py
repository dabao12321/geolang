import sklearn
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from bunch_data import bunch_training
from vectorize_data import count_vectorize

def train_multinomial_NB(X_train_tfidf, training):
    '''
    Classifies text data based on geographic origin.

    Inputs:
    X_train -- numpy array of vectorized data, see vectorize_data.py
    training -- Bunch of training data, see bunch_data.py

    Outputs:
    Multinomial Naive Bayes classifier object
    '''
    classifier = MultinomialNB().fit(X_train_tfidf, training.target)
    return classifier

def predict_multinomial_NB(testing, training_data='lexicon'):
    '''
    Predicts geographic origin based on classifier.

    Inputs:
    testing -- list of testing data (strings)
    training_data -- the type of data to train on
                    'lexicon' --> DARE corpus only
                    'transcripts' --> SB transcriptions only
                    'all' --> both DARE and SB data

    Outputs:
    res -- list of predicted geographic origins, indexes corresponding to
            testing data indexes.
    '''
    training = bunch_training(training_data)
    X_train_tfidf, count_vect, tfidf_transformer = count_vectorize(training)
    classifier = train_multinomial_NB(X_train_tfidf, training)

    X_testing_counts = count_vect.transform(testing)
    X_testing_tfidf = tfidf_transformer.transform(X_testing_counts)

    predicted = classifier.predict(X_testing_tfidf)
    res = []
    for doc, category in zip(testing, predicted):
        res.append(training.target_names[category])
    return res
