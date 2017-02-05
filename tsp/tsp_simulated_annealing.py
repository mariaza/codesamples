#!/usr/bin/env python

'''Main script for simulated annealing algorithm for the travelling
salesman problem. Run from the command line as
 
	$python tsp_simulated_annealing.py inputfile.tsp
	
where inputfile.tsp is the file in the format as in 
http://www.math.uwaterloo.ca/tsp/data/

Dependences: numpy, scipy, matplotlib  

'''

import sys
import random
import math
import copy
import time
import os.path
from datetime import datetime

import numpy as np
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt 

from tsp_library import *

start_time = time.time()
random.seed(20)

#parameters
t_init = 1000
alpha = 0.99
t_final = 0.001
L = 30
num_of_changes = 2

# get the current time (for estimation the running time)
d=datetime.now()
date_time=str(d.day)+'.'+str(d.month)+'_'+str(d.hour)+'.'+str(d.minute)

file_name = sys.argv[1] 

#name of the folder for storing all the results related to inputfile.tsp
folder_to_store = file_name +'_dir/'
file_object = open(file_name, 'r')
list_of_lines = []
for line in file_object:
    list_of_lines.append(line)
ind = [ i for i, word in enumerate(list_of_lines) if word.startswith('NODE_COORD_SECTION') ]

#extract the information with the coordinates as strings
filtered_list = list_of_lines[ind[0]+1:-1] #omit the last line with EOF

#split lines and convert coordinates to float
coordinates_table = []
for line in filtered_list:
    new_line=line.strip().split()
    coordinates_table.append(new_line[1:])

coordinates_table=[[float(y) for y in x] for x in coordinates_table]
coordinates_table = np.array(coordinates_table)

#distance matrix
dists = (ssd.squareform(ssd.pdist(coordinates_table, 'euclidean')))
number_of_points = dists.shape[1]

#simulated annealing algorithm
best_cost, best_solution, initial_cost = simulated_annealing(t_init, alpha, t_final, L, num_of_changes, dists)  

#running time of the algorithm
current_time = time.time()
spent_time = current_time - start_time

res_path  = folder_to_store + date_time + "_" + file_name

res_name = res_path + ".txt"

#create a folder if the folder does not exist
if not os.path.exists(folder_to_store):
    os.makedirs(folder_to_store)

writeResults=open(res_name,"w")
writeResults.write("t_init = " +  str(t_init)+" t_final = " + str(t_final) + \
" alpha = " + str(alpha) + " L = " + str(L) + " num_of_changes = " + str(num_of_changes) + "\n")
writeResults.write("Initial cost: " + str('%.2f' %initial_cost) +"\n")
writeResults.write("Best cost: " + str('%.2f' %best_cost) +"\n")
writeResults.write("\t".join(str(x) for x in best_solution)+"\n") #best found tour
writeResults.write("Time spent: " + str('%.2f' %spent_time) + ' sec')
writeResults.close()
print('\n\nThe cost of the best found tour:', str('%.2f' %best_cost))


#save the plot of the best found tour
plt.figure(1)
plot_tour(best_solution, coordinates_table,res_path)