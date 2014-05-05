#!/usr/bin/python

import operator
from math import sqrt

class Ranking:
    rankData = list()

    def ranking(self, featureset, db):
        ranking = list()
        for f in db.keys():
            #euclidean distance between normalized flatness and rms
            #index to feature mapping: [0->duration,1->specCent,2->specFlat,3->normRMS]
            if f != 'meta':
                ranking.append([f,
                    sqrt(pow(((db[f][0]-db['meta'][0])/db['meta'][1]-(featureset[0]-db['meta'][0])/db['meta'][1]),2)+pow(((db[f][1]-db['meta'][2])/db['meta'][3]-(featureset[1]-db['meta'][2])/db['meta'][3]),2)+pow((db[f][2]-featureset[2]),2)+pow((db[f][3]-featureset[3]),2))])
        ranking.sort(key=operator.itemgetter(1))
        self.rankData = ranking

    def getRankingList(self):
        return self.rankData

    def __init__(self,featureset,db):
        self.ranking(featureset,db)