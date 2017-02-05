
'''Helper functions for tsp_simulated_annealing script'''

import copy
import random
import math

import numpy as np
import matplotlib.pyplot as plt 

def tour_cost(permuted_list, distance_matrix):
    '''Calculation of the cost of a given tour.
	
    Parameters: 
    -----------
    permuted_list: array_like (int)
        numpy 1D array representing a tour
		
    distance_matrix: array_like (float, ndim=2)
        Distance matrix between all points 
		
	Returns:
	--------
	distance_cost(float): 
		A distance cost of the whole tour
		
	'''

    number_of_points = len(permuted_list)
    distance_cost = 0

    for point in range(number_of_points-1):
        dist_ij = distance_matrix[permuted_list[point],permuted_list[point+1]]
        distance_cost = distance_cost + dist_ij

    dist_last0 = distance_matrix[permuted_list[point+1],permuted_list[0]]
    distance_cost=distance_cost + dist_last0
    
    return distance_cost


def find_candidate_solution (initial_list, num_of_changes): 
    '''Generation of neighbouring solution
	
	Parameters: 
	-----------
	initial_list: array_like (int)
		numpy 1D array representing initial tour
		
	num_of_changes: scalar(int)
		the number of edges which should be flipped
		in the initial tour
	
	Returns:
	--------
	permutation_list: array_like (int)
		new tour different from the initial one
	
    '''

    permutation_list = copy.deepcopy(initial_list)
    list_size = len(permutation_list)

    #choose randomly num_of_changes*2 indices
    random_cities = random.sample(range(0,list_size),num_of_changes*2)

    #flip element positions one by one
    one_change = 0;
    while one_change < num_of_changes:
        a = permutation_list[random_cities[one_change]]
        permutation_list[random_cities[one_change]] = permutation_list[random_cities[one_change+1]]
        permutation_list[random_cities[one_change+1]] = a
        one_change = one_change + 2;

    return permutation_list   


def plot_tour(permutation, coordinates,res_name):
    '''Plotting of the given tour. Saves the image as .png
	
	Parameters:
	-----------
	permutation: array_like (int)
		numpy 1D array representing a tour
		
	coordinates: 
		a list of x-y coordinates
	res_name: str
		a name of the file .png
	
	'''

    permuteX = [coordinates[i,0] for i in permutation]
    permuteY = [coordinates[i,1] for i in permutation]
    
    #blue lines between points
    plt.plot(permuteX,permuteY)
    plt.plot([permuteX[-1], permuteX[0]], [permuteY[-1], permuteY[0]], color ='b')  #connects last and the first points
    #points are colored with red
    plt.plot(permuteX,permuteY, '.',color ='r')    
    plt.savefig(res_name + ".png")
    
    #plt.show()  #uncomment for obtaining a plot during the program execution


def initial_tour_shortest_distance(distance_matrix):
    '''The function finds the initial solution for SA algorithm
	Two closest points are found. They are starting points in the tour. 
	Then the program takes the second point and find the closets one to that point. 
	The point is appended to the end of the tour. 
    The procedure continues till the last point. 
	
	Parameters: 
	-----------
	distance_matrix: array_like(float, ndim=2)
		Distance matrix between all points
		
	Returns:
	--------
	tour: array_like(int)
		numpy 1D array representing a tour
		
	'''
    
    tour = [];
    
    #infinity on the diagonal
    for j in range (len (distance_matrix)):        
        distance_matrix[j][j] = float("inf")

    #find two closest points and add them to a tour
    min_index = np.unravel_index(distance_matrix.argmin(), distance_matrix.shape)
    tour.append(min_index[0])
    tour.append(min_index[1])
    
    #convert to infinity values for the first point both in rows and columns
    for i in range(len(distance_matrix)):
        distance_matrix[min_index[0]][i] = float("inf")
    for k in range(len(distance_matrix)):
            distance_matrix[k][min_index[0]] = float("inf")

    # find the closest points to the last point in the tour and add it to the end of the tour
    # The procedure continues till the last point is added.
    for points in range (2,len(distance_matrix)):
        min_dist = np.argmin(distance_matrix[tour[-1],:])
        for i in range(len(distance_matrix)):
            distance_matrix[tour[-1]][i] = float("inf")
        for k in range(len(distance_matrix)):
            distance_matrix[k][tour[-1]] = float("inf")

        tour.append(min_dist)
    return tour


def simulated_annealing(Tinit, alpha, Tfinal, L, num_of_changes,dists):
	'''The function runs the simulated annealing algorithm designed for TSP
	
	Parameters:
	-----------
	Tinit: scalar(float) 
		the initial temperature
	
	alpha: scalar(float)
		a speed rate
	
	Tfinal: scalar(float) 
		final temperature when algorithm terminates
	
	L: scalar(int)
		the number of sweeps
	
	num_of_changes: scalar(int)
		the number of edges in tour which should be replaced
		in a neighbour solution
		
	Returns:
	--------
	best_cost: scalar(float)
		the cost of the best tour
	
	best_solution: array_like(int)
		a tour with the best cost

    initial_cost: scalar(float)
        the cost of the initial tour
	
	'''
	
	T = Tinit
	distance_matrix = copy.deepcopy(dists)
	first_solution = initial_tour_shortest_distance(distance_matrix)
	best_solution = copy.deepcopy(first_solution)
	initial_solution = copy.deepcopy(first_solution)
	initial_cost = tour_cost(initial_solution,dists)

	first_cost = initial_cost
	best_cost = initial_cost
	current_cost = initial_cost
	print('Initial cost:')
	print(initial_cost)

	iterations = 0
	while T > Tfinal:
		for times in range(L):
			candidate_solution = find_candidate_solution(initial_solution,num_of_changes)
			candidate_cost = tour_cost(candidate_solution,dists)
			delta = candidate_cost - initial_cost

			if delta < 0:
				initial_cost = candidate_cost
				initial_solution = copy.deepcopy(candidate_solution)          
			else:
				r = random.random()
				if r <= math.exp(-delta/T):
					initial_cost = candidate_cost
					initial_solution = copy.deepcopy(candidate_solution)               

			if initial_cost < best_cost:
				best_solution = copy.deepcopy(initial_solution)
				best_cost = initial_cost

		T = alpha*T
		if iterations%50 == 0:
			print("\nIteration: " + str(iterations))
			print('Best cost:', str('%.2f' %best_cost))
		iterations = iterations + 1
		
	return best_cost, best_solution, initial_cost
