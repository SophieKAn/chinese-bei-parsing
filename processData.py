## Sophia Anderson | ander569@wwu.edu | 28 March 2016

import os
import sys




def main(args):

  with open ("test.txt") as data_file:
    line_number = 0;
    for line in data_file:
      line_number += 1
      sentence = line.split("\t")
      if len(sentence) > 1:
        sentence[1] = sentence[1].decode("utf-8")
      if u'\u88ab' in sentence:
          print("It's a bei sentence!")


  print(line_number)



main(sys.argv)
