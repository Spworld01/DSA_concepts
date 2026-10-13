# 1. Basic consecutive sequence

nums = [1, 2, 3, 4, 5]

def longestconsectivenum1__(nums):
    n=len(nums)

    my_set=set()
    for i in range(0,n):
        my_set.add(nums[i])

    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest




# 2. Unsorted array

nums = [100, 4, 200, 1, 3, 2]

def longestconsectivenum2__(nums):
    n=len(nums)

    my_set=set()
    for i in range(0,n):
        my_set.add(nums[i])

    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest





# 3. Duplicates and negative numbers

nums = [0, -1, 1, 2, 2, -2, 5, 6]

def longestconsectivesequence3__(nums):
    n=len(nums)

    my_set=set()
    for num in nums:
        my_set.add(num)
    
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1

            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest



# 4. Multiple sequences
nums = [10, 5, 12, 3, 55, 4, 11, 2]

def longestconsectivesequence4__(nums):
    n=len(nums)

    my_set=set()
    for num in nums:
        my_set.add(num)
    
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1

            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest

# 5. Edge cases and complexity
def longestconsectivesequence5__(nums):
    nums =[9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6]
    n=len(nums)

    my_set=set()
    for num in nums:
        my_set.add(num)
    
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1

            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest

print(longestconsectivesequence5__(nums))
