#!/usr/bin/python

"""
here's some docs
"""

import commands

class Analysis:
    """
    A feature set extraction class for MIRS.

    Currently the analysis class uses RScript to perform audio analysis, however I will migrate this functionality into Python to remove this dependency in the near future
    """
    features = []

    def fileToFeatureSet(self, absfilepath):
        """
        performs the feature extraction
        """
        rout = commands.getoutput('./MIRS/analysis.r '+absfilepath).split(' ')
        rout = filter(None,rout)
        if rout[0]!='Error':
            self.features = map(float,rout)

    def getFeatureList(self):
        """
        Returns the set of features
        """
        return self.features

    def __init__(self, filepath):
        self.fileToFeatureSet(filepath)