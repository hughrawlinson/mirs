#!/usr/bin/python

from os import listdir
from os.path import abspath, isfile
import csv
import analysis

class Database:
    db = dict()
    directory = ""

    def analyzeDirectory(self):
        files = [ f for f in listdir(self.directory) if isfile(join(self.directory,f)) ]
        durBounds = [sys.float_info.max,0]
        scBounds = [sys.float_info.max,0]
        for f in files:
            ana = Analysis(self.directory+"/"+f)
            self.db[f] = ana.getFeatureArray()
            if self.db[f][0] < durBounds[0]:
                durBounds[0] = self.db[f][0]
            if self.db[f][0] > durBounds[1]:
                durBounds[1] = self.db[f][0]
            if self.db[f][1] < scBounds[0]:
                scBounds[0] = self.db[f][1]
            if self.db[f][1] > scBounds[1]:
                scBounds[1] = self.db[f][1]
        self.db['meta'] = durBounds + scBounds

    def save(self):
        with open(directory+'/.mirs.csv', 'wb') as mirsfile:
            writer = csv.writer(mirsfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # writer.writerow(['filename','duration','spectralCentroid','spectralFlatness','normalizedRMS'])
            for f in self.db.keys():
                writer.writerow([f]+self.db[f])

    def readFromDisk(self):
        with open(self.directory+'/.mirs.csv','rb') as mirsfile:
            reader = csv.reader(mirsfile)
            try:
                for row in reader:
                    #catch R errors
                    if(row[0]!='filename'):
                        self.db[row[0]] = map(float,row[1:])
            except:
                raise IOError

    def getDbDict(self):
        return self.db

    def __init__(self, directory = ".", flush=False):
        self.directory = abspath(directory)+'/'

        try:
            self.readFromDisk()
        except IOError:
            self.analyzeDirectory()
            self.save()
        except Exception as e:
            print e
            print "Unexpected error"