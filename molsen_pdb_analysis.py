import sys
import glob
file1= sys.argv[1] # output from the epitope.js having epitopes-paratopes information from PDB
eph = open(file1.strip(),"r")
#z=fh.readline()

# Processing pdb_epitopes_paratopes file from epitope.js command

epipara=[]
for line in eph:
    line=line.strip().split(",")
   # print(line)
    pdb=line[1].strip().split("_")
    epipara.append([pdb[0],pdb[1],line[2].strip()])
#print(epipara)

#For identifying the antibody-targeting region of SARS-Cov-2 spike protein (S1, 14–685 residues)

ntd=[] # NTD loop (amino terminal domain, 13-303 amino acid residue)
rbd=[] # RBD (Receptor binding domain, 319-541)

for i,data in enumerate(epipara):
    if i == len(epipara)-1:
        a=data[2]
        if int(a)<=303:
            ntd.append([data[0],data[2]])
        if int(a)>303:
             rbd.append([data[0],data[2]])

print(ntd)
print(rbd)