import string


def clean_text(text):
    # Removing punctuations using replace() method
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text
