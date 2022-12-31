import random

from main import Tiles

class Board(object):
    def __init__(self) -> None:
        self.board = [[Tiles() for _ in range(4)] for _ in range(4)]
        
    def get_tiles(self, x: int, y: int) -> Tiles:
        return self.board[x][y]
        
    def get_value(self,x:int,y:int) -> int:
        return self.get_tile(x,y).get_value()
    
    def empty_tiles(self)-> list(tuple):
        results = []
        for i in range(4):
            for j in range(4):
                results.append((i,j)) if not self.get_value(i,j) else None
        return results
    
    def set_random(self):
        self.get_tiles(random.choice(self.empty_tiles())).set_value(random.choice(2,4))
        
    
    