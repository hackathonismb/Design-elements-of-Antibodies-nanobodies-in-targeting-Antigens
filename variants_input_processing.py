import sys
import glob

file1= sys.argv[1] # variant input file used for molsen* script
eph = open(file1.strip(),"r")
#z=fh.readline()

count2=[]
count=[]
for line in eph:
    a=line.strip().split(",")
    count.append(a[0])
    count2.append(a)
#print(count)

count_set=set(count)
#print(len(count_set))
print("Nextstrain_unq_mut_var")
for i in count_set:
    print(i)

from collections import Counter
mut=Counter(count)
#print(len(mut), mut)
#print(len(count))