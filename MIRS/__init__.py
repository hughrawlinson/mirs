#!/usr/bin/python

__all__ = ["database", "ranking", "analysis", "rank"]
from database import Database
from ranking import Ranking
from analysis import Analysis

def rank(infile,directory):
    analysis = Analysis(infile)
    db = Database(directory)
    # print analysis.getFeatureList()
    # print db.getDbDict()
    ranking = Ranking(analysis.getFeatureList(),db.getDbDict())
    return ranking.getRankingList()

if __name__ == '__main__':
    rankList = rank(sys.argv[1],sys.argv[2])
    for i, rank in enumerate(rankList):
        print "{}: {} - Distance: {}".format(str(i+1),str(rank[0]),str(rank[1]))
