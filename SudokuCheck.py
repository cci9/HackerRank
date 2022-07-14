def countcheck_9(x):                                   #Repeatation check for 9*9
    for i in x:
        set1 = set()
        for j in i:
            set1.add(j)
        if len(set1) != 9:
            print("Repeatation not allowed")
            break
def countcheck_3(x):                                    #Repeatation check for 3*3
    for i in x:
        set1 = set()
        for j in i:
            set1.add(j)
        if len(set1) != 3:
            print("Repeatation not allowed")
            break
sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [2, 3, 4, 5, 6, 7, 8, 9, 1],
          [3, 4, 5, 6, 7, 8, 9, 1, 2],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [5, 6, 7, 8, 9, 1, 2, 3, 4],
          [6, 7, 8, 9, 1, 2, 3, 4, 5],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [8, 9, 1, 2, 3, 4, 5, 6, 7],
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]                    #sample 1

sudoku = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
          [6, 8, 2, 5, 7, 1, 4, 9, 3],
          [1, 9, 7, 8, 3, 4, 5, 6, 2],
          [8, 2, 6, 1, 9, 5, 3, 4, 7],
          [3, 7, 4, 6, 8, 2, 9, 1, 5],
          [9, 5, 1, 7, 4, 3, 6, 2, 8],
          [5, 1, 9, 3, 2, 6, 8, 7, 4],
          [2, 4, 8, 9, 5, 7, 1, 3, 6],
          [7, 6, 3, 4, 1, 8, 2, 5, 9]]                     #sample2
import numpy as np

sudoku = np.asarray(sudoku)                                #convert list to matrix
countcheck_9(sudoku)                                       #check repeatation
sudoku_trans= sudoku.transpose()                           #transpose the matrix
countcheck_9(sudoku_trans)                                 #check repeatation

for n in range(0,7,3):                                     #create 3*3 matrices
    for i in range(n,n+3):
        sudoku3_3 = []
        for m in range(0,7,3):
            for j in range(m,m+3):
                sudoku3_3.append(sudoku[i][j])
        sudoku3_3 = np.asarray(sudoku3_3)
        sudoku3_3=sudoku3_3.reshape(3,3)
        countcheck_3(sudoku3_3)                             #check repeatation
        sudoku3_3= sudoku3_3.transpose()
        countcheck_3(sudoku3_3)                             #check repeatation
