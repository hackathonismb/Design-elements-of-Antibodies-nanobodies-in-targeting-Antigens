import sys
import glob

from Bio.PDB import * # Biopython PDB module
parser = PDBParser(QUIET=True)
#parser = PDBParser(PERMISSIVE=1)
# Automated PDBs download using shell script from https://www.rcsb.org/docs/programmatic-access/batch-downloads-with-shell-script
# ./batch_download.sh -f pdb_list_file.txt -p
file1= sys.argv[1] # PDB input file 6ZER, 6XC2, 6XC4,..used for molsen* script
eph = open(file1.strip(),"r")
#z=fh.readline()
#structure=parser.get_structure("example", '6ZER.pdb')
#model = structure.get_models()
#models = list(model)
#chains = list(models[0].get_chains())
#print(structure.header["compound"])
#print(chains)
pdb_sars=[]
for pdb in eph:
    #fname = pdb.split(pdb=",")
    a=pdb.strip().split(",")
    for j in a:
        b=j.strip().split(",")
        #print(b)
        pdb_sars.append(b)
#print(pdb_sars)
flat_list = [item for sublist in pdb_sars for item in sublist]
string=".pdb"
output = ["{}{}".format(i,string) for i in flat_list]

for i in output:
    j=i.strip().split(".")
    #print(i)
    structure=parser.get_structure("example", i)
    model = structure.get_models()
    models = list(model)
    #chains = list(models[0].get_chains())
    #print(structure.header["compound"])
    #print(chains,i)
    #print(i,structure.header["compound"]["1"]["chain"][0], structure.header["compound"]["2"]["chain"][0], structure.header["compound"]["3"]["chain"][0])
    
    print(i,structure.header["compound"])
    print(j[0],structure.header["compound"]["1"]["chain"][0].upper(), structure.header["compound"]["2"]["chain"][0].upper(), structure.header["compound"]["3"]["chain"][0].upper())
