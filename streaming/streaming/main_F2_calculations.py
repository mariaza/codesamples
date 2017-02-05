'''The script calculates the approximate value of F2 (the second moment)
of the stream as described in page 146 in http://infolab.stanford.edu/~ullman/mmds/ch4.pdf

F2 shows how uneven is distribution in the stream.

If there is n distinct words,
let c1, c2, c3, ..., cn be the number of counts those distinct words in the stream.

Then F2 is calculated as follows:

c1^2 + c2^2 + c3^2 + ... + cn

For huge streams (billions of tweets) it is impossible to calculate
F2 as there is a need for storing all the distinct words and their counts.

The approximate calculations of F2 allows calculating it with the
limited space but the relatively high estimation. 

The script can be run from a command line as follows:

    $python twitter_file

    where twitter_file is a text file where each line contains one word from a tweet.


'''

import time
import os.path
import sys
import random 
from datetime import datetime

from approx_F2_function import f2_mod
from stream_processing import exact_F1_F2

random.seed(573)
file_name = sys.argv[1]

#parameters

#x_parameters: the number of samples taken from set
#[size_of_the_first_subset, size_of_the_last_subset, step]
x_parameters = [2000,5000,1000]

#y_parameters: the number of times s1 is generated
#[smallest_number_largest_number, step]
y_parameters = [2,5,1]


d = datetime.now()
date_time = str(d.day) + '.' + str(d.month) + '_' + str(d.hour) + '.' + str(d.minute)

# exact values of F1 and F2 moments
exact_F1, exact_F2 = exact_F1_F2(file_name)

n = exact_F1
x_first = x_parameters[0]
x_last = x_parameters[1]
x_step = x_parameters[2]

y_first = y_parameters[0]
y_last = y_parameters[1]
y_step = y_parameters[2]

folder_to_store_Y = date_time + "/"

if not os.path.exists(folder_to_store_Y):
    os.makedirs(folder_to_store_Y)

write_result = open(folder_to_store_Y + "results.txt","w")
write_result.write("X: " + ' '.join(map(str,x_parameters)) + "\n" + "Y: " + ' '.join(map(str,y_parameters)) + '\n')


for i in range(y_first, y_last + 1, y_step):   
    write_result.write("\nY = " + str(i))  
    start_time = time.time()

    for j in range(x_first, x_last + 1, x_step):  
        print("\nX = ", j, "Y(number of subsets) = ", i, "\n")
        write_result.write("\nX = " + str(j))

        #aproximate calculations of F2
        approx_F2 = f2_mod(i, j, n,file_name)
        #difference between exact and approximate F2 in percentage
        difference = abs(100 - (100 * approx_F2 / exact_F2))

        current_time = time.time()
        spent_time = current_time - start_time
        start_time = current_time
        print('\nFor X = ' + str(j) + ' Y = ' + str(i) + " Time spent: " + str('%.2f' % spent_time) + " sec")      
        write_result.write("\nApproximate F2 = " + str(approx_F2) + "\n")
        print("\nApproximate F2 over Y subsets: ", approx_F2)
        print("Exact F2: ", exact_F2)        
        print("Approximate F2 differs from exact F2 in " + str('%.2f' % difference) + " %")
        write_result.write("Difference with exact F2 " + str('%.2f' % difference) + " %\n")
        print("\n===================================\n")
        write_result.flush()
   
write_result.close()