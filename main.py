import sys
from animation import *
import random;

import config
from Problem import *
from Fringe import *
from ClosedList import *
from graph_search import *
from SearchNode import *
from grid import *

def string_to_mat(string, size):
    ret = []
    a = string.split(",")
    place = 0
    inner = []
    for i in a:
        inner.append(i)
        place += 1
        if place == size:
            ret.append(inner)
            place = 0
            inner = []
    return ret

def get_init_state(string, size):
    row = 0
    col = 0
    for i in range(len(string)):
        if string[i] == ' ':
            return (row, col)
        if string[i] == ',':
            col += 1
            if col == size:
                col = 0
                row += 1

size = int(input("Size: "))
initial = input("initial: ")
initState = get_init_state(initial, size)
search = input("bfs or dfs or iddfs: ")
grid = Grid(size)


#===========================================================
# TODO: Compute solution using graph search.
# Select the correct fringe object.
#===========================================================
problem = nProblem(size=size,
                   initial_state=initial,
                   grid=grid)
startNode = SearchNode((initState, initial))

if search == 'bfs':
    fringe = FSQueue()
elif search == 'dfs' or search == 'iddfs':
    fringe = FSStack()
else:
    raise Exception('invalid search')

print("close animation window to halt", flush=True)
closed_list = SetClosedList()
#Returns the solution node
solution = graph_search(problem=problem,
                        Node = startNode,
                        fringe=fringe,
                        closed_list=closed_list,
)

#==============================================================================
# DO NOT CHANGE ANYTHING IN THIS SECTION.
#==============================================================================
if solution == None:
    print("solution = None")
    while 1:
        view0.run()
else:
    print("solution: %s" % solution)
    print("len(solution): %s" % len(solution))
    print("len(closed_list): %s" % len(closed_list))
    print("len(fringe): %s" % len(fringe))

    # Compute path from solution for drawing.
    path = []
    for node in solution:
        
        if node.parent_action != None:
            path.append(node.parent_action)
        
        print("path: %s" % path)

    draw(string_to_mat(initial, size), path)
