#!/usr/bin/python

import database, ranking, analysis

def rank(infile,directory):
    analysis = new Analysis(infile)
    db = new Database(directory)
    ranking = new Ranking(analysis.getFeatureList(),db.getDbDict())
    return ranking.getRankingList()

__all__ = ["database", "ranking", "analysis"]