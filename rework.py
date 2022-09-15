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
    def __init__(self, puzzle_to_solve):
        self.rows = []
        self.columns = []
        self.grids = []

        loop = 0
        location = 0 #within the puzzle
        while True:
            new_entries = []
            row_name = "R{}:".format(loop)

            if loop >= 9:
                break
            for i in range(9):
                i += location
                new_entries.append(puzzle_to_solve[i])
            
            for e in range(1, 9):
                if e == 0:
                    break
                else:
                    new_entries[0] = new_entries[0] + new_entries[e]
            self.rows.append(row_name + new_entries[0])
            location += 9 #move up the next 9 numbers
            loop += 1
        

init = Solver(test_puzzle)
print (init.rows)