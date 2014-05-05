#!/usr/bin/python

from MIRS import rank

if __name__ == '__main__':
    rankList = rank(sys.argv[1],sys.argv[2])
    for i, rank in enumerate(rankList):
        print "{}: {} - Distance: {}".format(i+1,rank[0],rank[1])
