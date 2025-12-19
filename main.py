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
def compareData():    
    return

# write Data
def writeData():

    return

### MAIN ###
loadData()
compareData()
writeData()