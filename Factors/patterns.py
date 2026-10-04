for i in range(0,4):
    for j in range(0,4):
        print("*",end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    print()

for i in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print()


for i in range(1,6+1):
    for j in range(1,6-i+1):
        print(j,end="")
    print()