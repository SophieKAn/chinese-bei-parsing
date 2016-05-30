## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys


def main():

    bei_sentences = []

    with open ("test.txt") as data_file:
        is_bei = False;
        sentence = []
        for line in data_file:
            token = line.split("\t")
            if len(token) > 1:
                token[1] = token[1].decode("utf-8")
            if u'\u88ab' in token:
                is_bei = True

            if len(token) == 1 and is_bei == True:
                bei_sentences.append(sentence)
                sentence = []
                is_bei = False 
            elif len(token) == 1 and is_bei == False:
                sentence = []
                is_bei = False
            else:
                sentence.append(token)




main()
