class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # col_check:
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in num_set:
                        print("col")
                        return False
                    else:
                        num_set.add(board[i][j])
        

        # row_check:
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in num_set:
                        print("row")
                        return False
                    else:
                        num_set.add(board[j][i])

        #square_check:
        for i in range(3):
            for j in range(3):
                num_set = set()
                for m in range(3):
                    for n in range(3):
                        x = i*3+m
                        y = j*3+n
                        print(f"{i}, {j}, {m}, {n}")
                        print(f"{x}, {y}")
                        print(f"{board[x][y]}")
                        if board[x][y] is not ".":
                            if board[x][y] in num_set:
                                print(f"{board[x][y]}")
                                print(f"{num_set}")
                                return False
                            else:
                                num_set.add(board[x][y])
                        print(f"{num_set}")

        return True
        