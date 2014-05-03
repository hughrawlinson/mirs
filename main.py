#!/usr/bin/python

import sys, csv, commands, operator
from math import sqrt, pow
from os import listdir
from os.path import isfile, join, abspath

def main(infile,directory):
    featureset = fileToFeatureSet(abspath(infile).replace(' ','\ '))
    db = getDbByDirectory(directory)
    return ranking(featureset,db)

def ranking(featureset,db):
    ranking = list()
    for f in db.keys():
        #euclidean distance between normalized flatness and rms
        #index to feature mapping: [0->duration,1->specCent,2->specFlat,3->normRMS]
        if f != 'meta':
            ranking.append([f,
                sqrt(pow(((db[f][0]-db['meta'][0])/db['meta'][1]-(featureset[0]-db['meta'][0])/db['meta'][1]),2)+pow(((db[f][1]-db['meta'][2])/db['meta'][3]-(featureset[1]-db['meta'][2])/db['meta'][3]),2)+pow((db[f][2]-featureset[2]),2)+pow((db[f][3]-featureset[3]),2))])
    ranking.sort(key=operator.itemgetter(1))
    return ranking

def fileToFeatureSet(absfilepath):
    rout = commands.getoutput('./r/analysis.r '+absfilepath).split(' ')
    rout = filter(None,rout)
    if rout[0]!='Error':
        return map(float,rout)

def getDbByDirectory(directory):
    if(not isfile(directory+'/.mirs.csv')):
        db = analyzeDirectory(directory)
        saveCreatedDatabase(directory,db)
        return db
    else:
        db = dict()
        with open(directory+'/.mirs.csv','rb') as mirsfile:
            reader = csv.reader(mirsfile)
            for row in reader:
                if(row[0]!='filename'):
                    db[row[0]] = map(float,row[1:])
        return db

def analyzeDirectory(directory):
    files = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
    db = dict()
    durBounds = [sys.float_info.max,0]
    scBounds = [sys.float_info.max,0]
    for f in files:
        db[f] = fileToFeatureSet(abspath(directory).replace(' ','\ ')+'/'+f)
        if db[f][0] < durBounds[0]:
            durBounds[0] = db[f][0]
        if db[f][0] > durBounds[1]:
            durBounds[1] = db[f][0]
        if db[f][1] < scBounds[0]:
            scBounds[0] = db[f][1]
        if db[f][1] > scBounds[1]:
            scBounds[1] = db[f][1]
    db['meta'] = durBounds + scBounds
    return db

def saveCreatedDatabase(directory, db):
    with open(directory+'/.mirs.csv', 'wb') as mirsfile:
        writer = csv.writer(mirsfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # writer.writerow(['filename','duration','spectralCentroid','spectralFlatness','normalizedRMS'])
        for f in db.keys():
            writer.writerow([f]+db[f])

if __name__ == '__main__':
    ranking = main(sys.argv[1], sys.argv[2])
    for x in range(0,len(ranking)):
        print "{}: {} - Distance: {}".format(x+1,ranking[x][0],ranking[x][1])


