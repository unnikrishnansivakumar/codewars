from collections import Counter
from itertools import chain

def pos_average(s):
    count=0
    count_loop=0
    substrings = [list(enumerate(i)) for i in s.split(", ")]    
    for i in range(len(substrings)):
        for j in range(i+1,len(substrings)):
            count_loop+=1
            if i!=j:
                count+=len(set(substrings[i])&set(substrings[j]))
    pos_avg =count/(len(substrings[0])*count_loop)
    return pos_avg      
    