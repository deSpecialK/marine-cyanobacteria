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
    ohandle     = open(file_handle, 'r')
    obuffer     = ohandle.readlines()
    origin_name = file_handle.split(".")[0]
    ohandle.close()
    # define array for data
    file_data   = []
    # iterate over all lines in buffer and add it to the array
    for i in obuffer:
	    file_data.append(i.strip("\n"))
    # return the array
    return file_data, origin_name

# Compare Data sets
def compareData(lines_doc_1, lines_doc_2):
    sameLines = []
    for i in lines_doc_1:
        for x in lines_doc_2:
            if i == x:
                sameLines.append(i)
    return sameLines

# write Data
def writeData(fileCyanoCompared):
    i=0
    output_file = "index.html"
    print("Writing to file:", output_file)
    obuffer=open(output_file, "w")
    obuffer.write("<h2> Vergleich Cyanobakterien nach Ort </h2> \n")
    obuffer.write("<p> </p> \n")
    obuffer.write("<body> \n")
    for bacterium in fileCyanoCompared:
        bacterium=bacterium.strip()  #das hat den Umbruch nach jedem Element weggestript
        i+=1
        # print(i, bacterium)
        oline=str("<p>"+str(i)+" "+bacterium+"</p>"+"\n")
        obuffer.write(oline)
    obuffer.write("</body> \n")
    obuffer.close()
    return

### MAIN ###
doc_1   = load_data("arctic_sea.txt")[0]
doc_2   = load_data("med_sea.txt")[0]
doc_3   = load_data("saragossa_sea.txt")[0]
same1_2 = compareData(doc_1, doc_2)
same2_3 = compareData(doc_2, doc_3)
same1_3 = compareData(doc_1, doc_3)
#writeData(same1_2)
writeData(same2_3)
#writeData(same1_3)