#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tools for managing data arrays
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from math import pi

# Tools for web service, Flask is easy to set up and to scale:
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField

# Tools for plotting
from bokeh.plotting import figure
from bokeh.embed import components

# Flask app set up
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='sdvflkjhsdfkjhsdf',
    WTF_CSRF_SECRET_KEY='sdfkjhsdfkjhsdf'
))


class TextForm(FlaskForm):
    """
    A form to input text using FlaskForm
    """
    # Should have some validation!
    the_text = TextAreaField(
        'Text to analyze',
    )


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
    # word count, very basic. Ignore punctuation, just spaces:
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


@app.route('/form', methods=['GET', 'POST'])
def manual_input():
    form = TextForm()
    if request.method == 'POST':
        text = request.form['the_text']
        results = analyze_text(text)
        # Char count plot settings
        ccount = figure(
            title="Character count",
            x_range=results.get('unique_chars'),
        )
        ccount.vbar(
            x=[index for index, count in enumerate(results.get('char_counts'))],
            top=results.get('char_counts'),
            width=0.4,
        )
        # Word count plot settings
        wcount = figure(
            title="Word count",
            x_range=results.get('bag_of_words'),
        )
        print(results.get('occurrence_array'))
        wcount.vbar(
            x=[index
               for index, count in enumerate(
                                    results.get('occurrence_array')[0])
               ],
            top=results.get('occurrence_array')[0],
            width=0.4,
        )
        wcount.xaxis.major_label_orientation = pi/2
        print(results.get('occurrence_array'))
        plot = (ccount, wcount)
        comp, div = components(plot)
        return render_template(
                                'results.html',
                                mf=results.get('max_frequence'),
                                wc=results.get('word_count'),
                                nsc=results.get('no_spaces_chars'),
                                mostf=results.get('most_frequent'),
                                script=comp,
                                div=div,
                            )
    return render_template('form.html', form=form)


@app.route('/')
def index():
    """
    This is a sample to test the app
    """
    return str(analyze_text('Hello world!'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
