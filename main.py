#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script analyses similarities of marine cyanobacteria in different seas of the world
Authors: Cosmima Schilling, Julian Weber, Sofia Kasek and Karsten Voigt
"""

# modules


# Variables definitions 

# load Data from files
def load_data(file_handle):
    # open the given file handle and read it line by line and close it
	ohandle    = open(file_handle, 'r')
	obuffer    = ohandle.readlines()
	ohandle.close()
    # define array for data
	file_data   = []
    # iterate over all lines in buffer and add it to the array
	for i in obuffer:
		file_data.append(i.strip("\n"))
    # return the array
	return file_data

# Compare Data sets
def compareData(lines_doc_1, lines_doc_2):
    for i in range(len(lines_doc_1)):
        for x in range(len(lines_doc_2)):
            if lines_doc_1[i] == lines_doc_2[x]:
                sameLines = lines_doc_1[i]
    return sameLines

# write Data
def writeData(fileCyanoCompared):
    fileCyanoComparedLines=fileCyanoCompared.readlines()
    i=1
    for bacterium in fileCyanoComparedLines:
        bacterium=bacterium.strip()  #das hat den Umbruch nach jedem Element weggestript
        print(i, bacterium)
        i+=1
        # datei.write(str(i) + name + "\n")
    return

### MAIN ###
load_data()
compareData()
writeData()