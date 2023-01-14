import unittest 
from main import Board, Tiles

class TestBoard(unittest.TestCase):
    
    def test_compress(self):
        my_test_board = Board()
        my_test_board.get_tiles(1,2).set_value(2)
        my_test_board.get_tiles(1,3).set_value(2)
        my_test_board.get_tiles(0,3).set_value(8)
        print(my_test_board)
        print()
        print()
        print()
        my_test_board.compress()
        print(my_test_board)
        print()
        print()
        print()
        my_test_board.merge()
        print(my_test_board)
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()