#!/usr/bin/python

import sys, csv, commands, operator
from math import sqrt, pow
from os import listdir
from os.path import isfile, join, abspath

def main(infile,directory):
    featureset = fileToFeatureSet(abspath(infile).replace(' ','\ '))
    db = getDbByDirectory(directory)
    return ranking(featureset,db)

if __name__ == '__main__':
    ranking = main(sys.argv[1], sys.argv[2])
    for x in range(0,len(ranking)):
        print "{}: {} - Distance: {}".format(x+1,ranking[x][0],ranking[x][1])


