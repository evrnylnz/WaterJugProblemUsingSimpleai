import time
from simpleai.search import SearchProblem, breadth_first, uniform_cost, depth_first, limited_depth_first, iterative_limited_depth_first
from simpleai.search.viewers import BaseViewer

myViewer = BaseViewer()

class WaterJugProblem(SearchProblem):
    
    def __init__(self, initial_state):
        """ Gets the value of capacities and goals and assigns them to a tuple """

        user_input = input('enter space seperated capacities : ' )
        capacities_tuple = tuple(int(item) for item in user_input.split())
        user_input2 = input('enter space seperated goal state : ' )
        goal_state_tuple = tuple(int(item) for item in user_input2.split())
        self.capacities = capacities_tuple
        self.initial_state = initial_state
        self.goal = goal_state_tuple
    print('')
    def actions(self, state):
        """ generates legal actions for state """
        (J0, J1, J2) = state
        """ generates legal actions for state """
        (C0, C1, C2) = self.capacities
        
        if J0 > 0: yield 'dump:0'
        if J1 > 0: yield 'dump:1'
        if J2 > 0: yield 'dump:2'

        if J0 < C0: yield 'fill:0'
        if J1 < C1: yield 'fill:1'
        if J2 < C2: yield 'fill:2'

        if J1<C1 and J0>0: yield 'pour:0-1'
        if J0<C0 and J1>0: yield 'pour:1-0'
        if J2<C2 and J0>0: yield 'pour:0-2'
        if J0<C0 and J2>0: yield 'pour:2-0'
        if J1<C1 and J2>0: yield 'pour:2-1'
        if J2<C2 and J1>0: yield 'pour:1-2'

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        (J0, J1, J2) = state
        (C0, C1, C2) = self.capacities
        
        if action == 'dump:0': 
            return (0,J1,J2)
        elif action == 'dump:1': 
            return (J0,0,J2)
        elif action == 'dump:2': 
            return (J0,J1,0)
        elif action == 'pour:0-1': 
            delta = min(J0, C1-J1)
            return (J0-delta, J1+delta,J2)
        elif action == 'pour:1-0':
            delta = min(J1, C0-J0) 
            return (J0+delta, J1-delta,J2)
        elif action == 'pour:0-2': 
            delta = min(J0, C2-J2)
            return (J0-delta, J1,J2+delta)
        elif action == 'pour:2-0':
            delta = min(J2, C0-J0) 
            return (J0+delta, J1,J2-delta)
        elif action == 'pour:1-2': 
            delta = min(J1, C2-J2)
            return (J0,J1-delta, J2+delta)
        elif action == 'pour:2-1':
            delta = min(J2, C1-J1) 
            return (J0, J1+delta, J2-delta)
        elif action == 'fill:0':
            return (C0,J1,J2) 
        elif action == 'fill:1':
            return (J0,C1,J2) 
        elif action == 'fill:2':
            return (J0,J1,C2)

    def is_goal(self, state):
        """ Checks for goal position """
        G0,G1,G2 = self.goal
        return ((state[0]==G0 or G0==0) and 
            (state[1]==G1 or G1==0) and 
            (state[2]==G2 or G2==0))

    def cost(self, state, action, state2):
        """ Returns the cost of actions as defined in problem """
        (C0, C1, C2) = self.capacities

        if action == 'fill:0':
           return C0-state[0]
        elif action == 'fill:1':
           return C1-state[1] 
        elif action == 'fill:2':
           return C2-state[2]
        elif action == 'dump:0':
           return state[0]
        elif action == 'dump:1':
           return state[1]
        elif action == 'dump:2':
           return state[2]
        else :
            return 1
    
problem = WaterJugProblem(initial_state=(0,0,0))
print('\n')

""" runs program for different search algorithms (You can change function parameters)"""

def BreadthFirstSearch():
    print('*** Breadth First Search ***')
    start_time = time.time()
    result = breadth_first(problem, graph_search=True, viewer=myViewer)
    print(result.state)
    print(result.path())
    print(myViewer.stats)
    print('Cost : ' + str(result.cost))
    print('Execution time : '+ "%s seconds" % (time.time() - start_time))
    print('\n')

def DepthFirstSearch():
    print('*** Depth First Search ***')
    start_time = time.time()
    result = depth_first(problem, graph_search=True, viewer=myViewer)
    print(result.state)
    print(result.path())
    print(myViewer.stats)
    print('Cost : ' + str(result.cost))
    print('Execution time : '+ "%s seconds" % (time.time() - start_time))
    print('\n')

def UniformSearch():
    print('*** Uniform Search ***')
    start_time = time.time()
    result = uniform_cost(problem, graph_search=True, viewer=myViewer)
    print(result.state)
    print(result.path())
    print(myViewer.stats)
    print('Cost : ' + str(result.cost))
    print('Execution time : '+ "%s seconds" % (time.time() - start_time))
    print('\n')

def LimitedDepthFirstSearch():
    print('*** Limited Depth First Search ***')
    start_time = time.time()
    result = limited_depth_first(problem, depth_limit=100, graph_search=True, viewer=myViewer)
    print(result.state)
    print(result.path())
    print(myViewer.stats)
    print('Cost : ' + str(result.cost))
    print('Execution time : '+ "%s seconds" % (time.time() - start_time))
    print('\n')

def IterativeLimitedDepthFirstSearch():
    print('*** Iterative Limited Depth First Search ***')
    start_time = time.time()
    result = iterative_limited_depth_first(problem, graph_search=True, viewer=myViewer)
    print(result.state)
    print(result.path())
    print(myViewer.stats)
    print('Cost : ' + str(result.cost))
    print('Execution time : '+ "%s seconds" % (time.time() - start_time))
    print('\n')

BreadthFirstSearch()
UniformSearch()
LimitedDepthFirstSearch()
IterativeLimitedDepthFirstSearch()
DepthFirstSearch()

        

