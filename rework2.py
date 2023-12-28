from math import *
class Puzzle():
    def __init__(self, input_puzzle):
        """
        Organize subunits of sudoku puzzle

        Args:
            input_puzzle (string): A string in order of grids from upper left corner to lower right corner
           
            Alignment of grids - 
            LG NG CG
            LN NN CN
            LE NE CE
        """
        self.grids = {}
        self.rows = {}
        self.columns = {}
        input_puzzle = input_puzzle.lower()
        
        #get rows
        for i in range(9):
            if i < 1:
                self.rows[i+1] = [input_puzzle[:9]]
            else:
                self.rows[i+1] = [input_puzzle[(i*9):(i*9+9)]]

        #get grids
        grid_assembly = []
        i = 0
        while i < len(input_puzzle):
            grid_assembly.append([input_puzzle[i:i+3]])
            i = i+3
        
        for grid_row in range(3):
            for grid_column in range(3):
                grid_assembly2 = grid_assembly[grid_column+(9*grid_row)]+grid_assembly[grid_column+3+(9*grid_row)]+grid_assembly[grid_column+6+(9*grid_row)]
                self.grids[len(self.grids)+1] = grid_assembly2

        #get columns
        for column in range(9):
            column_assembly = []
            for i in range(9):
                column_assembly.append(input_puzzle[column+(9*i)])
                column_assembly2 = "".join(column_assembly)
            self.columns[column+1] = [column_assembly2]

        #get unknown values + get indexes
        self.number_unknown_values = input_puzzle.count('n')
    
    def Guesser(self):
        guesses = {}
        possible_values = [1,2,3,4,5,6,7,8,9]
        while self.number_unknown_values > 0:
            for i in range(1,9):
                if self.grids[i][0].find('n') != -1:
                    position = (self.grids[i][0].find('n'))+i*9
                    guess = []
                    # column_number = Position % 81

                    guesses[position] = guess
            break
                    
                


#test            
test = "123456789"*6+"nnnnnnnnn"*3
#grid test
test = "111222333111222333111222333444555666444555666444555666777888999777888999777888999"
test = Puzzle(test)
print("[*] Grids:")
print(test.grids)
print("[*] Rows:")
print(test.rows)
print("[*] Columns:")
print(test.columns)
print("[*] Number of 'n's:")
print(test.number_unknown_values)
test.Guesser()