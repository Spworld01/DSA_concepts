# 1. Bubble Sort — Descending
nums = [5, 8, 1, 6, 9, 2, 4]

def bubble_sortdes(nums):
    n=len(nums)

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums


print(bubble_sortdes(nums))

# 2. Bubble Sort — Count Swaps
nums = [5, 1, 4, 2]

def bubble_sortcount(nums):
    n=len(nums)
    count=0

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                count+=1

    return count

print(bubble_sortcount(nums))

# 3. Bubble Sort — Already Sorted Check
nums=[1, 2, 3, 4, 5]

def bubble_sortcheck(nums):
    n=len(nums)

    for i in range(n-2,-1,-1):
        is_swaaped=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swaaped=True

        if is_swaaped==False:
            break

    return nums

print(bubble_sortcheck(nums))

# 4. Bubble Sort — Sort Only First K Elements

nums = [5, 3, 8, 1, 2, 9]

def bubble_sortk(num,k):
    n=len(nums)

    for i in range(k-1,-0,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums

print(bubble_sortk(nums,4))



# 5. Bubble Sort — Find the Kth Largest

nums =[5, 8, 1, 6, 9, 2, 4]

def bubble_sortkth(nums,k):
    n=len(nums)
    

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    
    print(nums)
    return nums[n-k]

print(bubble_sortkth(nums,3))
