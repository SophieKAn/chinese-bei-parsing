import os
import sys
from hanziconv import HanziConv
from snownlp import SnowNLP

## Main ##
def main():
    corpus = "data/UD_Chinese/zh-ud-train.conllu"

    ### Find bei sentences ###
    bei_sentences, bei_count = find_bei_sentences(corpus)
    print("{} bei sentences.".format(bei_count))

    ### Find short/long passives ###
    long_passives = detokenize(findLongs(bei_sentences))
    short_passives = detokenize(findShorts(bei_sentences))

    ### Sentiment Analysis ###
    s = SnowNLP(long_passives[0])
    print(s.sentiments)



## Functions ##
def find_bei_sentences(corpus):
    bei_sentences = []
    bei_count = 0
    with open (corpus) as data_file:
        is_bei = False;
        sentence = []
        for line in data_file:   
            token = line.split("\t")
            if len(token) > 1:
                token[1] = token[1]
            if u'\u88ab' in token:
                is_bei = True
                bei_count += 1

            if len(token) == 1 and is_bei == True:
                bei_sentences.append(sentence)
                sentence = []
                is_bei = False 
            elif len(token) == 1 and is_bei == False:
                sentence = []
                is_bei = False
            else:
                sentence.append(token)
    return bei_sentences, bei_count


def findLongs(bei_sentences):
    longs = []
    for sentence in bei_sentences:
        for token in range(len(sentence)):
            if u'\u88ab' in sentence[token]:
                if sentence[token+1][3] != 'VERB':
                    longs.append(sentence)

    print("{} long passives.".format(len(longs)))
    return longs

def findShorts(bei_sentences):
    shorts = []
    for sentence in bei_sentences:
        for token in range(len(sentence)):
            if u'\u88ab' in sentence[token]:
                if sentence[token+1][3] == 'VERB':
                    shorts.append(sentence)

    print("{} short passives.".format(len(shorts)))
    return shorts

def detokenize(set_of_passives):
    sentence_strings = []
    for sentence in set_of_passives:
        sentence_chars = []
        for token in sentence:
            sentence_chars.append(token[1])
        sentence_strings.append(''.join(sentence_chars))
    return sentence_strings

main()

