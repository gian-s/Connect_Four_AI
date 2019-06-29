"""
AI Player Class, these methods initiate AI Player and it's functionality
AI player assigns each column a score based on the potential to win the game, lose it
not have anything happen or cannot place it because the column is full
In the event of a tie you can choose how the tie is broken
"""
import random  
from connect_four_class import *


class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """Constructer for AIPlayer objects
        """
        assert(checker == 'X'  or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
         
        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """returns string representation for AIPlayers
        """
        return 'Player ' + str(self.checker) + ' ('+ str(self.tiebreak) + ', ' + str(self.lookahead) + ')'

    def max_score_column(self,scores):
        """inputs a list of scores containing score for each column on a board object
           returns the index of the column with the max score, uses one of the tie-breaking methods
           to choose between two or more of the same score
        """
        max_score = max(scores)

        max_indices = [i for i in range(len(scores)) if scores[i] == max_score]

        if self.tiebreak == 'LEFT':
            return max_indices[0]
        elif self.tiebreak == 'RIGHT':
            return max_indices[-1]
        else:
            return random.choice(max_indices)
        
    def scores_for(self,board):
        """inputs a board object and determines AIPlayer's scores for the columns in the board obecject
           returns a list of scores for each column 
        """
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker,col)
                opp_player = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1) 
                opp_scores = opp_player.scores_for(board)   #recursive call for opponent of lookahead -1
                #based on the opponents scores we can tell if the placed checker will result in a win, loss, or no result
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50

                board.remove_checker(col)

        return scores
                    
                
    def next_move(self,board):
        """inputs a board object
           returns AIPlayer's judgement for its best possible move
        """
        scores = self.scores_for(board)
        best_choice = self.max_score_column(scores)
        self.num_moves += 1
        return best_choice
            
                
        

        
