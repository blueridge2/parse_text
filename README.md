This is a program that uses spacy to parse text and print out the proper names in a file.
You will have to create a virtual environment and load the language model in the virtual environment.
There are limitations to the program.  It loads the entire file into a one string and the default max length is
1,000,000 characters.  Read the documentation on how to adjust this limit
Follow the instructions for Pycharm or Linux

First
python3 -m venv .venv
source .venv/bin/activate
Next
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
