# 1. Move all zeros to the end

nums = [0, 1, 0, 3, 12]

def move_all(nums):
    if len(nums)==1:
        return nums

    i=0
    while i<len(nums):
        if nums[i]==0:
            break

        i+=1

    if i==(len(nums)):
        return nums

    j=i+1

    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1

    return nums

print(move_all(nums))

2. Move all zeros to the beginning
nums = [1, 0, 3, 0, 5, 2]

def remove_zero(nums):
    n=len(nums)

    if len(nums)==1:
        return nums

    i=n-1

    while i>=0:
        if nums[i]==0:
            break

        i-=1

    if i==-1:
        return nums
    
    j=i-1

    while j>=0:
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i-=1

        j-=1

    return nums

print(remove_zero(nums))