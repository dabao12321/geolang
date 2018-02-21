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
from clean_geodata import abbrev_to_state

def get_regions():
    regions = {"allegheny mountains": abbrev_to_state("md, va, pa, wv"),
                    "appalachians": abbrev_to_state("pa, wv, md, va, nc, ky, tn, nc, ga, al"),
                    "atlantic": abbrev_to_state("me, nh, vt, ma, ct, ri, ny, pa, nj, de, md, dc, va, nc, ga, sc, fl"),
                    "central": abbrev_to_state("ne, ks, mo, ok, ar"),
                    "central atlantic": abbrev_to_state("pa, de, nj, md, dc, va"),
                    "chesapeake bay": abbrev_to_state("md, va"),
                    "delmarva": abbrev_to_state("de, md, va"),
                    "desert southwest": abbrev_to_state("ca, az, nm"),
                    "great lakes": abbrev_to_state("mn, wi, mi, il, in, oh, pa, ny"),
                    "gulf states": abbrev_to_state("tx, la, ms, al, fl"),
                    "inland north": abbrev_to_state("wa, or, id, mt, wy, nd, sd, mn, ia, wi, il, mi, in, oh, pa, ny, nj"),
                    "inland south": abbrev_to_state("ky, tn, al, ms"),
                    "lower mississippi valley": abbrev_to_state("mo, ky, il, tn, ar, la, ms"),
                    "middle atlantic": abbrev_to_state("md, dc, va, nc, sc"),
                    "midland": abbrev_to_state("sd, ne, ia, mo, ok, ar, la, ms, tn, ky, il, in, oh, wv, pa, md, de, nj, va, nc, ga, al, sc"),
                    "mississippi valley": abbrev_to_state("mn, wi, ia, il, mo, ar, ky, tn, la, ms"),
                    "mississippi ohio valleys": abbrev_to_state("mn, wi, ia, il, mo, in, oh, ky"),
                    "new england": abbrev_to_state("vt, nh, me, ma, ct, ri"),
                    "north": abbrev_to_state("wa, or, id, mt, wy, nd, sd, mn, wi, ia, il, mi, in, oh, pa, ny, nj, ct, vt, nh, ma, ri, me"),
                    "north atlantic": abbrev_to_state("me, nh, vt, ny, nj, ma, ct, ri"),
                    "north central": abbrev_to_state("wi, mi, il, in, oh, ky"),
                    "north midland": abbrev_to_state("ne, sd, ia, mo, il, in, oh, wv, pa, md, de, nj"),
                    "northeast": abbrev_to_state("pa, nj, ny, vt, nh, ma, ct, me, ri"),
                    "northwest": abbrev_to_state("wa, or, id, mt, wy"),
                    "ohio valley": abbrev_to_state("il, mo, ky, in, oh"),
                    "okefenokee": abbrev_to_state("ga, fl"),
                    "ozarks": abbrev_to_state("mo, ok, ar"),
                    "pacific": abbrev_to_state("wa, or, ca"),
                    "pacific northwest": abbrev_to_state("wa, or, ca"),
                    "plains states": abbrev_to_state("co, ks, ne"),
                    "rocky mountains": abbrev_to_state("id, mt, wy, co, ut, nv"),
                    "smoky mountains": abbrev_to_state("tn, nc"),
                    "south": abbrev_to_state("tx, la, ms, al, fl, ga, nc, sc, va, dc, md"),
                    "south atlantic": abbrev_to_state("nc, ga, sc, fl"),
                    "south midland": abbrev_to_state("ok, mo, ar, la, ms, il, in, ky, tn, al, oh, wv, va, nc, ga, dc, md, de, sc"),
                    "southeast": abbrev_to_state("ms, tn, al, nc, ga, fl, sc"),
                    "southwest": abbrev_to_state("az, nm, tx, ca, ok"),
                    "upper midwest": abbrev_to_state("nd, sd, ne, mn, ia"),
                    "upper mississippi valley": abbrev_to_state("mn, ia, mo, wi, il"),
                    "west": abbrev_to_state("wa, or, ca, nv, az, id, ut, nm, mt, wy, co, ok, tx, nd, sd, ne, ks, ok"),
                    "west midland": abbrev_to_state("sd, ne, ia, mo, ok, ar, la, ms, il, in, oh, ky, tn, al, wv, va, nc, sc")
                   }
    return regions

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
