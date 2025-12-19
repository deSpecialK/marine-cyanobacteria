#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script analyses similarities of marine cyanobacteria in different seas of the world
Authors: Cosmima Schilling, Julian Weber, Sofia Kasek and Karsten Voigt
"""

# modules


# Variables definitions 

# load Data from files, define separator if needed, delete header if needed
def load_data(file_handle,sep=None, header=False):
	ohandle    = open(file_handle, 'r')
	obuffer    = ohandle.readlines()
	ohandle.close()
	file_data   = []
	head_info   = ""
	if sep:
		for i in obuffer:
			if header:
				header   = False
				head_info = i
				continue
			atoms = string.split(i.strip("\n"), sep)
			file_data.append(atoms)
	else:
		for i in obuffer:
			if header:
				header = False
				head_info = i
				continue
			file_data.append(i.strip("\n"))
	return file_data, head_info

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
    return

### MAIN ###
loadData()
compareData()
writeData()