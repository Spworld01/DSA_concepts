# 1. Maximum Consecutive Zeros
# nums=[1, 0, 0, 1, 0, 0, 0, 1]


# def Maxconsective_ones(nums):
#     n=len(nums)

#     maxi=0
#     count=0

#     for i in range(0,n):
#         if nums[i]==0:
#             count+=1

#         else:
#             maxi=max(maxi,count)
#             count=0

        

#     return max(maxi,count)

# print(Maxconsective_ones(nums))

# 2. Count Consecutive Ones Groups

# Input=[1, 1, 0, 1, 1, 1, 0, 1]

# def Consective_zeros(nums):
#     n=len(nums)

#     maxi=0
#     count=0

#     for i in range(0,n):
#         if nums[i]==1:
#             count+=1

#         else:
#             maxi=max(maxi,count)
#             count=0

#     return max(maxi,count)

# print(Consective_zeros(Input))

# 3. Maximum Consecutive Equal Elements
# Input=[1, 1, 2, 2, 2, 3, 3, 1]

# def maximum_consective(nums):
#     n=len(nums)

#     maxi=0
#     count=1

#     for i in range(1,n):
#         if nums[i]==nums[i-1]:
#             count+=1

#         else:
#             maxi=max(maxi,count)
#             count=1

#     return max(maxi,count)
# print(maximum_consective(Input))

# 4. Longest Subarray of Ones After at Most One Flip
Input=[1, 0, 1, 1, 0, 1]

def longest_subarray(nums):
    n=len(nums)

    left=0
    right=left+1
    while left<n and right<n:
        if 

print(longest_subarray(Input))