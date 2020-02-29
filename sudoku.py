
def getBoard(temp):
    returnBoard = list()
    for line in temp:
        currLine = list()
        for c in line:
            if c != ' ' and c != '\n':
                currLine.append(int(c))
        returnBoard.append(currLine)
    return returnBoard
def printStart(board):
    print("Sudoku board:")
    for line in board:
        temp = str()
        for num in line:
            temp += str(num)
            temp += ' '
        print(temp)
def printResult(board):
    for line in board:
        temp = str()
        for num in line:
            temp += str(num)
        print(temp)
        print('\n')
def checkRow(board,row,num):
    tempSet = set()
    tempSet.add(num)
    for currNum in board[row]:
        if currNum in tempSet:
            return False
        tempSet.add(currNum)

    return True
def checkColumn(board,column,num):
    tempSet = set()
    tempSet.add(num)
    for i in range(0,9):
        if board[i][column] in tempSet:
            return False
        tempSet.add(board[i][column])
    return True

def checkSquares(board,row,column,num):
    #get specific square 
    #square rule: top left is square 0
    #count moving horizontally so top right square is square 2
    #bottom left square is square 6
    #bottom right square is 8
    square = int()
    if row >=0 and row < 3:
        if column >= 0 and column < 3:
            square = 0
        elif column >= 3 and column <6:
            square = 1
        else:
            square = 2
    if row >=3 and row < 6:
        if column >= 0 and column < 3:
            square = 3
        elif column >= 3 and column <6:
            square = 3
        else:
            square = 5
    else:
        if column >= 0 and column < 3:
            square = 6
        elif column >= 3 and column <6:
            square = 7
        else:
            square = 8
    if(square == 0):    #top left 
        tempSet = set()
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] in tempSet:
                    return False
                tempSet.add(board[i][j])



def promising(board,row,column,num):
    return checkRow(board,row,num) and checkColumn(board,column,num) and checkSquares(board,row,column,num)

def solve(board,index):

    row = index / len(board)
    column = index % len(board)

    if(row == 8 and column == 8):
        print('Solved')
        printResult(board)
    #increment index
    index += 1

    if board[row][column] != 0: #if number doesn't need to be changed
        return solve(board,index)
    else:   #if number needs to be changed
        for i in range(1,10):
            if promising(board,row,column,i):
                board[row][column] = i    
                solve(board,index)
            
            
    




print('Enter filename for sudoku board: ')

#read in board
fileName = input()
temp = list()
with open(fileName,'r') as f:
    for line in f:
        temp.append(line)



#change lines of strings to ints
board = getBoard(temp)

#print starting configuration:
printStart(board)
    
#solve board
solve(board,0)