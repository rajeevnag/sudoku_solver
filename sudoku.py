def getBoard(temp):
    returnBoard = list()
    for line in temp:
        currLine = list()
        for c in line:
            if c != ' ' and c != '\n':
                currLine.append(int(c))
        returnBoard.append(currLine)
    return returnBoard

def printBoard(board):
    print("Sudoku board:")
    for line in board:
        temp = str()
        for num in line:
            temp += str(num)
            temp += ' '
        print(temp)
        
def checkRow(board,row,num):
    tempSet = set()
    tempSet.add(num)
    for currNum in board[row]:
        if currNum in tempSet:
            return False
        if currNum != 0:
            tempSet.add(currNum)
    return True

def checkColumn(board,column,num):
    tempSet = set()
    tempSet.add(num)
    for i in range(0,9):
        if board[i][column] in tempSet:
            return False
        if board[i][column] != 0:
            tempSet.add(board[i][column])
    return True

def checkSquares(board,row,column,num):

    #lowerbound = (row or column / 3) and then multiply by 3
    tempRow = int(row // 3)
    tempCol = int(column // 3)

    
    lowerBoundRow = tempRow * 3
    upperBoundRow = lowerBoundRow + 3
    
    
    lowerBoundCol = tempCol * 3
    upperBoundCol = lowerBoundCol + 3

    #add the number you want to add first so that if you come across it in the nearby squares that means it's already there and you can't add it
    tempSet = set()
    tempSet.add(num)
    
    for i in range(lowerBoundRow,upperBoundRow):
        for j in range(lowerBoundCol,upperBoundCol):
            if board[i][j] in tempSet:
                return False
            if board[i][j] != 0:
                tempSet.add(board[i][j])
            

    return True


def promising(board,row,column,num):
    rowResult = checkRow(board,row,num)
    colResult = checkColumn(board,column,num)
    squareResult = checkSquares(board,row,column,num)
 
    return checkRow(board,row,num) and checkColumn(board,column,num) and checkSquares(board,row,column,num)
    

def solve(board,index):

    row = int(index // len(board))
    column = int(index % len(board))
    if row > 8 or column > 8:
        print('wrong')
        printBoard(board)
        print(row)
        print(column)
        print(index)
        return True
    
    #increment index
    index += 1


    if board[row][column] != 0: #if number doesn't need to be changed
        return solve(board,index)
    else:   #if number needs to be changed
        
        for i in range(1,10):
            
            if promising(board,row,column,i):
                board[row][column] = i    
                worked = solve(board,index)
                if(worked != True):
                    board[row][column] = 0
                else:
                    return True
        
            
                
            
                
            
            
    




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
printBoard(board)
    

#solve board
solve(board,0)

#output result
print('result')
printBoard(board)