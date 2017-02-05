The program  calculates the second moment (F2) of a stream as described on page 146:
http://infolab.stanford.edu/~ullman/mmds/ch4.pdf

It consists of three files: 
	- the main script main_F2_calculations.py 
	- module stream_processing.py
			calculates exact F1 and F2 smoments.
	- approximate_F2_function.py
			calculates approximate F2

Python 3 required.

The main script can be run from the command line as 

	$python twitter_file

where twitter_file is a text file where each line contains one word from a tweet.
The initial parameters can be changes inside the main_F2_calculations.py.

x_parameters: the number of samples taken from set
[size_of_the_first_subset, size_of_the_last_subset, step]

y_parameters: the number of times s1 is generated
[smallest_number_largest_number, step]

Output

The result of the program is a file 'results' in the folder named after date/time of program execution, containing:
	- the set of all parameters used in the run
	- approximate F2 and difference in percentage with the exact F2 for 
	all the parameter combinations specified in the program.

Example:
X: 2000 5000 2000
Y: 2 5 2

Y = 2
X = 2000
Approximate F2 = 20727701.0
Difference with exact F2 10.39 %

X = 4000
Approximate F2 = 20592816.5
Difference with exact F2 10.98 %

Y = 4
X = 2000
Approximate F2 = 21564559.0
Difference with exact F2 6.78 %

X = 4000
Approximate F2 = 23178122.5
Difference with exact F2 0.20 %

X means that the program used different number of samples: 2000 and 4000 (from 2000 to 5000 with step 2000).
Y means that on each sample programe was run 2 and 4 times (from 2 to 5 with step 2).