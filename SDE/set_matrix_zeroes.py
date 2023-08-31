from ast import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = []
        cols = []
        for i, c in enumerate(matrix):
            for j, r in enumerate(c):
                if r == 0:
                    row.append(i)
                    cols.append(j)

        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        print(matrix)

if __name__=='__main__':
    Solution.setZeroes(matrix=[[1,1,1,1],[1,0,1,1],[1,0,0,1]])
           
                
                