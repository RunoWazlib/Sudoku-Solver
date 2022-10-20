#Solve a Sudoku Puzzle
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
        #Define the rows, columns, and grids of the puzzle
        self.rows = {}
        self.columns = {}
        self.grids = {}

        #Row Detection
        loop = 0
        location = 0 #within the puzzle
        while (loop < 9):
            new_entries = []
            row_name = "R{}".format(loop)
            
            #Add all numbers in the row into "new_entries", accounting for the previous row(s)
            for i in range(9): 
                i += location
                new_entries.append(puzzle_to_solve[i])
            
            #combine all individual entries into single str, don't count the first, otherwise add entry
            for e in range(1, 9):
                if isinstance(new_entries[0], list) == True:
                    break
                elif isinstance(new_entries[e],list) == True:
                    break
                else:
                    new_entries[0] = new_entries[0] + new_entries[e]
            
            #tag row entry with row name, and move up next 9 numbers
            self.rows[row_name] = new_entries[0]
            location += 9
            loop += 1
        
        #Column Detection
        loop = 0
        while (loop < 9):
            new_entries = []
            col_name = "C{}".format(loop)

            #Add all numbers in column to "new_entries", accounting for previous column(s)
            for i in range(9):
                i *= 9
                i += loop
                new_entries.append(puzzle_to_solve[i])
            
            #combine all individual entries into single str, don't count the first, otherwise add entry
            for e in range(1, 9):
                if isinstance(new_entries[0], list) == True:
                    break
                elif isinstance(new_entries[e],list) == True:
                    break
                else:
                    new_entries[0] = new_entries[0] + new_entries[e]
            
            #tag column entry with column name, and advance to next column
            self.columns[col_name] = new_entries[0]
            loop += 1
        
        #Grid Detection
        loop = 0
        location = 0
        while (loop < 9):
            new_entries = []
            grid_name = "G{}".format(loop)

            #Add all number in grid to "new_entries", accounting for previous grid(s)
            for i in range(3):
                i += location #read row
                row_to_view = "R{}".format(i)

                if loop == 0 or loop == 3 or loop == 6:
                    new_entries.append(self.rows[row_to_view][:3])
                
                elif loop == 1 or loop == 4 or loop == 7:
                    new_entries.append(self.rows[row_to_view][3:6])

                elif loop == 2 or loop == 5 or loop == 8:
                    new_entries.append(self.rows[row_to_view][6:])
                
                #combine all individual entries into single str, don't count the first, otherwise add entry
            for e in range(1,3):
                if isinstance(new_entries[0], list) == True:
                    break
                elif isinstance(new_entries[e],list) == True:
                    break
                else:
                    new_entries[0] = new_entries[0] + new_entries[e]
                
            #tag grid entry with grid name, and advance to next grid
            self.grids[grid_name] = new_entries[0]
            loop += 1
    def guesser(self, row, col):
        #Determine the possible numbers for a given unknown
        guesses = []
        known_values = set()
        row_name = "R{}".format(row)
        col_name = "C{}".format(col)
        key = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for i in range(9): #add each individual value to known_values
            known_values.add(self.rows[row_name][i])
        for i in range(9):
            known_values.add(self.columns[col_name][i])
        known_values.remove('n') #Remove unknown placeholder (can't guess to be unknown)

        known_values = list(known_values) #turn set(known_values) to a list so individuals can be changed

        while True:
            #whatever remains in the key is the possible values of a particular spot
            if len(known_values) == 0:
                guesses = key
                break

            key.remove(known_values[0])
            known_values.remove(known_values[0])

        return guesses
    def solver(self):
        #Complete puzzle
        solved_puzzle = []
        unknown_map = []
        #For each row, look at each value and determine if it is unknown or known
        for i in range(9):
            for e in range(9):
                row_name = "R{}".format(i)
                if self.rows[row_name][e] == 'n': 
                    #guess if unknown
                    solved_puzzle.append(self.guesser(i, e))
                    unknown_map.append((i, e))
                else: 
                    #fill in if known
                    solved_puzzle.append(self.rows[row_name][e])
        #Once determined guesses or identities of each value, determine which guess for each value is correct
        #If there's only one guess, replace with that value
        for i in range(len(unknown_map)): #read every unknown
            row = unknown_map[i][0]
            col = unknown_map[i][1]
            row_name = "R{}".format(row)
            if self.rows[row_name][col]:
                pass
            pass
        return solved_puzzle

#Maybe to fix list access issue, make everything a list in a list (DO THIS FOR SURE!!!)

init = Solver(test_puzzle)
print (init.solver())
