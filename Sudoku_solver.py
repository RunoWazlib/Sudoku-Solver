#Sudoku is a game with a 9x9 square consisting of 3x3 squares
#assumptions are made on the unfilled squares

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

class Puzzle_Assembler():
    def __init__(self, ):
    #row sensing
        row_org = {}
        row_org['r1'] = []
        row_org['r2'] = []
        row_org['r3'] = []
        row_org['r4'] = []
        row_org['r5'] = []
        row_org['r6'] = []
        row_org['r7'] = []
        row_org['r8'] = []
        row_org['r9'] = []

        location = 0
        for i in range(1, 10): #repeat 9 times for each of the 9 rows
            current_row = (row_org['r' + str(i)]) #tells what row you're in
            for e in range(9):
                e += location
                current_row.append(total_values[e])   
            location += 9

    #column sensing    
        col_org = {}
        col_org['c1'] = []
        col_org['c2'] = []
        col_org['c3'] = []
        col_org['c4'] = []
        col_org['c5'] = []
        col_org['c6'] = []
        col_org['c7'] = []
        col_org['c8'] = []
        col_org['c9'] = []

        column_to_check = 0 #column to check is the location of what column we are searching for, starting at 0
        #The logic to find values of columns simply takes the values out of the row_org arrays
        for i in range(1, 10): 
            current_col = (col_org['c' + str(i)]) #tells me what column i'm in
            for e in range(1, 10):
                current_col.append(row_org['r' + str(e)][column_to_check]) #[0] =
            column_to_check += 1

    #grid sensing
        grids = {}
        grids['a1'] = []
        grids['a2'] = []
        grids['a3'] = []
        grids['b1'] = []
        grids['b2'] = []
        grids['b3'] = []
        grids['c1'] = []
        grids['c2'] = []
        grids['c3'] = []

        while len(grids['c3']) != 9:
            #get a row, sort the row by sets of three, put each in its grid
            # a [1, 2, 3]       #a should get the first three rows
            # b [1, 2, 3]       #b should get the next three rows
            # c [1, 2, 3]       #c should get the last three rows
            # grids represents the sub-grids of the main puzzle consisting of 9 values

            for i in range(1, 10): #i is representing the row
                grid = 'a'
                if i >= 4:
                    grid = 'b'
                    pass
                if i >= 7:
                    grid = 'c'
                    pass

                row_to_check = row_org['r'+str(i)] #gives a row to look through
                first_set = row_to_check[:3] #1, 3 => should go to a1, then b1, then c1
                second_set = row_to_check[3:6] #4, 6 => should go to a2, then b2, then c2
                third_set = row_to_check[6:] #7, 9 => should go to a3, then b3, then c3

                for e in range(3):
                    grids[grid+str(1)].append(first_set[e]) #should be three values per grid
                    grids[grid+str(2)].append(second_set[e])
                    grids[grid+str(3)].append(third_set[e])

        #takes the composite puzzle and splits it into the three categories, and defines them as self.x
        self.grids = grids
        self.row_org = row_org
        self.col_org = col_org
    

    def solved_check(self, row_org, col_org, grids):
        for i in range(1, 10): #checks rows
            row_org_check = set(row_org['r' + str(i)]) #the nature of sets is that no number can be the same within the same set
                #ex. 'r1' = [1, 2, 3, 4, 5, 6, 7, 8, 9] --- Passed
                #ex. 'r1' = [1, 2, 4, 7, 8, 9] --- Failed
        if len(row_org_check) != 9:
            rows_solved = False
            print("[!] Failed row check; Not Solved")
        else:
            rows_solved = True
            print("[*] Passed row checks")
            
        for i in range(1, 10): #checks columns
            col_org_check = set(col_org['c' + str(i)])
        if len(col_org_check) != 9:
            cols_solved = False
            print("[!] Failed column check; Not Solved")
        else:
            cols_solved = True
            print("[*] Passed column checks")

        passed = True #grid 
        for i in range(1, 10): #i is representing the row
            grid = 'a'
            if i >= 4:
                grid = 'b'

            if i >= 7:
                grid = 'c'
            
            if grids[grid + str(1)][0] == grids[grid + str(1)][1]:
                print("[!] Failed grid check; Not Solved")
                passed = False
                break
            elif grids[grid + str(1)][0] == grids[grid + str(1)][2]:
                print("[!] Failed grid check; Not Solved")
                passed = False
                break
            elif grids[grid + str(2)][1] == grids[grid + str(3)][2]:
                passed = False
                print("[!] Failed grid check; Not Solved")
                break

        if passed == True:
            print("[*] Passed grid checks")
        
        if rows_solved == True and cols_solved == True and passed == True:
            print("[-] All checks complete, Puzzle solved\n")
            return None

        else:
            print("[-] All checks complete, Puzzle not solved\n")
            return None


