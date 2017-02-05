
The program  executes simulated annealing algorithm for travelling salesman problem (TSP). 
It consists of two files: 
	- the main script tsa_simulated_annealing.py 
	- library tsa_library.py. 

Dependences required: Python 3, libraries numpy, scipy and matplotlib. 

The main script can be run from the command line as 

	$python tsp_simulated_annealing.py inputfile.tsp

where format of inputfile.tsp is described at http://www.math.uwaterloo.ca/tsp/data/

It can be run with the sample file as: 
	
	$python tsp_simulated_annealing.py wi29.tsp


Output

The result of the program are two files in the folder '[inputfile]_dir' (derived from the input file name).
All the results from different runs related to the same input file are written to the same folder. 
The output files are:
 [datetime]_[inpufile].txt  -  the information about  initial parameters, cost of initial solution, cost of 
 the best found solution, the best solution as the permuted sequence and the running time.
 [datetime]_[inpufile].png - image of the best found tour.

Example:
 Script run on 25th of May at 13.53 on inputfile wi29.tsp.
 Generated files: wi29/20.5_13.53_wi29.tsp.txt and wi29/20.5_13.53_wi29.tsp.png
 

 