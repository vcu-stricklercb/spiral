def spiralize(number):
    n=501
    Spiralmatrix= None
    Spiralmatrix_first_diagonal = sum(Spiralmatrix[i][i] for i in range(n))
    Spiralmatrix_second_diagonal = sum(Spiralmatrix[i][n-i-1] for i in range(n)) - 1
    print(str(Spiralmatrix_first_diagonal)+" "+str(Spiralmatrix_second_diagonal)) 
    Value = Spiralmatrix_first_diagonal + Spiralmatrix_second_diagonal
    print(Value)
