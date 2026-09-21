# 1. Basic Insertion Sort

# nums = [7, 3, 5, 2, 9, 1]

# def insertionsort1(nums):
#     n=len(nums)

#     for i in range(1,n):
#         key=nums[i]
#         j=i-1

#         while j>=0 and nums[j]>key:
#             nums[j+1]=nums[j]
#             j-=1

#         nums[j+1]=key

#     return nums

# print(insertionsort1(nums))

# 2. Descending Order
# nums = [4, 8, 1, 9, 3, 6]

# def insertionsort2(nums):
#     n=len(nums)

#     for i in range(1,n):
#         key=nums[i]
#         j=i-1

#         while j>=0 and nums[j]<key:
#             nums[j+1]=nums[j]
#             j-=1

#         nums[j+1]=key

#     return nums

# print(insertionsort2(nums))

# 3. Sort Only the First k Elements
# nums = [8, 3, 6, 2, 9, 1]

# def insertionsort3(nums,k):
#     n=len(nums)

#     for i in range(1,k):
#         key=nums[i]
#         j=i-1

#         while j>=0 and nums[j]>key:
#             nums[j+1]=nums[j]
#             j-=1

#         nums[j+1]=key

#     return nums

# print(insertionsort3(nums,3))

# 4. Find the Kth Smallest Element

# nums= [7, 2, 9, 4, 1, 6]

# def insertionsort4_(nums,k):
#     n=len(nums)

#     for i in range(1,n):
#         key=nums[i]
#         j=i-1

#         while j>=0 and nums[j]>key:
#             nums[j+1]=nums[j]
#             j-=1

#         nums[j+1]=key


#     print(nums)
#     return nums[k-1]

# print(insertionsort4_(nums,3))

# 5. Insertion Sort Without Creating Another List
nums = [5, 3, 8, 6, 2, 9, 1]

def insertionsort5(nums):
    n=len(nums)

    for i in range(1,n):
        key=nums[i]
        j=i-1

        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1

        nums[j+1]=key

    return nums

print(insertionsort1(nums))
