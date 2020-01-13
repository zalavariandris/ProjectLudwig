import gzip
import os
import json
import re
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from multiprocessing import Process
import time
import sys




def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out
        

    

def compare_names(name1, name2, filename):
    

    fuzzy = fuzz.ratio(name1, name2)

    if fuzzy > 64:
        fout = open(filename, 'a')
        #fout.write(name1 + '\t' + name2 + '\t' + str(jacc) + '\t' + str(whos) + '\t' + str(fuzzy) + '\n')
        fout.write(name1 + '\t' + name2 + '\t' + str(fuzzy) + '\n')
        fout.close()



def compare_lists(names_l, num_thread, num_threads):



    fout = open(foldout + '/artist_names_matched_' + str(num_thread) + '.dat', 'w')
    fout.write('name1\tname2\tsimilarity\n')
   
    nnn = len(names_l)


    for ind, n1 in enumerate(names_l):
        for n2 in names_l:

            print(ind+1, '/', nnn, '\t\t', num_thread+1, '/', num_thread)

            if n1 != n2:
                fuzzy = fuzz.ratio(n1, n2)
                if fuzzy > 60:
                    fout.write(n1 + '\t' + n2 + '\t' + str(fuzzy) + '\n')

    fout.close()





all_names = [line.strip().split('\t')[0] for line in open('extracted/all_artists_cleaned_stage1.dat')]

print(len(all_names))


foldout = 'name_matching'
if not os.path.exists(foldout):
    os.makedirs(foldout)


    
num_threads = 3
name_chunks = chunkIt(all_names, num_threads)
Pros        = []



for ind, chunk in enumerate(name_chunks):
    p = Process(target = compare_lists, args=(chunk, ind, num_threads,))
    Pros.append(p)
    p.start()
   
for t in Pros:
    t.join()



