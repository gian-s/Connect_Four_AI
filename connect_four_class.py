"""
Connect Four function initializes a new game between two player objects. This is how the player objects will begin playing
and processes the moves of each player
"""

from board_class import Board
from player_class import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board


def process_move(player,board):
    """inputs a player object and a board object for the game being played
       prints a message showing which player's turn it is, obtains and applies the player's next move
    """

    
    print(str(player) + "'s turn") #shows which player's turn it is
    col = player.next_move(board)
    board.add_checker(player.checker,col) #adds checker to specific column
    print()
    print(board)
    print()
    if board.is_win_for(player.checker) == True:
        print(player, "wins in", player.num_moves,'moves.\nCongratulations!')
        return True
    elif board.is_win_for(player.checker)== False and board.is_win_for(player.opponent_checker()) == False and board.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
        
"""
For Testing Purposes
"""
class RandomPlayer(Player):

    def next_move(self,board):
        """inputs a board and chooses at random an available column to add a checker to 
           returns index of the randomly selected column    
        """
        avail_col = [i for i in range(board.width) if board.can_add_to(i) == True]
        col = random.choice(avail_col)
        self.num_moves += 1
        return col
        
   
