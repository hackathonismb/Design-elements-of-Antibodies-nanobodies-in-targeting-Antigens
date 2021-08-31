import sys
import glob

file1= sys.argv[1] # output from molsen_change_indv_interact_count_analysis.py or molsen_change_sum_interact_count_analysis.py
eph = open(file1.strip(),"r")
#z=fh.readline()

from collections import Counter
def remove(string):
    return string.replace(" ", "") # remove the white space
# frequency of the interactions
count=[]
for line in eph:
    a=line.strip()
    b=remove(a)
    count.append(b)
#print(count)
mut=Counter(count)
print(mut)