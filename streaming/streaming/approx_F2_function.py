import sys
import random 
import statistics
from functools import reduce


def f2_mod(Y, X, n, text_file):
    ''' Calculation of the second moment of stream for a tweeter file
    as described on page 146 http://infolab.stanford.edu/~ullman/mmds/ch4.pdf

    Parameters:
    -----------
    Y: scalar(int)
        the number of times a subset is taken from the whole line in a file

    X: scalar(int)
        the number of lines should be sampled from the file

    n: scalar(int)
        the number of lines in the file

    text_file: txt file
        a file where each line presenting a word from a tweet

    Returns:
    --------
    Ymedian: scalar(float)
        an approximate value of the second moment of a stream (F2)

    '''
    random.seed(573)
    y_list = [0] * Y
    for i in range(Y):
        print('\nSubset: ', i + 1)
        lines_with_counts = dict() #dictionary with lines from file and how many times
                                   #the line is observed by the moment
        
        #take X number of indeces randomly
        random_indexes_of_all_lines = sorted([random.randrange(n) for i in range(X)])

        ind = 0 # index of line
        index_of_random_indeces = 0

        index_of_last_index = len(random_indexes_of_all_lines) - 1

        with open(text_file, "r", encoding="utf-8") as f:
            for line in f:                               
                line_in_dictionary = lines_with_counts.get(line)
                                      
                if ind % 10000 == 0:
                    print('Processing line : ', ind)

                while ind == random_indexes_of_all_lines[index_of_random_indeces]:            
                    if line_in_dictionary:
                        lines_with_counts[line].append(0)                   
                    else:
                        lines_with_counts[line] = [0]
                        line_in_dictionary = True
                                
                    if index_of_random_indeces < index_of_last_index:
                        index_of_random_indeces += 1                   
                    else: break
        
                if line_in_dictionary:          
                    lines_with_counts[line] = [item + 1 for item in lines_with_counts[line]]
          
                ind += 1       

            values_list = list(lines_with_counts.values())
            flattened_values = [item for sublist in values_list for item in sublist]
            f2array = map((lambda x: n * (2 * x - 1)), flattened_values)
            f2average = round(reduce((lambda x,y:x + y), f2array) / X)
            y_list[i] = f2average

    Ymedian = statistics.median(y_list)
    
    return Ymedian
