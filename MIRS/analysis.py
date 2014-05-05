#!/usr/bin/python

import commands

class Analysis:
    features = []

    def fileToFeatureSet(absfilepath):
        rout = commands.getoutput('./analysis.r '+absfilepath).split(' ')
        rout = filter(None,rout)
        if rout[0]!='Error':
            return map(float,rout)

    def getFeatureList():
        return self.features

    def __init__(self, filepath):
        self.fileToFeatureSet(filepath)