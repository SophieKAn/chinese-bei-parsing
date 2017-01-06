## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys
from hanziconv import HanziConv # Converting between traditional and simplified characters

positive = [] # 'bei's with positive usage
negative = [] # 'bei's with negative usage

def main():

    bei_sentences = []
    token_count = 0
    bei_count = 0


    with open ("Data/UD_Chinese/zh-ud-train.conllu") as data_file:
        is_bei = False;
        sentence = []
        for line in data_file:
            token_count += 1
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

    print("{} total tokens.".format(token_count))
    print("{} instances of the bei passive marker.".format(bei_count))

    long_passives = findLongs(bei_sentences)
    file = open("testing.txt","w")
    for sentence in long_passives:
        for token in sentence:
            file.write(HanziConv.toSimplified(token[1]))
            file.write("\n")
    file.close()

    short_passives = findShorts(bei_sentences)


    print("Average distance from head for short sentences is {}".format(averageDistance(short_passives)))
    print("Average distance from head for long sentences is {}".format(averageDistance(long_passives)))


    ##Lets get these dictionaries!

    with open("Data/Sentiment/negative_comment.txt") as file:
        for line in file:
            negative.append(line.rstrip())
    with open("Data/Sentiment/negative_emotion.txt") as file:
        for line in file:
            negative.append(line.rstrip())
    with open("Data/Sentiment/positive_comment.txt") as file:
        for line in file:
            positive.append(line.rstrip())
    with open("Data/Sentiment/positive_emotion.txt") as file:
        for line in file:
            positive.append(line.rstrip())
    with open("Data/NTUSD_simplified/NTUSD_negative_simplified.utf8.txt") as file:
        for line in file:
            negative.append(line.rstrip())
    with open("Data/NTUSD_simplified/NTUSD_positive_simplified.utf8.txt") as file:
        for line in file:
            positive.append(line.rstrip())


    findStats("short", short_passives)
    findStats("long", long_passives)



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


def averageDistance(sentences):
    summ = 0
    count = 0

    for sentence in sentences:
        for token in sentence:
            if u'\u88ab' in token:
                count += 1
                summ += int(token[6])
    return summ/count

def getScore(sentences):
    scores = []
    print("{} total sentences".format(len(sentences)))
    for sentence in sentences:
        score = 0;
        for token in sentence:
            simp_token = HanziConv.toSimplified(token[1])
            if simp_token in negative:
                score += 1
            if simp_token in positive:
                score -=1
        
        scores.append(score)

    return scores
    

def findStats(structure, sentences):
    print("Stats for {} passive sentences:".format(structure))
    scores = getScore(sentences)
    
    pos_count = 0;
    neg_count = 0;
    neu_count = 0;


    for score in scores:
        if score > 0:
            pos_count += 1
        if score < 0:
            neg_count += 1
        if score == 0:
            neu_count += 1

    print("{} positive sentences.".format(pos_count))
    print("{} negative sentences.".format(neg_count))
    print("{} neutral sentences.".format(neu_count))





main()
