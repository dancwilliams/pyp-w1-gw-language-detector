# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    word_count = {}
    
    list_of_words = text.split()
    
    for item in languages:
        counter = 0
        for common_word in item['common_words']:
            if common_word in list_of_words:
                counter += 1
        word_count[item['name']]=counter

    maximum = max(word_count, key=word_count.get)
    
    return maximum
    