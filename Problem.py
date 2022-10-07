"""
nProblem is a subclass of Problem.The following methods of MazeProblem must tbe implemented:
- goal_test(self, state)
- actions(self, state)
- result(self, state, action)
- successors(self, state)
    
"""
class Problem(object):

    def __init__(self,
                 initial_state,
                 ):
        self.initial_state = initial_state
        
    
    def get_initial_state(self):
        return self.initial_state

    def goal_test(self, state):
        raise NotImplementedError
                 
    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def successors(self, state):
        raise NotImplementedError
    
    def cost(self, state, action):
        return 1


class nProblem(Problem):

    def __init__(self,
                 size = 0,
                 initial_state=None,
                 grid = None
                 ):
        Problem.__init__(self, initial_state)
        self.goal_state = 0
        for i in range(1, size * size):
            self.goal_state *= 10
            self.goal_state += (i)
        self.goal_state *= 10
        print("Goal State: ", self.goal_state)
        self.grid = grid

    def goal_test(self, state):
        return state == self.goal_state
                 
    def actions(self, state):
        return self.grid.get_directions(state)

    def result(self, state, action):
        return self.grid.get_adj_tuple(state, action)

    def successors(self, state):
        dirs = self.actions(state)
        return [(d, self.result(state, d)) for d in dirs]

