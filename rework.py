from os import read


test_puzzle = [
    'n', '5', '9', 'n', '6', 'n', '4', '8', 'n',
    'n', '8', '2', '9', 'n', '4', '7', '5', 'n',
    'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n',
    'n', '4', '6', '5', 'n', '7', '3', '9', 'n',
    'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n',
    'n', '7', '1', '3', 'n', '9', '2', '4', 'n',
    'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n',
    'n', '2', '4', '6', 'n', '3', '1', '7', 'n',
    'n', '1', '3', 'n', '2', 'n', '9', '6', 'n'
]

test_puzzle_2 = 'n59n6n48nn829n475nnnnnnnnnnn465n739nnnnnnnnnnn713n924nnnnnnnnnnn246n317nn13n2n9n6n'

class Solver():
    def __init__(self):
        self.rows = []
        self.columns = []
        self.grids = []

        while True:
            loop = 0
            location = 0 #within the puzzle
            if loop >= 9:
                break
            for i in range(9):
                i += location
                self.rows.append()
            location += 9 #move up the next 9 numbers

            loop += 1
        

test_puzzle = Solver()
print (test_puzzle.rows)