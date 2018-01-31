#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(
    description='Get some text and return some statistics')
parser.add_argument('text', metavar='TEXT', help='Texto to analyze')
args = parser.parse_args()


def analyze_text(text):
    """
    """
    statistics = {}
    statistics['length'] = len(text)
    return statistics


if __name__ == "__main__":
    text_to_analyze = args.text
    print(analyze_text(text_to_analyze))
