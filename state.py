#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Mensun Wang
# email: mensun@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Daniel Kim
# partner's email: cmdannyk@bu.edu
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    
    def __init__(self, board, predecessor, move):
        ''' a constructor for initiating a state '''
        self.board = board
        self.predecessor = predecessor
        if(self.predecessor == None):
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1
        self.move = move
            
    ### Add your method definitions here. ###
    
    #2
    def is_goal(self):
        ''' takes in self (State object) and returns True if State object is goal, False otherwise '''
        return(self.board.tiles == GOAL_TILES)
    
    #3
    def generate_successors(self):
        ''' takes in self (board object) and returns a list of all successors '''
        successors = []
        for move in MOVES:
            b = self.board.copy()
            if(b.move_blank(move)):
                state = State(b, self, move)
                successors += [state]
        return successors
    
    #7
    def print_moves_to(self):
        ''' takes in self (state object) and returns a print chain from initial state to
        goal state '''
        
        if(self.num_moves == 0):
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print("move the blank " + self.move + ":")
            print(self.board)
            

        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
