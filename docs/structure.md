# Project Structure

This is how geolang is currently structured:

- geolang
  - docs
  - geolang
    - data
      - SBData
        - dialectsdata
        - metadata
        - TRN
        - TXT
    - src
      - classifiers
      - cleaners
  - test

## docs
This is where all documentation files are. These files
should be written in MarkDown unless strictly necessary otherwise.

## geolang
This is the main folder of geolang, where all the libraries methods and data
are contained. This is a packaged directory, meaning it has an `__init__.py`

### data
All data used for training the classification models are stored here.
This is where the cleaner methods locate raw data. Any subdirectories within data
indicate a large number of files corresponding to one raw dataset.

### src
All of geolang's methods and classes are stored here, under classifiers or cleaners.
Utilize method-based .py files, rather than classes, whenever possible.
More subdirectories may be added later, if necessary.

## test
All unit tests are stored here, testing the files under `../geolang/src`.
Unit tests should be named `test_file_name.py`.
