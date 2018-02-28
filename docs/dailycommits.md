# Daily Commit Log

### 1/21/2018
- Came up with idea for project
- updated README
- created a tentative project plan

### 1/22/2018
- added conduct & contributing
- research on linguistics/geographic lexicon

### 1/24/2018
- more data gathering
- created folder structure
- started jupyter notebook for vocabulary classification

### 1/25/2018
- began parsing through DARE corpus
- split U.S. into discrete regions (non-overlapping, state boundaries)
- created a TODO file to outline project's next steps for other contributors

### 1/29/2018
- merged Gerardo's pull request (transcribed speech from people of various origins in .trn format, labeled in corresponding .csv metadata files)
- continued parsing through the DARE corpus
- restructured folder hierarchy (src vs data files, moved jupyter notebooks to src)

### 1/30/2018
- researched sk-learn's implementation of Bayesian classifiers
- researched how to build a Naive Bayes classifier for assigning probabilities of a speaker's geographic origin based on inputted text.
  - worked through a general naive bayes classifier worksheet (not related to/included in repo)

### 2/2/2018
- split U.S. regions into individual rows for easier future use of Bayes classifier
  - ex. instead of {'nh, ma, ri', 'groaner'}, expand into
  {'nh', 'groaner'}
  {'ma', 'groaner'}
  {'ri', 'groaner'}
- finished parsing through DARE corpus
- exported cleaned pandas DataFrame of state-specific words to a new .csv file
  - 'cleaned_dare_corpus.csv'

### 2/5/2018
- began working on a new notebook for classification purposes
  - vectorizing words/sentences
  - Naive Bayes classifier for predicting geographic origins
- reviewed Jocelyn's pull request to add an SVM plotting function
  - left it unmerged (for now), since I'm not yet planning to implement an SVM classifier
- researched the pros/cons of Bayesian classifiers versus SVMs

### 2/7/2018
- worked with .csv data in classification notebook
- began using sklearn to classify dataset
- assigned targets (corresponding to states) to geodare data

### 2/10/2018
- fixed multiple indexing/null entry related bugs in dataset
- vectorized DARE corpus with sklearn's CountVectorizer
- normalized inputted training data with sklearn's tfidf transformer
- created and trained a Naive Bayes classifier on DARE corpus
  - initial testing indicates that it can functionally predict geographic origin,
  given the presence of one or more documented wordsgit

### 2/19/2018
- merged sarah's modified pull request on deriving .txt data from .trn dataset
- merged kunal's weeklong pull request converting .txt data to a .csv format
- condensed kunal's and sarah's contributions plus my own modifications into a
jupyter notebook, so it will be able to be replicated by any user if necessary
- enhanced documentation for `transcriptions.ipynb`

### 2/20/2018
- cleaned and converted the transciptions into pandas DataFrames
- vectorized SB transcriptions with sklearn's CountVectorizer
- normalized transcription data with sklearn's tfidf transformer
- added this Bunch to the Naive Bayes classifier on DARE corpus
  - parameters (both, dare, transcriptions) determine which sets to train on

### 2/22/2018
- reorganzied 'src' structure around .py files, rather than jupyter notebooks
- enhanced cleaners methods
- enhanced vectorizers (under classifiers)
- added `__init__.py` files to support relative imports

### 2/23/2018
- finalized Naive Bayes classifier, working model
- added classification src code, new files:
  - bunch_data.py
  - vectorize_data.py
  - naive_bayes.py
- added functionality with optional parameters in methods bunch_training,
  count_vectorize, and predict_multinomial_NB

### 2/27/2018
- restructured geolang project, more intuitive.
- added docs and test folder, more unit tests, docs/structure.md
- added a setup.py and requirements.txt for simple installation
- improved CONTRIBUTING.md, README.md
