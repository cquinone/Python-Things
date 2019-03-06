import numpy as np
import random as rand
from collections import defaultdict

class Graph():
	def __init__(self):
		self.graph = defaultdict(list) #sets kind to add (if no key exists) as list
	
	def addEdge(self,u,v): 
		self.graph[u].append(v)

	def connections(self,coord):
		return self.graph[coord]
  
def gen_graph(N,grid):
	#generate directed graph for grid of size NxN
	g = Graph()
	for i in range(N):
		for j in range(N):
			#look at only adjacent cells, and add connections where those cells are in the same state!
			if i > 0:
				if grid[i,j] == grid[i-1,j]:
					g.addEdge((i,j),(i-1,j))
			if i < N-1:
				if grid[i,j] == grid[i+1,j]:
					g.addEdge((i,j),(i+1,j))
			if j > 0:
				if grid[i,j] == grid[i,j-1]:
					g.addEdge((i,j),(i,j-1))
			if j < N-1:
				if grid[i,j] == grid[i,j+1]:
					g.addEdge((i,j),(i,j+1))
	return g

def search_adj(i,j,visited,grid_graph):
	#use i,j and depth first search for region from given cell, return visited updated from search
	visited[i,j] = True #we've visited this point now
	for point in grid_graph.connections((i,j)):
		k = point[0]
		l = point[1]
		if visited[k,l] == False:
			search_adj(k,l,visited,grid_graph)
	return visited

def avg_area(gen_binary,N):
	# find # of regions 
	# copy grid size, then make grid set to false for all cells
	# check first cell, find all adjacent similar cells, mark each on other matrix as false
	# add 1 to count, continue, skipping any cell that is True as visited in other matrix
	# count is # of regions, divide by over N^2 for average size
	region_avg = 0
	for curr_grid in gen_binary:
		#constuct graph for DFS here, it depends on N but also on actual given grid!
		grid_graph = gen_graph(N,curr_grid)
		region_count = 0
		visited = np.full((len(curr_grid),len(curr_grid)),False,dtype=bool)
		for i in range(len(curr_grid)):
			for j in range(len(curr_grid)):
				if visited[i,j] == False:  #haven't been here yet					
					region_count = region_count+1 #? add for each new region -> should be only when you hit unvisited spots
					visited = search_adj(i,j,visited,grid_graph) #search here through all connected ones, update visited
		region_avg = region_avg + ((N**2)/region_count)
	region_avg = region_avg/float(max_gen)
	return region_avg

np.set_printoptions(threshold=np.nan)
max_gen = 1000 #how many to generate per N 
size = 50 #how high you want to go in dimension
areas = []
for N in range(2,size+1):
	print "N:", N
	gen_binary = [] 
	while len(gen_binary) < max_gen: #keep generating
		grid = np.zeros((N,N))
		for i in range(N):
			for j in range(N):
				grid[i,j] = rand.randint(0,1)
		gen_binary.append(grid)
	avg = avg_area(gen_binary,N)	#here, calc avg size of area in all the grid in gen_binary (so avg area for given N!) 
	areas.append((avg,N))

print areas