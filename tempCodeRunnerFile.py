def dmatrix_():
    rows=int(input("Enter a rows:"))
    cols=int(input("enter a cols:"))

    matrix2=[]

    for i in range(rows):
        value=list(map(int,input().split()));
        matrix2.append(value)

    return matrix2

print(dmatrix_())