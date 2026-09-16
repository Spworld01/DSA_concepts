def Fibonacci_number(nums):
    if nums==1:
        return 1
    elif nums==0:
        return 0

    return Fibonacci_number(nums-1)+Fibonacci_number(nums-2)

print(Fibonacci_number(1))