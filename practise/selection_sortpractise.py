# 1. Sort in Descending Order
numsf = [5, 2, 8, 1, 9, 3]

def des_selectionsort(nums):
    n=len(nums)

    for i in range(0,n):
        max_index=i

        for j in range(i+1,n):
            if nums[j]>nums[max_index]:
                max_index=j

        nums[i],nums[max_index]=nums[max_index],nums[i]

    return nums


print(des_selectionsort(numsf))

# 2. Find the Smallest Element Using Selection Sort
nums = [10, 3, 7, 1, 8, 2, 5]

def smallest_selectionsort(nums):
    n=len(nums)
    smallest=0

    for i in range(0,n):
        mini_index=i

        for j in range(i+1,n):
            if nums[j]<nums[mini_index]:
                mini_index=j

        nums[i],nums[mini_index]=nums[mini_index],nums[i]


    return nums[1]



print(smallest_selectionsort(nums))

# . Count the Number of Swaps
nums = [5, 4, 3, 2, 1]

def countSwap__(nums):
    n=len(nums)
    swap=0

    for i in range(0,n):
        mini_index=i

        for j in range(i+1,n):
            if nums[j]<nums[mini_index]:
                mini_index=j


        if mini_index!=i:
            nums[i],nums[mini_index]=nums[mini_index],nums[i]
            swap+=1

    return (nums,swap)

print(countSwap__(nums))

# 5. Selection Sort Without Creating a New List


nums= [12, 5, 8, 3, 10, 1, 7]

def des_selectionsort(nums):
    n=len(nums)

    for i in range(0,n):
        max_index=i

        for j in range(i+1,n):
            if nums[j]<nums[max_index]:
                max_index=j

        nums[i],nums[max_index]=nums[max_index],nums[i]

    return nums


print(des_selectionsort(nums))


    


