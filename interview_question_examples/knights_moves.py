# solve for a board whose tiles are annotated 1..64

class MoveTracker:
    def __init__(self, start, first_move):
        self.location = start
        self.moves = [first_move]
        self.num_moves = 0
        
    def get_next_moves(self):
        MOVES = {-15, 15, -17, 17, -6, 6, -10, 10}
        
        this_move = self.moves.pop(0)
        self.num_moves += 1
        
        self.location += this_move
        
        moves = MoveTracker.remove_bad_moves(self.location, this_move)

        for move in moves:
            self.moves.append(move)
            
    @staticmethod
    def remove_bad_moves(location, prev_move=None):
        '''Perform logic to generate next moves based on board location
         remove previous move made, and moves that would put knight out of the board'''
        MOVES = {-15, 15, -17, 17, -6, 6, -10, 10}
        if prev_move:
            MOVES.remove(prev_move)
            
        # check if location are on any of the board edges/corners
        pass
    
        return MOVES

def minJumps(src, dest):
    MOVES = MoveTracker.remove_bad_moves(src)
    
    states = [MoveTracker(src, move) for move in moves]
    
    for s in states:
        s.get_next_moves()
        if s.location == dest:
            return s.num_moves
