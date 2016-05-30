## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys


def main():

    bei_sentences = []
    token_count = 0

    with open ("zh-ud-train.conllu") as data_file:
        is_bei = False;
        sentence = []
        for line in data_file:
            token_count += 1
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

    print("{} total tokens.".format(token_count))
    print("{} instances of the bei passive marker.".format(len(bei_sentences)))

    long_passives = findLongs(bei_sentences)
    short_passives = findShorts(bei_sentences)



def findLongs(bei_sentences):
    longs = []
    for sentence in bei_sentences:
        for token in range(len(sentence)):
            if u'\u88ab' in sentence[token]:
                if sentence[token+1][3] != 'VERB':
                    longs.append(sentence)

    print("{} instances of long passive sentences.".format(len(longs)))
    return longs

def findShorts(bei_sentences):
    shorts = []
    for sentence in bei_sentences:
        for token in range(len(sentence)):
            if u'\u88ab' in sentence[token]:
                if sentence[token+1][3] == 'VERB':
                    shorts.append(sentence)

    print("{} instances of short passive sentences.".format(len(shorts)))
    return shorts


main()
