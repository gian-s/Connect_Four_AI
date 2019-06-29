"""
Board Class that creates a visual representation of a Connect Four Board
The methods create the rules of the game and check if someone has one. Other
methods were used for testing purposes
"""


class Board:

    def __init__(self,height,width):
        
        """a constructor for Board Objects
        """
        self.height = height
        self.width = width
        self.slots = [[' ']*width for r in range(height)]




    def __repr__(self):
        
        """Returns a string representation for a Board object.
        """
        s = ''
        hyphen_factor = (self.width*2)+1
        
        for row in range(self.height):          #Displays the column lines
            s += '|'

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'

        for col in range(hyphen_factor):  #Displays the hyphens at the bottom
            s += '-'  
        s+= '\n'
        
        for col in range(self.width):     #Displays the column numbers at the bottom
            col_num = col % 10
            s += ' ' + str(col_num)
            
        return s

    def add_checker(self, checker, col):
        
        """ adds a checker in the specified slot
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        
        row = 0

        while row < self.height-1 and self.slots[row][col] not in "XO" :
            row += 1
            if self.slots[row][col] in 'XO':
                row -= 1
                break

        self.slots[row][col] = checker

        

    def reset(self):
        """resets the board object by replacing the slots attribute with a new
           board of the same height and width
        """
        self.slots = [[' ']*self.width for r in range(self.height)]
            
                
    #Method testing purposes
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

         

    def can_add_to(self,col):
        
        """Returns True if it is valid to place a checker in the column col
           Otherwise it should return False
        """
        if col > self.width-1 or col < 0:
            
            return False
        else:
           
            if self.slots[0][col] == " ":
                return True
            else:
                return False




    def is_full(self):
        """Returns True if the called Board object is completely full of checkers
           returns False otherwise
        """
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False
        return True
        
       
    #For testing purposes
    def remove_checker(self,col):
        """removes the top checker from a specified column, col
           if there are no checkers in the column, the method will not do anything
        """
        row = 0
        while row <= self.height-1:
            if self.slots[row][col] in 'XO':
                self.slots[row][col] = ' '
                break
            else:
                row += 1
                

    def is_win_for(self,checker):
        """inputs a checker that is either X or O
           returns True if there are four consecutive slots containing checker
        """

        assert(checker == "X" or checker == 'O')
        #calls every method to see if there is at least one type of win
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker)== True or \
           self.is_up_diagonal_win(checker)== True:
            return True
        else:
            return False


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col+1] == checker and \
                   self.slots[row][col+2] == checker and \
                   self.slots[row][col+3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self,checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False

    def is_down_diagonal_win(self,checker):
        """ Checks for a diagonal win from left to right
            for the specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True

        return False
    

    def is_up_diagonal_win(self,checker):
        """Checks for a diagonal win from right to left
            for the specified checker
        """
        for row in range(self.height-3,):
            for col in range(self.width - 4,self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col-1] == checker and \
                   self.slots[row+2][col-2] == checker and \
                   self.slots[row+3][col-3] == checker:
                    return True
        return False
            
    
