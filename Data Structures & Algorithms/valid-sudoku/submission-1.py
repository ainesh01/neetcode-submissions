class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #horizontal
        for i in range(9):
            numSet = set()
            for j in range(9):
                # print("i: "+ str(i) + " j: "+ str(j)+" numSet: "+str(numSet))
                if board[i][j] != ".":
                    # print("board[i][j]: "+ str(board[i][j]))
                    if board[i][j] in numSet:
                        print("horizontal failing")
                        return False
                    else:
                        numSet.add(board[i][j])

        #vertical
        for i in range(9):
            numSet = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in numSet:
                        print("vertical failing")

                        return False
                    else:
                        numSet.add(board[j][i])

        #3x3
        for i in range(3):
            for j in range(3):
                numSet = set()
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] != ".":
                            if board[i*3+k][j*3+l] in numSet:
                                print("3x3 failing")

                                return False
                            else:
                                numSet.add(board[i*3+k][j*3+l])
        return True



