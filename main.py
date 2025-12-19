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
def compareData(lines_doc_1, lines_doc_2):
    if len(lines_doc_1) != len(lines_doc_2):
        while len(lines_doc_1) < len(lines_doc_2):
            lines_doc_1.append("")
        while len(lines_doc_2) < len(lines_doc_1):
            lines_doc_2.append("")
    for i in range(len(lines_doc_1)):
        for x in range(len(lines_doc_1)):
            if lines_doc_1[i] == lines_doc_2[x]:
                sameLines = lines_doc_1[i]
    return sameLines

# write Data
def writeData():
    return

### MAIN ###