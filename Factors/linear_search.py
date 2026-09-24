nums=[5,3,9,8,1,6,4,-10,-100]

def linear_search(nums,target):
    n=len(nums)

    for i in range(0,n):
        if nums[i]==target:
            return i

    return -1
print(linear_search(nums,4))