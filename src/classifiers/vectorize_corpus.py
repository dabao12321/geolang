import sklearn
import numpy as np
import pandas as pd
import nltk
import os
import sys
sys.path.append('../')
from cleaners.clean_geodata import abbrev_to_state


def get_catagories():
    '''
    Return a standard list of regional catagories (states)
    '''
    catagories = []
    geodata = pd.read_csv("../../data/cleaned_dare_corpus.csv")
    for x in geodata['dialect']:
        if x not in catagories:
            catagories.append(x)
    return catagories

def read_DARE():
    '''
    Read in DARE corpus from cleaned CSV, returns data points and target lists.
    Data points are words.
    Targets (states) correspond to the index of said state in catagories.
    '''
    geodata = pd.read_csv("../../data/cleaned_dare_corpus.csv")
    examples = []
    targets = []
    catagories = get_catagories()
    for i,x in enumerate(geodata['word']):
        if pd.notnull(x):
            examples.append(x)
            dialect = geodata.get_value(i,'dialect')
            target = catagories.index(dialect)
            targets.append(target)
    return examples, targets, catagories

def read_SB_transcriptions():
    '''
    Read in SB translations from cleaned CSVs, returns data points and target lists.
    Data points are words.
    Targets (states) correspond to the index of said state in catagories.
    '''
    directory = "../../data/SBData/dialectsdata"
    transcripts = pd.DataFrame({"name":[], "dialect":[], "word":[]})
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv") and filename.startswith("dialects"):
            currpath = os.path.join(directory, filename)
            currdata = pd.read_csv(currpath, names=["name", "dialect", "word"])
            transcripts = pd.concat([transcripts, currdata])
            continue
        else:
            continue
    transcripts = transcripts.reset_index()
    transcripts = transcripts.drop("index", axis = 1)

    SBexamples = []
    SBtargets = []
    catagories = get_catagories()
    for i,x in enumerate(transcripts['word']):
        if pd.notnull(x) and pd.notnull(transcripts.get_value(i, 'dialect')):
            try:
                dialect = transcripts.get_value(i,'dialect')
                dialect = abbrev_to_state(dialect)
                target = catagories.index(dialect)
                SBexamples.append(x)
                SBtargets.append(target)
            except KeyError:
                # These speakers do not identify with a single state, discard.
                pass
    return SBexamples, SBtargets, catagories
