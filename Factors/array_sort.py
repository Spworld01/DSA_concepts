nums=[3,5,6,8,9,10,20]

def array_sort(nums):
    n=len(nums)

    for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                return False

    return True

print(array_sort(nums))