def guesser(row_org, col_org, grids, unknown_values, iteration, iteration_2): #iteration_2 is used so row knows when to change
    #find how many values are unknown
    key = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    known_values = []
    grid_to_look_at = 1
    row_to_look_at = 1
    col_to_look_at = iteration #changes what column to take from
    grid_to_pull = 'a'

    #change row
    if iteration_2 >= 8 and iteration_2 < 17: #0-8, 9-17, 18-26, 35
        row_to_look_at = 2
    elif iteration_2 >= 17 and iteration_2 < 26:
        row_to_look_at = 3
    elif iteration_2 >= 26 and iteration_2 < 35:
        row_to_look_at = 4
    elif iteration_2 >= 35 and iteration_2 < 44:
        row_to_look_at = 5
    elif iteration_2 >= 44 and iteration_2 < 53:
        row_to_look_at = 6
    elif iteration_2 >= 53 and iteration_2 < 62:
        row_to_look_at = 7
    elif iteration_2 >= 62 and iteration_2 < 71:
        row_to_look_at = 8
    elif iteration_2 >= 71:
        row_to_look_at = 9
    
    #change grid
    if row_to_look_at > 3:
        grid_to_pull = 'b'
    if row_to_look_at > 6:
        grid_to_pull = 'c'
    
    if col_to_look_at >= 1:
        grid_to_look_at = 1
    if col_to_look_at > 3:
        grid_to_look_at = 2
    if col_to_look_at > 6:
        grid_to_look_at = 3

    #grab values...
    for i in range(1,9):
        known_values.append(row_org['r'+str(row_to_look_at)][i])

    for i in range(1,9):
        known_values.append(col_org['c'+str(col_to_look_at)][i])
    
    for i in range(9):
        known_values.append(grids[grid_to_pull + str(grid_to_look_at)][i])
    
    known_values = set(known_values)
    known_values_sorted = list(known_values)

    known_values_sorted.remove('n')

    while True:
        for i in range(len(known_values_sorted)):
            key.remove(known_values_sorted[i])
            known_values_sorted.remove(known_values_sorted[i])
            break
        if len(known_values_sorted) == 0:
            break
    

    unknown_values -= 1
    return key

def solver(total_values, row_org, col_org, grids):
    print("\n[*] Beginning to solve...")
    global guesses
    global n_location
    guesses = []
    n_location = []
    exit_case = False
    unknown_values = Unknown_Value_Counter(total_values)
    e = 0
    iteration = 1
    
    #e counts total values while iteration counts to 9 for each column, then resets

    while exit_case == False:
        if e == 81:
            exit_case = True

        if total_values[e] == 'n': #if unknown value...
            n_location.append(int(e))
            key = guesser(row_org, col_org, grids, unknown_values, iteration, e) #guess what it could be
            if len(key) == 1: #if only one guess...
                total_values[e] = key[0] #replace in main
                unknown_values -= 1 #reduce unknowns by 1
                n_location.remove(n_location[-1]) #get rid of unknown location
            else:
                guesses.append(key) #otherwise make a note of all guesses and move on
            
        if len(guesses) == unknown_values:
            exit_case = True #if there aren't any unknown values, break out

        e += 1
        iteration += 1
        if iteration == 10:
            iteration = 1

    print("[-] Guesses Compiled:\n")
    print(guesses)

def Unknown_Value_Counter(puzzle): #gives the number of 'n's or "Unknowns"in the puzzle
    count = 0
    i = 0
    while i <= 81:
        if puzzle[i] == 'n':
            count += 1
        i += 1
        if i == 81:
            break
    return count

total_values = []
init_count = 0

#Get values for boxes:
print("[*] Input the known values of the boxes or 'n' if unknown")
print("[*] Begin input from the upper left-most square, and continue input from left to right\n")

def box_value_checker(box_value):
    valid_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    check = False
    for i in range(9):
        if box_value == valid_number[i]:
            check = True
            break
    return check

#raw data interpreter
while init_count <= 81:
    if len(test_puzzle) == 81: #For testing
        total_values = test_puzzle
        init_count += 81
        break
    
    box_value = str(input("What is the value of the box?\n"))
    if box_value != 'n':
        if box_value_checker(box_value) == True: #checks if input is a valid number
            total_values.append(box_value)
            init_count += 1
        else:
            print('Invalid entry, try again...')

    elif box_value == 'n':
        total_values.append('n')
        init_count += 1
    
print("Total Values: %s \n" % (total_values))
print("Total Values.len: %d \n" % (len(total_values)))
if len(total_values) < 81:
    print("[!] Not all values given")
    exit()
puzzle = total_values

puzzle = Puzzle_Assembler()
print ("Rows: " + str(puzzle.row_org) + "\n")
print ("Columns: " + str(puzzle.col_org) + "\n")
print("Grids: " + str(puzzle.grids) + "\n")


#check if puzzle is solved
puzzle.solved_check(puzzle.row_org, puzzle.col_org, puzzle.grids)

#Number of 'n's in puzzle
print("Number of Unknown Values: " + str(Unknown_Value_Counter(total_values)) + "\n")

#Sorting out values
i = 0
while True:
    i += 1
    solver(total_values, puzzle.row_org, puzzle.col_org, puzzle.grids)
    if i == 2:
        break
#check if puzzle is solved
puzzle.solved_check(puzzle.row_org, puzzle.col_org, puzzle.grids)

print('fin')