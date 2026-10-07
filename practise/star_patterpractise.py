def starpattern_(n):

    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print()



def starpattern2_(n):

    for i in range(0,n):
        for j in range(0,i):
            print("*",end="")
        print()



def starpattern3_(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()


def starpattern4_(n):
    for i in range(0,n):
        for j in range(1,i):
            print(j,end="")
        print()



def starpattern5_(n):

    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end="")
        print()


def starpatter6_(n):

    for i in range(0,n):

        for j in range(0,n-i-1):
            print(" ",end="")

        for k in range(0,2*i+1):
            print("*",end="")
        print()


def starpatter7_(n):

    for i in range(n,-1,-1):

        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,2*i+1):
            print("*",end="")
        print()

def pattern9(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")
            for k in range(0,2*i+1):
                print("*",end="")
            print()

            

    # for m in range(0,n):
    #     for n in range(0,n-1):
    #         print(" ",end="")
    #         for o in range(0,2*i+1):
    #             print("*",end="")

            
print(pattern9(10))





