# Palindrome Check
def palindrome_(num):
    n=num
    result=0

    while num>0:
        id=num%10
        result=(result*10)+id
        num=num//10

    return n==result

print(palindrome_(121))

# Count Palindrome Numbers
number=[121, 123, 22, 45, 11]
def countpalindrome_(num):
    count=0

    for i in num:
        n=i
        result=0

        while i>0:
            digit=i%10
            result=(result*10)+digit
            i=i//10

            if n==result:
                count+=1

    return count

print(countpalindrome_(number))

# Print Palindrome Numbers
def rangepalindrome_(num):
    count=0

    for i in range(0,num):
        n=i
        result=0

        while i>0:
            digit=i%10
            result=(result*10)+digit
            i=i//10

            if n==result:
                count+=1
                print(result)

    return count
print(rangepalindrome_(150))

# Largest Palindrome
number=[121, 45, 1331, 99, 123]
def largestpalindrome_(num):
    largest=0

    for i in num:
        n=i
        result=0

        while i>0:
            id=i%10
            result=(result*10)+id
            i=i//10

            if n==result:
                if n<largest:
                    largest=n

    return largest

print(largestpalindrome_(number))

# Smallest Palindrome
number=[121, 44, 7, 123, 22]

def smallestpalindrome_(num):
    smallest=None

    for i in num:
        n=i
        result=0

        while i>0:
            id=i%10
            result=(result*10)+id
            i=i//10

        if n==result:
            if smallest is None or result<smallest:
                smallest=result

    return smallest

print(smallestpalindrome_(number))
