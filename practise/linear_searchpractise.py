# 1. Find the index
nums = [12, 7, 4, 19, 25, 3]

def index_(nums,target):
    n=len(nums)

    for i in range(0,n):
        if nums[i]==target:
            return i

    return -1


print(index_(nums,19))

# 2. Check if element exists

nums = [10, 20, 30, 40, 50]

def element_exists(nums,target):
    n=len(nums)

    for i in range(0,n):
        if nums[i]==target:
            return True
    return False

print(element_exists(nums,35))

# 3. Count occurrences
nums = [5, 2, 5, 8, 5, 9, 5, 1]

def count_occurence(nums,target):
    n=len(nums)
    count=0
    
    for i in range(0,n):
        if nums[i]==target:
            count+=1

    return count

print(count_occurence(nums,5))

# 4. Find the first occurrence
nums = [7, 3, 9, 3, 5, 3, 8]

def first_occurence(nums,target):
    n=len(nums)

    for i in range(0,n):
        if nums[i]==target:
            return i

    return -1

print(first_occurence(nums,3))

# Question 5 — Last occurrence
nums = [4, 8, 2, 8, 9, 8, 1]

def last_occurence(nums,target):
    n=len(nums)
    index=0

    for i in range(0,n):
        if nums[i]==target:
            index=i

    return index

print(last_occurence(nums,8))