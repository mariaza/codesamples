'''The script contains a function calculating 
the exact values for the first moment F1 (the length of the stream)
the second moment F2.

'''
import time
from functools import reduce


def exact_F1_F2(filename):
    '''Calculations of F1 and F2

    Parameters:
    -----------
    filename: text file
        a file with a stream where one line
        is a one word from tweets

    Returns:
    --------
    F1: scalar(int)
        the first moment (the length of a stream)

    F2: scalar(int)
        the second moment
    '''

    i = 0
    removed_lines = 0
    counts = dict()
    start_time = time.time()
  
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            i = i + 1       
  
            try:
                word = line        
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1

            except IndexError :
                removed_lines = removed_lines + 1
                pass

    li = list(counts.values())

    F1 = reduce((lambda x,y:x + y), li)
    print('F1 (number of all elements) = ', F1)

    squared = map((lambda x: x ** 2), li)
    F2 = reduce((lambda x,y:x + y), squared)
    print('F2 (second moment) = ',F2)
    print('Removed lines = ', removed_lines)
    print('Number of lines = ',i)
    return F1, F2