#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from sklearn.feature_extraction.text import CountVectorizer
from pprint import pprint
import numpy as np

parser = argparse.ArgumentParser(
    description='Get some text and return some statistics')
parser.add_argument('--text', metavar='TEXT', help='Text to analyze')
parser.add_argument('--file', metavar='FILE', type=open, help='Text file')
args = parser.parse_args()


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

    # TODO:

    return statistics


if __name__ == "__main__":
    text_to_analyze = args.file.read() or args.text
    pprint(analyze_text(text_to_analyze))
