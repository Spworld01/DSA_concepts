nums=[55,32,-97,99,3,67]

def largest(nums):
    n=len(nums)
    largest=nums[0]

    for i in range(0,n):
        if largest<nums[i]:
            largest=nums[i]

    return largest

print(largest(nums))

def largest2(nums):
    n=len(nums)
    largest=nums[0]

    for i in range(0,n):
        largest=max(largest,nums[i])

    return largest

# print(largest2(nums))

def largest3(nums):
    n=len(nums)
    largest=float("-inf")

    for i in range(0,n):
        largest=max(largest,nums[i])

    return largest

print(largest3(nums))