def Armstrong_(num):
    n=num
    total=0
    nod=len(str(num))

    while num>0:
        digit=num%10
        total=total+(digit**nod)
        num=num//10

    return total==n

print(Armstrong_(153))

# Write a function armstrong_count(num) that counts how many Armstrong numbers exist from 1 to num.
def countarmstrong_(num):
    count=0

    for i in range(1,num):
        n=i
        nod=len(str(i))
        total=0

        while i>0:
            digit=i%10
            total=total+(digit**nod)
            i=i//10

        if n==total:
            count+=1

    return count

print(countarmstrong_(500))

# Given a list of numbers, return only the Armstrong numbers.
nums = [153, 10, 370, 25, 371, 100, 407]
def armstrongnumber_(num):
    armstrong=[]

    for i in num:
        n=i
        nod=len(str(i))
        total=0

        while i>0:
            digit=i%10
            total=total+(digit**nod)
            i=i//10

        if n==total:
            armstrong.append(n)

    return armstrong

print(armstrongnumber_(nums))

# Find the largest Armstrong number in a list.
nums= [153, 370, 10, 407, 371, 9474, 100]
def largestarmstrong(num):
    largest=0

    for i in num:
        n=i
        nod=len(str(i))
        total=0

        while i>0:
            digit=i%10
            total=total+(digit**nod)
            i=i//10

        if n==total:
            if n>largest:
                largest=n

    return largest

print(largestarmstrong(nums))

# Find the smallest Armstrong number greater than n

def smallestarmstrong_(num):

    while True:
        n=num
        nod=len(str(num))
        total=0

        while num>0:
            digit=num%10
            total=total+(digit**nod)
            num=num//10

        if n==total:
            print(n)
        
        num=n+1

print(smallestarmstrong_(150))

# Find all Armstrong numbers between two given numbers without using any built-in Armstrong-related function.

def betweenarmstrong(start,end):

    for i in range(start,end+1):
        n=i
        nod=len(str(i))
        total=0

        while i>0:
            digit=i%10
            total=total+(digit**nod)
            i=i//10

        if n==total:
            print(n)

print(betweenarmstrong(1,10000))


