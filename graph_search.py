import random
from SearchNode import SearchNode
import collections
import math

#==============================================================================
# GRAPH_SEARCH
#
# The fringe and closed list must be drawn while the thinking takes place.
# - Draw the closed list blue (255, 0, 0).
# - Draw the fringe in green (0, 255, 0).
#
# There must be NO console printing in this python file. Make sure you remove
# them or comment them out when you are done.
#==============================================================================
def swap(str, i, j):
   list1 = list(str)
   list1[i], list1[j] = list1[j], list1[i]
   return ''.join(list1)

def intify(it):
    ret = 0
    for i in range(len(it)):
        if it[i] == ',':
            continue
        ret *= 10
        if it[i] != ' ':
            ret += int(it[i]) + 1
        i += 1
    return ret

def sizeOf(it):
    #print("Intify: ",it)
    running = -1
    s = str(it)
    for i in range(len(s)):
        if int(s[i]) > running:
            running = int(s[i])
    return int(math.sqrt(running + 2))
        

def process(state, loc, action, size):
    (r0, c0) = loc
    #print(r0, " ", c0)
    #print("Value: ", state[2 * size * r0 + 2 * c0])
    row = 2 * size * r0
    col = c0 * 2

    if action == 'N':
        r1 = row - 2
        c1 = col
        #t = state[row + col]
        #state[row + col] = state[r1 + c1]
        #state[r1 + c1] = t
        return ((r1, c1),swap(state, (row + col), (r1 + c1)))
    elif action == 'S':
        r1 = row + 2
        c1 = col
        #t = state[row + col]
        #state[row + col] = state[r1 + c1]
        #state[r1 + c1] = t
        return ((r1, c1), swap(state, (row + col), (r1 + c1)))
    elif action == 'E':
        r1 = row
        c1 = col + 2
        
        #t = state[row + col]
        #state[row + col] = state[r1 + c1]
        #state[r1 + c1] = t
        return ((r1, c1), swap(state, (row + col), (r1 + c1)))
    else:
        r1 = row - 2
        c1 = col
        
        #t = state[row + col]
        #state[row + col] = state[r1 + c1]
        #state[r1 + c1] = t
        return ((r1, c0), swap(state, (row + col), (r1 + c1)))
    

def graph_search(problem=None,
                 Node=None,
                 fringe=None,
                 closed_list=None,
                 ):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    """
    This is the incorrect Version, Needs to be fixed.

    Correct solution looks like:
    closed list is empty
    fringe has the initial state
    While fringe not empty:
        pull a state,s, from the fringe.
        check to see if s is a goal state.
        if it is:
            return the search node, for walking back to root.
        else:
            add s.state() to closed list
            expand s to s0 with action a0 ... sn to an
            if s0 not in fringe or closed list:
                add s0 to fringe
                point s0 to s with parent action a0
            repeat for s1 ... sn
    """


#Test Code:
    fringe.put(Node)
    #grid = problem.grid
    while len(fringe) > 0:
        s = fringe.get()
        #print("State: ", s.state)
        coords, state = s.state
        #print(s.state)
        stateTest = intify(state)
        if problem.goal_test(stateTest):
            solution.append(s)
            while s.parent != None:
                s = s.parent
                solution.append(s)
                solution = solution[::-1]
                #for node in solution:
                    #print(node.state, ' ', node.parent_action)
            return solution
        closed_list.put(stateTest)
        #We need to get the successors of each coordinate
        for nodes in problem.successors(coords):
            action = nodes[0]
            newCoords, newState = process(state, coords, action, sizeOf(intify(state)))
            if intify(newState) in closed_list.xs:
                pass
            else:
                fringe.put(SearchNode((newCoords, newState), s, action))
    return None # None is used to indicate no solution

    

"""
    while 1:
                
        (r, c) = (0, 0)
        maze = problem.maze
        for action in solution:
            (r, c) = maze.get_adj_tuple((r, c), action)
        dirs = maze.get_directions((r, c))
        if dirs != []:
            action = random.choice(dirs)
            solution.append(action)
            print("actions:", dirs, ",", end='')
            print("choose:", action, ",", end='')
            print("resulting pos:", maze.get_adj_tuple((r, c), action))
            print("solution:", solution)
            print()
    
            
        if random.randrange(0, 200) == 0:
            return solution

"""
