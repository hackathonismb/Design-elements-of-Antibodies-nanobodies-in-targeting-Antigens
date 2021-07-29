import sys
import glob
file1= sys.argv[1] # list of the variants file
fh = open(file1.strip(),"r")
file2= sys.argv[2] # output from the epitope.js having epitopes-paratopes information from PDB
eph = open(file2.strip(),"r")
z=fh.readline()
import itertools
from itertools import groupby
from collections import OrderedDict

# function to split alpha_numberic characters example ["V141K"] to ["V","141","K"]
def split_text(alnum):
    for i, j in groupby(alnum, str.isalpha):
        yield ''.join(j)

# Processing variants file
variants=[]
variants_pos=[]
for line in fh:
    line=line.strip()
    variants.append(line)
    variants_pos.append(list(split_text(line)))
#print(variants_pos)

# Processing pdb_epitopes_paratopes file from epitope.js command

epipara=[]
for line in eph:
    line=line.strip().split(",")
   # print(line)
    pdb=line[1].strip().split("_")
    epipara.append([pdb[0],pdb[1],line[2].strip()])
#print(epipara)

# matching amino acid postion for wild type and mutant type
match_pos_wild=[]
match_pos_mutant=[]
for i in variants_pos:
    a=int(i[1])
    #print(a)
    for j in epipara:
        b=int(j[2])
        #print(b)
        if a==b:
            match_pos_mutant.append([j+list(i[2])])
            match_pos_wild.append([j+list(i[0])])

# flatten the nested lists
match_pos_wld=(list(itertools.chain.from_iterable(match_pos_wild)))
match_pos_mut=(list(itertools.chain.from_iterable(match_pos_mutant)))


# Preserve the order of the matched postions
interact_mut=(list(map(list, OrderedDict.fromkeys(map(tuple, match_pos_mut)).keys())))
interact_wld=(list(map(list, OrderedDict.fromkeys(map(tuple, match_pos_wld)).keys())))

# function for converting list to string as input for interaction2.js command 
def listToString(ls):
    strg = " "
    return (strg.join(ls))

for w, m in zip(interact_wld, interact_mut):
    print((listToString(w)),(listToString(m)), sep="\n")
