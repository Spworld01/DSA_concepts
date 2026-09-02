def palindrome(num):
    n=num
    result=0

    while num>0:
        id=num%10
        result=(result*10)+id
        num=num//10

    return n==result

print(palindrome(121))