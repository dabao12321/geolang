import csv
import pandas as pd
import string
import nltk
from nltk import RegexpTokenizer

def trn_to_txt():
    '''
    Convert the SB .trn data to .txt data
    Outputs unmodified .txt files found in '../../data/SBData/TXT'
    '''
    for i in range(1,61):
        if i < 10:
            with open("../../data/SBData/TRN/SBC00" + str(i) + ".trn", "r") as f:
                text = f.read()
            f = open("../../data/SBData/TXT/SBC00" + str(i) + ".txt",'w')
            f.write(text)
            f.close()
        elif i == 37 or i == 60:
            pass
        else:
            with open("../../data/SBData/TRN/SBC0" + str(i) + ".trn", "r") as f:
                text = f.read()
            f = open("../../data/SBData/TXT/SBC0" + str(i) + ".txt",'w')
            f.write(text)
            f.close()

def read_metadata():
    '''
    Rewrite the CSV files in a proper format.

    CSV headers are:
    NUMBER,NAME,GENDER,AGE,HOMETOWN,HOMESTATE,CURRENT STATE,
    EDUCATION,YEARS OF EDUCATION,OCUPATION,ETHNICITY
    '''
    df = pd.read_csv("../../data/SBData/dialectsdata/metadata4a.csv")
    with open('../../data/SBData/dialectsdata/metadata4a.csv', 'w') as ma:
        with open('../../data/SBData/dialectsdata/metadata4.csv') as m:
            for line in m.readlines():
                write = csv.writer(ma, dialect='excel')
                write.writerow(line.split(','))

def clean_file(filename='SBC054.txt'):
    '''
    Reads existing .txt files and outputs cleaned .csv files containing
    transcription data. Do not run unless necessary! All cleaned files already exist.

    Input:
    filename -- name of .txt transcription file. Currently set to file 54.

    Output:
    file in CSV format: speaker_name, dialect, word.
    These files are found in '../../data/SBData/dialectsdata'.
    '''
    dialectfile = '../../data/SBData/dialectsdata/' + filename[0:6] + ".csv"
    # change the number for the .txt and .csv each time you move on to the next .txt file
    with open('../../data/SBData/TXT/' + filename) as f:
        data = f.readlines()
    with open(dialectfile, 'w') as r:
        # for oldName and newName, whenever there's speakers who aren't in the metadata CSV, you need to change
        # the line number of your data to the line number where the first speaker who is in the metadata CSV appears
        # (ex: cleanLine(data[0])[0] to cleanLine(data[1])[0])
        oldName = cleanLine(data[0])[0] # must be the starting pt of dialogue
        newName = cleanLine(data[0])[0] # must be the starting pt of dialogue
        fix = []
        # if you change the line number (ex: cleanLine(data[0])[0] to cleanLine(data[1])[0]), you need to slice the
        # data variable accordingly (in this case, since the line number is now 1, it should say "for line in data[1:]")
        for line in data:
            sentence = ""
            no_punc = cleanLine(line)
            if len(no_punc) == 0: continue # ignore empty lists

            # see if there's a switch in people talking
            if no_punc[0] in list(df['NAME']) and newName != no_punc[0]:
                oldName = newName
                newName = no_punc[0]

            # put the words in the list together as a sentence
            for elm in no_punc:
                sentence += elm + " "

            # see a new name? write to csv BEFORE appending to 'fix'
            if no_punc[0] in list(df['NAME']) and oldName != newName: # check for name change

                # when running, you need to uncomment below and manually put the names of the people talking
                # and their geographical origin (put 'NA' if unknown and add more elif statements as needed):
                if fix[0][0:len(oldName)] == 'CYNTHIA':
                    state = 'IL'
                elif fix[0][0:len(oldName)] == 'AUD':
                    state = 'NA'
                elif fix[0][0:len(oldName)] == 'MANY':
                    state = 'NA'
                fix = [fix[0][0:len(oldName)], state, fix[0][len(oldName)+1:len(fix[0])-1]]
                write = csv.writer(r, dialect='excel')
                write.writerow(fix)
                fix = []

            # append line to person's dialogue
            if len(fix) == 0: fix.append(sentence)
            else: fix[0] += sentence

def format_word(w):
    '''
    Cleans a single word, removing unnecessary alphanumerics or punctuation.
    '''
    newWord = ""
    for i in w:
        # add more edge cases as needed
        if i.isnumeric() or i in ["=", "[", "]", "~", "(", ")"]:
            continue
        else: newWord += i
    return newWord

def clean_line(line):
    '''
    Cleans a single line of text, removing unnecessary alphanumerics or punctuation.
    '''
    no_punc = [word.strip(string.punctuation) for word in line.split()]
    no_punc = no_punc[2:]
    no_punc = [x for x in no_punc if x]
    no_punc = [format_word(x) if x.isalpha() == False else x for x in no_punc]
    return no_punc
