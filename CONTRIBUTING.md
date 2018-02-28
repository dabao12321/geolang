# How to Contribute

Thank you for being a part of this project! I want to keep it as easy as possible
to contribute changes that get things working in your environment. There will be a
few guidelines below to follow to keep things organized, efficient, and generally
simple.

Please read the [Code of Conduct](CONDUCT.md) before contributing.

## What can I do?
For things to contribute, check out the issues or [benchmarks.md](./docs/benchmarks.md).


## Submitting Pull Requests
First, create a fork of this repository to your own account, then clone it to your
local machine. Make all modifications there, then submit your pull request to the master branch.
Please explain what issues that you are fixing or what features that you are adding.
Make sure that your modified code passes all existing unit tests, and
write new unit tests for added features.

### Running the tests
```
cd test
python test_all.py
```
Ensure that all tests pass!

### Opening issues
If you spot a bug or want to implement a new feature, please open an issue with
a clear description of what changes you believe need to be made.

Bugs:
- How can I recreate the bug (i.e. which files to run, what order, etc.)?
- What is the scope of the bug, to your knowledge?
- What is the error message?

New features:
- Provide as much detail on the new feature as possible.
- What necessitates this feature, and how will it impact the rest of the project?
- List the steps needed to successfully implement the feature.

### Style guide
* Long comments for methods, detailing functionality, input, output, and examples
if necessary
* Comments on their own lines
* Aim for less than 80 characters per line, and do not exceed 100.
* name methods like "method_name()"
* name non-class files like "file_name"
* name class files like "FileName"
