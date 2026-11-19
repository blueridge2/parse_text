# This is a sample Python script.

# this file is a test case of the spacy module described at https://spacy.io/
# for spacy to function correctly, one must load the en_core_web_sm into the .venv
# using the command  python -m spacy download en_core_web_sm
# to do this I opened a the using the terminal button on the side of the pycharm ide
# ad cd to .venv directory
# then I ran the command  python -m spacy download en_core_web_sm


import spacy

def parse_text(name: str):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_sm")

    # Process whole documents
    text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")
    doc = nlp(text)

    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_text('call spacy text')

