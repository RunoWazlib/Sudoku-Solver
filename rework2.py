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
        
        #get grids
        for i in range(9):
            if i < 1:
                self.grids[i+1] = [input_puzzle[:9]]
            else:
                self.grids[i+1] = [input_puzzle[(i*9):(i*9+9)]]

        #get rows
        for i in range(9):
            self.rows[i+1] = [
                input_puzzle[(3*i):((3*i)+3)]
                +input_puzzle[((3*i)+9):((3*i)+12)]
                +input_puzzle[((3*i)+18):((3*i)+21)]
                ]

        #get columns
        for column in range(9):
            column_assembly = []
            for i in range(9):
                column_assembly.append(input_puzzle[column+(9*i)])
                column_assembly2 = "".join(column_assembly)
            self.columns[column+1] = [column_assembly2]

        #get unknown values + get indexes
        self.number_unknown_values = input_puzzle.count('n')
        try:
            self.unknown_locations = input_puzzle.index('n')
        except ValueError:
            print("[-] No unknown values")
    
    def Guesser(self):
        possible_values = [1,2,3,4,5,6,7,8,9]
        while self.unknown_values > 0:
            self.unknown_locations[0]
            
test = "123456789"*6+"nnnnnnnnn"*3
test = Puzzle(test)
print(test.grids)
print(test.rows)
print(test.columns)
print(test.number_unknown_values)