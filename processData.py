## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys


def main(args):

    with open ("test.txt") as data_file:
        is_bei = False;
        sentence = [[]]
        for line in data_file:
            token = line.split("\t")
            if len(token) > 1:
                #print(token[1])
                token[1] = token[1].decode("utf-8")
                #print(token[1])
            if u'\u88ab' in token:
                is_bei = True


            if len(token) == 1 and is_bei == True:
                print("It's Bei!")
                sentence = [[]]
                is_bei = False 
            elif len(token) == 1 and is_bei == False:
                print("Not a BEI")
                sentence = [[]]
                is_bei = False
            else:
                sentence.append(token)



    for token in sentence:
        if len(token) > 1:
            print(token[1])




main(sys.argv)
