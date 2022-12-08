###########################################################################
#
# Author: John Shalenko
# Date: 10-4-22
# Project: Brute-force Sudoku solver
#   Description: project takes in an unfinished and solvable sudoku, and brute forces the result to the operator
#   Inspiration: I love sudoku, but I hate the 'evil' and 'extreme' variations put out there by sudoku.com; this is my way of expressing and getting out my frustrations
#   Sources used: None really beyond what I learned in entry-level computer science courses, with all the algorithms coming from me
#
###########################################################################

class Block:
    
    def __init__(self, value = 0):
        self.value = value
        self.possibleValues = [1,2,3,4,5,6,7,8,9]

    def __str__(self):
        return f'{self.value}'

    __repr__ = __str__

    def setValue(self, value):
        
        self.value = value

        if value != 0:
            return
        elif value == 0: # this part is not entirely necessary, but does save the hassle of going back and adding another function to reset the block
            
            for i in range(len(self.possibleValues)):
                self.possibleValues.pop()
                
            for i in range(9):
                val = i + 1
                self.possibleValues.insert(len(self.possibleValues), val)

    def removePossibility(self, value): #checks to see if it is possible to remove a value from the block, and does so if it can
        if self.value == 0 and value in self.possibleValues:
            self.possibleValues.pop(self.possibleValues.index(value))

            if len(self.possibleValues) == 1:
                self.setValue(self.possibleValues[0])

    def absoluteValue(self, value): #sets the value and removes all non-relivant possibilities
        for i in range(9):
            newVal = i + 1
            if newVal != value:
                self.removePossibility(newVal)

class Board:

    def __init__(self): #yes this formatting was necessary as if I had done 9*[9*[Block()]] they would have all pointed to the same object, trust me I tested it

        self.board = [
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()],
            [Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block(), Block()]
        ]


    def __str__(self):
        content = ""
        
        for i in range(9):
            if i % 3 == 0 and i != 0:
                content  += "\n― ― ― + ― ― ― + ― ― ―\n"
            elif i != 0:
                content += "\n"

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    content += '| '
                
                content += f'{self.board[i][j]} '

        return content

    
    __repr__ = __str__

    def setBoard(self, values):

        for i in range(9):
            for j in range(9):
                val = int(values[i][j])
                if val != 0:
                    
                    self.board[i][j].absoluteValue(val)
                
                else:
                    self.board[i][j].setValue(val)
    '''
    # takes in a board of a specified structure to run through the program
    # it shoud be in the format of each row with numbers separated by spaces and 0 as the placeholder for any blank spaces on the board
    # such as the following:
    # 0 7 0 6 0 0 0 8 3
    # 5 0 0 0 0 9 0 0 0
    # 0 0 0 0 0 0 0 0 0
    # 0 0 0 1 3 0 0 0 2
    # 9 0 0 0 0 0 4 0 0 => [[0,7,0,6,0,0,0,8,3],[5,0,0,0,0,9,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,1,3,0,0,0,2],[9,0,0,0,0,0,4,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,3,0,0,0,9,0],[4,0,0,0,0,0,5,0,0],[0,2,0,0,0,0,0,0,0]]
    # 0 0 0 0 8 0 0 0 0
    # 0 0 0 3 0 0 0 9 0
    # 4 0 0 0 0 0 5 0 0
    # 0 2 0 0 0 0 0 0 0
    # and yes, the above board does have a solution, don't be scared of the 0s, that's what this program's for
    '''
    def importBoard(self, fileName):
        
        with open(fileName) as f:
            contents = f.read()

        f.close()

        rows = contents.splitlines()

        values = 9*[None]

        for i in range(len(values)):
            values[i] = rows[i].split(' ')

        self.setBoard(values)

    '''
    #This function was only used in back-end testing for the program
    def resetBoard(self):
        values = 9*[9*[0]]

        self.setBoard(values)
        '''

    def isPossible(self, value, row, column):
        
        for i in range(9): #tests against all values in the current row
            if value == self.board[row][i].value and value in self.board[row][column].possibleValues:
                return False
        
        for i in range(9): #tests against all values in the current column
            if value == self.board[i][column].value and value in self.board[row][column].possibleValues:
                return False

        boxYCoord = row - row % 3
        boxXCoord = column - column % 3

        #tests against all values in the 'box' that is on a standard sudoku board
        for i in range(3):
            for j in range(3):
                if value == self.board[i + boxYCoord][j + boxXCoord].value and value in self.board[row][column].possibleValues:
                    return False

        return True

    def narrowDown(self): #eliminates the possible values from a given block that has no current value
        
        hasChanged = True

        while hasChanged:
            hasChanged = False
        
            for i in range(9):
                for j in range(9):
                    if self.board[i][j].value == 0:
                        for v in range(9):
                            val = v + 1
                            if not (self.isPossible(val, i, j)):
                                hasChanged = True
                                self.board[i][j].removePossibility(val)
    
    '''
    def listUnknowns(self): #this function was only used in back end testing for the program

        for i in range(9):
            for j in range(9):
                if self.board[i][j].value == 0:
                    print(f"Row {i+1}, Column {j+1}, Box{(j//3 + 1)+(i-i%3)}: {self.board[i][j].possibleValues}")'''

    def findNextBlank(self, row, column): #returns the 'coordinates' of the next block that is subject to be affected by the .force() method

        for i in range(9):
            for j in range(9):
                if len(self.board[i][j].possibleValues) > 1 and ((i == row and j > column) or (i > row)):
                    return i, j
                elif i == 8 and j == 8:
                    return None, None

    def force(self, row = 0, column = 0): #very bizzare recursive method that works a bit like a pseudo-DFS algorithm; it tests for values as far as it can on its own, and back tracks if it runs into any problems, all without using any Node() structures, though i guess the Block()s are pseudo-nodes in this case
        
        if len(self.board[row][column].possibleValues) == 1 or self.board[row][column].value != 0: #tests to see if the block only has one value possible(i.e. it's already filled in)
            nextRow, nextCol = self.findNextBlank(row, column)                                     #or if the value of the block is non-zero
            if nextRow is not None:
                return self.force(nextRow, nextCol) #moves on to next cycle if it is either and it is not at the final space of the board
            else: #base case = end of board and all values have been filled in
                return None
        else:
            totalImpossible = 0

            for i in range(len(self.board[row][column].possibleValues)): #goes through the block objects list to see if the remaining values are possible and adjusts the board if necessary
                if self.isPossible(self.board[row][column].possibleValues[i], row, column) and self.board[row][column].value == 0:
                    self.board[row][column].setValue(self.board[row][column].possibleValues[i])
                    checkNext = self.force(row, column)
                    
                    if checkNext is None:
                        return
                    elif checkNext is False:
                        self.board[row][column].value = 0 #does not use .setvalue() here as it would erase the narrowed list on the block
                        totalImpossible += 1
                else: 
                    totalImpossible += 1
            
            if totalImpossible == len(self.board[row][column].possibleValues):
                return False

def solve(fileName): #culminating function and proper order of how they should be run; running .force() without .narrowDown() cuts down heavily on efficiency as it will make a check againt all 9 values in each block
    b = Board()
    b.importBoard(fileName)
    b.narrowDown()
    b.force()

    print(b)
