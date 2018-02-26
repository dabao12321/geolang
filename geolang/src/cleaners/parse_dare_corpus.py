'''
Gather vocabulary unique to a certain region of the U.S. Data via the DARE corpus.
Link to original dataset: https://www.kaggle.com/rtatman/dictionary-of-american-regional-english-dareds
Link to original research: https://www.daredictionary.com/
'''

import json
import string
import numpy as np
import pandas as pd
import nltk
from sklearn import svm
from clean_geodata import abbrev_to_state, get_regions

def expand_region(region, word):
    '''This expands a singular entry of a general region to multiple entries containing
    each state within the region. Takes in two string entries and outputs a pandas DataFrame

    Ex: The call 'expand_region('pacific', 'hi')' will return a DataFrame:

        dialect   word
    0  washington   hi
    1      oregon   hi
    2  california   hi

    '''
    regions = get_regions()
    states = regions[region].split(", ")
    toadd = pd.DataFrame()
    toadd['dialect'] = states
    toadd['word'] = word
    return toadd

def clean_dare():
    alldata = pd.read_json("../../data/geodare.json")
    alldata = alldata.drop("dialect subregions", axis=1)
    todrop = []
    regions = get_regions()
    for index, row in alldata.iterrows():
        if row["dialect"] in regions.keys():
            toadd = expand_region(row['dialect'], row['word'])
            alldata = alldata.append(toadd)
            todrop.append(index)

    alldata = alldata.drop(todrop, axis = 0)
    alldata = alldata.reset_index()
    for index, row in alldata.iterrows():
        alldata.set_value(index, 'index', index)

    return alldata

def print_dare_file(overrule=False):
    daredata = clean_dare()
    if overrule:
        daredata.to_csv("../../data/cleaned_dare_corpus.csv", sep = ",", index=False)
    else:
        daredata.to_csv("../../data/cleaned_dare_corpus_new.csv", sep = ",", index=False)
