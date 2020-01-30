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
        

    


def compare_lists(names_l, num_thread, num_threads):


   
    nnn = len(names_l)

    all_names_scores = {}


    for ind, n1 in enumerate(names_l):
        for n2 in names_l:

            print(ind+1, '/', nnn, '\t\t', num_thread+1, '/', num_thread)

            if n1 != n2:
                fuzzy = fuzz.ratio(n1, n2)

                if n1 not in all_names_scores:
                    all_names_scores[n1] = []
                if n2 not in all_names_scores:
                    all_names_scores[n2] = []

                all_names_scores[n1].append(fuzzy)
                all_names_scores[n2].append(fuzzy)


    fout = open('similarities/names_scores_' + str(num_thread) + '.dat', 'w')
    for name, scores in all_names_scores.items():
        fout.write(name + '\t\t' + '\t'.join([str(s) for s in scores]) + '\n')
    fout.close()



all_names = list(set([line.strip().split('\t')[1] for line in open('cleaning_steps/step6.csv')]))
print(len(all_names))


foldout = 'similarities'
if not os.path.exists(foldout):
    os.makedirs(foldout)


    
num_threads = 50
name_chunks = chunkIt(all_names, num_threads)
Pros        = []



for ind, chunk in enumerate(name_chunks):
    p = Process(target = compare_lists, args=(chunk, ind, num_threads,))
    Pros.append(p)
    p.start()
   
for t in Pros:
    t.join()


all_names_scores = {}
fout  = open('similarities/COMBINED_scores.dat', 'w')
files = [f for f in  os.listdir('similarities') if 'COMBINED' not in f]

for fn in files:
    for line in open('similarities/' + fn):
        name, scores = line.strip().split('\t\t')
        scores = [int(s) for s in scores.split('\t')]

        if name not in all_names_scores:
            all_names_scores[name] = []
        all_names_scores[name] += scores 



for n, s in all_names_scores.items():
    fout.write(n +  '\t\t' + '\t'.join([str(_) for _ in  sorted(s, reverse = True)[0:50]]) + '\n')
fout.close()







