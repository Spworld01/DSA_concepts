nums=[-2,1,-3,4,-1,2,1,-5,4]

def subarray_(nums):
    n=len(nums)

    maxi=float("-inf")
    for i in range(0,n):
        total=0
        for j in range(i,n):
            total=total+nums[j]
            maxi=max(maxi,total)

    return maxi

print(subarray_(nums))




def Subarray_2(nums):
    n=len(nums)

    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)

        if total<0:
            total=0

    return maxi

print(Subarray_2(nums))

# 1. Maximum Subarray Sum
nums1= [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def Subarray_(nums):
    n=len(nums)

    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)

        if total<0:
            total=0

    return maxi

print(Subarray_(nums1))


# 2. Maximum Sum of a Subarray of Size K
nums = [2, 1, 5, 1, 3, 2]

def Subarray_3(nums):
    n=len(nums)

    maxi=float("-inf")
    total=0
    size=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)
        size+=1

        if size==3:
            size=0
            total=0

    return maxi

print(Subarray_3(nums))
            
