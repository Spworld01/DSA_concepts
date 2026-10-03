# 1.largest_element

# nums=[55,32,-97,99,3,67]

# def largest_element(nums):
#     n=len(nums)
#     largest=float("inf")

#     for i in range(0,n):
#         if nums[i]<largest:
#             largest=nums[i]

#     return largest

# print(largest_element(nums))

# 2.find the 2nd largest element in an array/list

# nums=[12, 35, 1, 10, 34, 1]

# def second_largest(nums):
#     n=len(nums)

#     largest=float("-inf")
#     second=float("-inf")

#     for i in range(0,n):
#         if nums[i]>largest:
#             second=largest
#             largest=nums[i]

#         elif nums[i]>second and nums[i]!=largest:
#             second=nums[i]

#     return second
# print(second_largest(nums))

# Question 3: Find the Second Smallest Element
# nums = [8, 3, 15, 1, 9, 2]

# def second_smallest(nums):
#     n=len(nums)

#     first=float("inf")
#     second=float("inf")

#     for i in range(0,n):
#         if nums[i]<first:
#             second=first
#             first=nums[i]

#         elif nums[i]<second and nums[i]!=first:
#             second=nums[i]

#     return second

# print(second_smallest(nums))

# Question 4: Find the Largest and Smallest Elements Together
# nums = [45, 12, 89, -5, 34, 67]

# def largest_smallest(nums):
#     n=len(nums)

#     largest=float("-inf")
#     smallest=float("inf")
    
#     for i in range(0,n):
#         if nums[i]>largest:
#             largest=nums[i]

#         if nums[i]<smallest:
#             smallest=nums[i]

#     return (largest,smallest)

# print(largest_smallest(nums))

# Question 5: Find the Third Largest Distinct Element
# nums = [10, 5, 20, 8, 20, 15, 10]

# def third_largest(nums):

#     n=len(nums)
#     largest=float("-inf")
#     second=float("-inf")
#     third=float("-inf")

#     for i in range(0,n):
#         if nums[i]>largest:
#             third=second
#             second=largest
#             largest=nums[i]

#         elif nums[i]>second and nums[i]!=largest:
#             second=nums[i]
#         elif nums[i]>third and nums[i]!=second and nums[i]!=largest:
#             third=nums[i]

#     return third

# print(third_largest(nums))

nums=[1,1,1,2,3,4,4,7,9,9,10]

# def remove_duplicate_(nums):
#     n=len(nums)

#     hash={}
#     k=0
#     for i in range(0,n):
#         hash[nums[i]]=0

#     for j in hash:
#         k+=1


#     return k

# print(remove_duplicate_(nums))

# def remove_dupicate(nums):
#     n=len(nums)

#     if n==1:
#         return nums

#     i=0
#     j=i+1
#     while j<n:
#         if nums[i]!=nums[j]:
#             i+=1
#             nums[i],nums[j]=nums[j],nums[i]

#         j+=1

#     return i+1

# print(remove_dupicate(nums))

nums=[3,1,-2,-5,2,-4]
def rearrange(nums):
    n=len(nums)

    positive=[]
    negative=[]

    for i in range(0,n):
        if nums[i]>0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])

    add=positive+negative

    i=0
    j=i+1
    while j<n:
        if nums[i]>0 and nums[j]<0:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]

        j+=1

    return add

print(rearrange(nums))