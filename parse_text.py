#!/usr/bin/env python
#
# This file is a test case of the spacy module described at https://spacy.io/
# for spacy to function correctly, one must load the en_core_web_sm into the .venv
# using the command  python -m spacy download en_core_web_sm
# to do this I opened a terminal using the terminal button on the side of the pycharm ide
# and cd to .venv directory
# then I ran the command  python -m spacy download en_core_web_sm


import spacy
import argparse
import sys


def read_file(path:str)->str:
    """
    Read a text file.
    :param path: path to the file to be read
    :return: file text
    """
    with open(path, "r", encoding="utf-8") as file:
        file_text = file.read()
    return file_text

def parse_text(language_model: str, text:str):
    """
        parse the test using spacy and "en_core_web_sm
           :param language_model: the name of the logger
           :param text: the text to be parsed
           :return: None
           """

    # Load English tokenizer, tagger, parser and NER
    try:
        nlp = spacy.load(language_model)
    except OSError as error:
        print(f"{type(error).__name__}: {error}")
        print(f"Could not load the spacy language model{language_model}")
        print(f"Use the command python -m spacy download {language_model}")
        print(f"to load the model from spacy.io")
        exit(1)
    else:
        print(f"Loaded the spacy language model{language_model}")

    # Process whole documents
    #text = ("When Sebastian Thrun started working on self-driving cars at "
    #        "Google in 2007, few people outside of the company took him "
    #        "seriously. “I can tell you very senior CEOs of major American "
    #        "car companies would shake my hand and turn away because I wasn’t "
    #        "worth talking to,” said Thrun, in an interview with Recode earlier "
    #        "this week. My name is Roger Rabbit and want to go to the city of Metropolis")

    doc = nlp(text)

    # Analyze syntax
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Propper Names:", [token.lemma_ for token in doc if token.pos_ == "PROPN"])
    names = [ent.text.strip() for ent in doc.ents if ent.label_ == "PERSON"]
    print("The names in the doc are")
    for  name in names:
        print(name)

    # Find named entities, phrases and concepts
    #for entity in doc.ents:
    #    print(entity.text, entity.label_)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="parse a file for Proper Names using spacy",
                        type=str)
    args = parser.parse_args()
    # get the file path
    file_path = args.file_name
    # get the text
    doc_text = read_file(file_path)
    spacy_language_model = "en_core_web_sm"
    # now pass to the language parser
    parse_text(spacy_language_model, doc_text)

