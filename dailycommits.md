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
