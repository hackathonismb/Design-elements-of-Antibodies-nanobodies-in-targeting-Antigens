import sys
import glob

# https://github.com/ncbi/icn3d/tree/master/icn3dnode
# https://github.com/ncbi/icn3d/blob/master/icn3dnode/interaction2.js
file1= sys.argv[1] # output from the interaction2.js having the change in the relative interactions due to mutation compared to wild type based on epitopes-paratopes information from PDB
eph = open(file1.strip(),"r")
#z=fh.readline()

# the relative change in interaction based on individual interaction
count_hbond=[] # change in H-bond
count_ionic=[] # change in ionic interaction
count_contact=[] # change in contact
count_halogen=[] # change in halogen interaction
count_pication=[] # change in pication interaction
count_pistacking=[] # change in pistacking interaction

epipara=[]
for line in eph:
    #print(line)
    line=line.strip().split(",")
    if line[3] == line[4]:
        a_hbond=int(line[5])
        #print("wild_hbond"+"="+str(a_hbond))
        a_ionic=int(line[6])
        #print("wild_ionic"+"="+str(a_ionic))
        a_contact=int(line[7])
        #print("wild_contact"+"="+str(a_contact))
        a_halogen=int(line[8])
        #print("halogen"+"="+str(a_halogen))
        a_pication=int(line[9])
        #print("pication"+"="+str(a_pication))
        a_pistacking=int(line[10])
        #print("pistacking"+"="+str(a_pistacking))
    if line[3] != line[4]:
        b_hbond=int(line[5])
        #print("mutant_hbond"+"="+str(b_hbond))
        b_ionic=int(line[6])
        #print("mutant_ionic"+"="+str(b_ionic))
        b_contact=int(line[7])
        #print("mutant_contact"+"="+str(b_contact))
        b_halogen=int(line[8])
        #print("mutant_halogen"+"="+str(b_halogen))
        b_pication=int(line[9])
        #print("mutant_pication"+"="+str(b_pication))
        b_pistacking=int(line[10])
        #print("mutant_pistacking"+"="+str(b_pistacking))
        if a_hbond == b_hbond:
            count_hbond.append("no_change_Hbond"+line[3]+line[2]+line[4])
        if a_hbond > b_hbond:
            count_hbond.append("decrease_Hbond"+line[3]+line[2]+line[4])
        if a_hbond < b_hbond:
            count_hbond.append("increase_Hbond" +line[3]+line[2]+line[4])
        if a_ionic == a_ionic:
            count_ionic.append("no_change_ionic"+line[3]+line[2]+line[4])
        if a_ionic > b_ionic:
            count_ionic.append("decrease_ionic"+line[3]+line[2]+line[4])
        if a_ionic < b_ionic:
            count_ionic.append("increase_ionic" +line[3]+line[2]+line[4])
        if a_contact == b_contact:
            count_contact.append("no_change_contact"+line[3]+line[2]+line[4])
        if a_contact > b_contact:
            count_contact.append("decrease_contact"+line[3]+line[2]+line[4])
        if a_contact < b_contact:
            count_contact.append("increase_contact" +line[3]+line[2]+line[4])
        if a_halogen == b_halogen:
            count_halogen.append("no_change_halogen"+line[3]+line[2]+line[4])
        if a_halogen > b_halogen:
            count_halogen.append("decrease_halogen"+line[3]+line[2]+line[4])
        if a_halogen < b_halogen:
            count_halogen.append("increase_halogen" +line[3]+line[2]+line[4])
        if a_pication == b_pication:
            count_pication.append("no_change_pication"+line[3]+line[2]+line[4])
        if a_pication > b_pication:
            count_pication.append("decrease_pication"+line[3]+line[2]+line[4])
        if a_pication < b_pication:
            count_pication.append("increase_pication" +line[3]+line[2]+line[4])
        if a_pistacking == b_pistacking:
            count_pistacking.append("no_change_pistacking"+line[3]+line[2]+line[4])
        if a_pistacking > b_pistacking:
            count_pistacking.append("decrease_pistacking"+line[3]+line[2]+line[4])
        if a_pistacking < b_pistacking:
            count_pistacking.append("increase_pistacking" +line[3]+line[2]+line[4])

#print(count_hbond)
#print(count_ionic)
#print(count_contact)
#print(count_halogen)
#print(count_pication)
#print(count_pistacking)
#print(epipara)

# count for the relative change in interaction based on individual interaction
def listToString(ls):
    strg = " "
    return (strg.join(ls))

for w in count_hbond:
    print(listToString(w),sep="\n")
for w in count_ionic:
    print(listToString(w),sep="\n")
for w in count_contact:
    print(listToString(w),sep="\n")
for w in count_halogen:
    print(listToString(w),sep="\n")
for w in count_pication:
    print(listToString(w),sep="\n")
for w in count_pistacking:
    print(listToString(w),sep="\n")