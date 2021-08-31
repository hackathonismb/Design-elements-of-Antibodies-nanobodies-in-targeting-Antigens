import sys
import glob

# https://github.com/ncbi/icn3d/tree/master/icn3dnode
# https://github.com/ncbi/icn3d/blob/master/icn3dnode/interaction2.js
file1= sys.argv[1] # output from the interaction2.js having the change in the relative interactions due to mutation compared to wild type based on epitopes-paratopes information from PDB
eph = open(file1.strip(),"r")
#z=fh.readline()

# the relative change in interaction based on sum of interactions (Change Hbond +Change Ionic +Change Contact+Change Halogen+Change Pi-Cation+Change Pi-Stacking)
count=[]
epipara=[]
for line in eph:
    print(line)
    line=line.strip().split(",")
    if line[3] == line[4]:
        a=int(line[5])+int(line[6])+int(line[7])+int(line[8])+int(line[9])+int(line[10])
        print("wild"+"="+str(a))
    if line[3] != line[4]:
        b=int(line[5])+int(line[6])+int(line[7])+int(line[8])+int(line[9])+int(line[10])
        print("mutant"+"="+str(b))
        if a == b:
            count.append("no_change"+line[3]+line[2]+line[4])
        if a > b:
            count.append("decrease"+line[3]+line[2]+line[4])
        if a < b:
            count.append("increase" +line[3]+line[2]+line[4])

print(count)