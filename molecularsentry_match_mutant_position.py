import sys
import glob
file1= sys.argv[1] # list of the variants file
fh = open(file1.strip(),"r")
file2= sys.argv[2] # output from the epitope.js having epitopes-paratopes information from PDB
eph = open(file2.strip(),"r")
z=fh.readline()
import itertools
from itertools import groupby
#from collections import OrderedDict
import re

# function to split alpha_numberic characters example ["V141K"] to ["V","141","K"]
#def split_text(alnum):
#    for i, j in groupby(alnum, str.isalpha):
#       yield ''.join(j)

##updated for the deletion variants example ["V141-"] to ["V","141","-"]
def split_text(alnumspchr):
    return filter(None, re.split(r'(\d+)', alnumspchr))

# Processing variants file
variants=[]
variants_pos=[]
for line in fh:
    line=line.strip()
    variants.append(line)
    variants_pos.append(list(split_text(line)))
#print(variants_pos)
# https://github.com/ncbi/icn3d/tree/master/icn3dnode
# https://github.com/ncbi/icn3d/blob/master/icn3dnode/epitope.js
# Processing pdb_epitopes_paratopes file from epitope.js command

epipara=[]
for line in eph:
    line=line.strip().split(",")
   # print(line)
    pdb=line[1].strip().split("_")
    epipara.append([pdb[0],pdb[1],line[2].strip()])
#print(epipara)

##updated to get unique epitope-paratope position
unique_epipara = [list(x) for x in set(tuple(x) for x in epipara)]

# matching amino acid postion for wild type and mutant type
match_pos_wild=[]
match_pos_mutant=[]
for i in variants_pos:
    a=int(i[1])
    #print(a)
    for j in unique_epipara:
        b=int(j[2])
        #print(b)
        if a==b:
            match_pos_mutant.append([j+list(i[2])])
            match_pos_wild.append([j+list(i[0])])

# flatten the nested lists
match_pos_wld=(list(itertools.chain.from_iterable(match_pos_wild)))
match_pos_mut=(list(itertools.chain.from_iterable(match_pos_mutant)))

# function for converting list to string as input for interaction2.js command 
def listToString(ls):
    strg = " "
    return (strg.join(ls))

for w, m in zip(match_pos_wld, match_pos_mut):
    print((listToString(w)),(listToString(m)), sep="\n")