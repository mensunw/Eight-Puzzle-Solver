#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Mensun Wang
# email: mensun@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Daniel Kim
# partner's email: cmdannyk@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        ''' creates a new searcher object with a deph limit '''
        self.states  = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    #2
    def add_state(self, new_state):
        ''' takes in self (searcher object) and new_state (state object) and adds the
        state to the list '''
        
        self.states += [new_state]
        
    #3
    def should_add(self, state):
        ''' takes in self (searcher object) and state (state object), returns True if Searcher should
        add state to list of untested states, False otherwise '''
        
        if((state.num_moves > self.depth_limit) and (self.depth_limit != -1)):
            return False
        if(state.creates_cycle()):
            return False
        return True
    
    #4
    def add_states(self, new_states):
        ''' takes in self (searcher object) and list of new states []'''
        
        for state in new_states:
            if(self.should_add(state)):
                self.add_state(state)
                
                
    #5
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    #6
    def find_solution(self, init_state):
        ''' takes in self (searcher object) and init_state (first state) and returns a solution state'''
        
        self.add_state(init_state)
        while(len(self.states) != 0):
            state = self.next_state()
            self.num_tested += 1
            if(state.is_goal()):
                return state
            else:
                self.add_states(state.generate_successors())
            #self.add_states(succ)
            
        return None
        
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    ''' subclass of searcher, searches for goal state based on depth '''
    
    #1
    def next_state(self):
        ''' takes in self (BFSearcher object) and chooses the next state to
        be tested based on lowest depth '''
        
        lowestDepth = self.states[0]
        for state in self.states:
            if(state.num_moves < lowestDepth.num_moves):
                lowestDepth = state
        self.states.remove(lowestDepth)
        return lowestDepth

class DFSearcher(Searcher):
    ''' subclass of searcher, searches for goal state based on depth '''
    
    #2
    def next_state(self):
        ''' takes in self (DFSearcher object) and chooses the next state to
        be tested based on highest depth '''
        
        highestDepth = self.states[0]
        for state in self.states:
            if(state.num_moves > highestDepth.num_moves):
                highestDepth = state
        self.states.remove(highestDepth)
        return highestDepth


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    ''' a heuristic function that calcluates misplaced tiles and returns it '''
    return state.board.num_misplaced()

def h2(state):
    ''' a heuristic function that calculates index difference and returns it '''
    return state.board.num_difference()


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    
    def __init__(self, heuristic):
        ''' constructor for GreedySearcher '''
        super().__init__(-1)
        self.heuristic = heuristic
        
        
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        ''' overrides, takes in self (GreedySearcher object) and state (state object) and adds 
        sublist to states attribute '''
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        ''' takes in self (GreedySearcher object) and chooses next state based on priority '''
        
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
        
    ### Add your GreedySearcher method definitions here. ###


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    ''' a subclass searcher that takes into account misplaced tiles and depth '''
    
    def priority(self, state):
        ''' overrides and also accounts for depth (num_moves) '''
        return -1 * (self.heuristic(state) + state.num_moves) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
