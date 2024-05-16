import spacy


def clean_text(text):
    nlp = spacy.load("en_core_web_sm")
    # Process the text using spaCy
    doc = nlp(text)

    # Remove stop words
    tokens = [token.text for token in doc if not token.is_stop]

    # Remove punctuation
    tokens = [token for token in tokens if token.isalpha()]

    # Join the tokens back into a string
    cleaned_text = " ".join(tokens)

    return cleaned_text
