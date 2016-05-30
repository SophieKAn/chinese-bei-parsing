## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys


def main(args):

    with open ("test.txt") as data_file:
        line_number = 0;
        sentence = [[]]
        for line in data_file:
            line_number += 1
            token = line.split("\t")
            if len(token) == 1:
                sentence = [[]]
            else:
                sentence.append(token)



    for token in sentence:
        if len(token) > 1:
            print(token[1].decode("utf-8"))


    ##if len(token) > 1:
    ##  token[1] = token[1].decode("utf-8")
    ##if u'\u88ab' in token:
    ##    print("It's a bei sentence!")


    ##print(line_number)


main(sys.argv)
