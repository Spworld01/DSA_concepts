# 1. Smallest Element
nums = [55, 32, -97, 99, 3, 67]

def smallestelement(nums):
    n=len(nums)
    smallest=nums[0]

    for i in range(0,n):
        if smallest>nums[i]:
            
            smallest=nums[i]

    return smallest

print(smallestelement(nums))

# 2. Second Largest Element

nums = [55, 32, -97, 99, 3, 67]

def second_largest(nums):
    n=len(nums)
    largest=nums[0]
    second=nums[0]

    for i in range(0,n):
        if largest<nums[i]:
            second=largest
            largest=nums[i]

        if nums[i]>second and nums[i]<largest:
            second=nums[i]

    return second

print(second_largest(nums))

# 3. Largest Positive Number

nums = [-10, 25, -3, 99, 4, -50]

def largestpositive_(nums):
    n=len(nums)
    largest=nums[0]

    for i in range(0,n):
        if largest<nums[i] and nums[i]>0:
            largest=nums[i]

    return largest

print(largestpositive_(nums))

# 4. Largest Even Number

nums = [55, 32, -97, 98, 3, 67, 100, 42]

def largest_even(nums):
    n=len(nums)
    largesteven=nums[0]

    for i in range(0,n):
        if nums[i]%2==0 and nums[i]>largesteven:
            largesteven=nums[i]

    return largesteven

print(largest_even(nums))

# 5. Largest and Smallest Together


nums = [55, 32, -97, 99, 3, 67]

def largestsmallest(nums):
    n=len(nums)
    largest=nums[0]
    smallest=nums[0]

    for i in range(0,n):
        if nums[i]>largest:
            largest=nums[i]

        if nums[i]<smallest:
            smallest=nums[i]

    return (smallest,largest)

print(largestsmallest(nums))