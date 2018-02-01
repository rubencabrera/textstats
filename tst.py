#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

from flask import Flask

app = Flask(__name__)


def analyze_text(text):
    """
    Get statistics from text input.
    Some interesting values that come to mind are:
        - Item count.
        - Item frequency.
        - Word frequency vs word length.
        - Word length measures.
    Words or characters can be items.

    This method returns information to later present as statistics.

    Some errors are detected on the counting, caused by ignored chars or
    words.
    """
    statistics = {}
    # Char length
    statistics['length'] = len(text)
    # word count, very rough ignore punctuation, just spaces:
    statistics['word_count'] = len(text.replace('\n', ' ').split(' '))

    statistics['no_spaces_chars'] = len(list(text.replace(' ', '')))

    statistics['unique_chars'], statistics['char_counts'] = np.unique(
        list(text), return_counts=True)

    # Getting a bag of words using sklearn, single characters like 'a' and
    #   punctuation are ignored by default:
    vectorizer = CountVectorizer(min_df=1)
    occurence_vector = vectorizer.fit_transform([text])
    statistics['bag_of_words'] = vectorizer.get_feature_names()
    n_files, statistics['significant_words'] = occurence_vector.shape
    statistics['occurrence_array'] = occurence_vector.toarray()
    statistics['most_frequent'] = statistics['bag_of_words'][
                                            occurence_vector.toarray().argmax()]
    statistics['max_frequence'] = occurence_vector.toarray(
                                  )[0, occurence_vector.toarray().argmax()]

    return statistics


@app.route('/')
def index():
    return str(analyze_text('Hello world!'))
