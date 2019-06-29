"""
Player Class, methods establish functionality for a human player

"""
from board_class import Board



class Player:




    def __init__(self,checker):
        """Creates a player object
        """
        assert(checker == "X" or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """displays the player object and the checker it represents
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """returns the checker for the opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    def next_move(self,board):
        """inputs a board object and asks the user to input the column number
           where it would like to place a checker
        """
        a = int(input('Enter a column: '))

        while board.can_add_to(a) == False:
            print('Try again!')
            a = int(input('Enter a column: '))

        if board.can_add_to(a) == True:
            self.num_moves += 1
            return a

        
            
        
        
            
        
            
        
        
