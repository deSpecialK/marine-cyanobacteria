#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script analyses similarities of marine cyanobacteria in different seas of the world
Authors: Cosmima Schilling, Julian Weber, Sofia Kasek and Karsten Voigt
"""

# load Data from files
def loadData():
    return

# Compare Data sets
def compareData():
    return

# write Data
def writeData(fileCyanoCompared):
    fileCyanoComparedLines=fileCyanoCompared.readlines()
    i=1
    for cyanobacterium in fileCyanoComparedLines:
        bacterium=bacterium.strip()  #das hat den Umbruch nach jedem Element weggestript
        print(i, bacterium)
        i+=1
    return

### MAIN ###