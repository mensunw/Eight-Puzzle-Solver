#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Mensun Wang
# email: mensun@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Daniel Kim
# partner's email: cmdannyk@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        col = 0
        for c in digitstr[0:3]:
            self.tiles[0][col] = c
            col += 1
        
        
        col = 0
        for c in digitstr[3:6]:
            self.tiles[1][col] = c
            col += 1
        
        
        col = 0
        for c in digitstr[6:9]:
            self.tiles[2][col] = c
            col += 1
            
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if(self.tiles[r][c]) == "0":
                    self.blank_r = r
                    self.blank_c = c
    
                    
                


    ### Add your other method definitions below. ###
    
    #2
    def __repr__(self):
        ''' takes in self (board object) and returns a new board string representations '''
        
        builder = ""
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if(self.tiles[r][c] == "0"):
                    builder += "_ "
                else:
                    builder += self.tiles[r][c] + " "
            builder += "\n"
        return builder
    
    #3
    def move_blank(self, direction):
        ''' takes in self (board object) and str direction and changes board based on direction. Returns
        False if direction is invalid, True otherwise '''
        
        blank_r = self.blank_r
        blank_c = self.blank_c
        
        if(direction == "up"):
            blank_r -= 1
        elif(direction == "down"):
            blank_r += 1
        elif(direction == "left"):
            blank_c -= 1
        elif(direction == "right"):
            blank_c += 1
        else:
            return False
        
        if(blank_r < 0 or blank_r > 2 or blank_c < 0 or blank_c > 2):
            return False
        
        
        if(direction == "up"):
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r-1][self.blank_c]
            self.blank_r -= 1
        elif(direction == "down"):
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r+1][self.blank_c]
            self.blank_r += 1
        elif(direction == "left"):
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c-1]
            self.blank_c -= 1
        elif(direction == "right"):
            self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c+1]
            self.blank_c += 1
        else:
            print("something went wrong")
            
        self.tiles[self.blank_r][self.blank_c] = "0"
        return True
    
    #4
    def digit_string(self):
        ''' takes in self (board object) and uses tile attributes to return a string of
        the digits '''
        
        builderBob = ""
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                builderBob += self.tiles[r][c]
        
        return builderBob
    
    #5
    def copy(self):
        ''' takes in self (board object) and uses tile attribute to return a deep copy (board object)'''
        return Board(self.digit_string())
    
    #6
    def num_misplaced(self):
        ''' takes in self (board object) and counts the number of tiles that are not goal tiles. returns
        count '''
        
        count = 0
        for r in range(3):
            for c in range(3):
                if(GOAL_TILES[r][c] != self.tiles[r][c] and self.tiles[r][c] != "0"):
                    count += 1
        return count
    
    def num_difference(self):
        ''' takes in self (board object) and finds difference between each index positions after
        converting them into a list '''
        
        score = 0
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        boardList = []
        bitString = self.digit_string()
        for c in bitString:
            boardList += [int(c)]
        for index in range(len(goal)):
            score += abs(goal[index] - boardList[index]) 
        return score
    
    #7
    def __eq__(self, other):
        ''' takes in self (board object) and checks if the board objects tiles are equal to each other '''
        
        return(self.digit_string() == other.digit_string())
          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    