#!/usr/bin/python

import commands

class Analysis:
    features = []

    def fileToFeatureSet(self, absfilepath):
        rout = commands.getoutput('./MIRS/analysis.r '+absfilepath).split(' ')
        rout = filter(None,rout)
        if rout[0]!='Error':
            self.features = map(float,rout)

    def getFeatureList(self):
        return self.features

    def __init__(self, filepath):
        self.fileToFeatureSet(filepath)