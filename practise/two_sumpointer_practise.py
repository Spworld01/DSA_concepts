# Question 2: Check if a Pair Exists
# nums = [3, 5, 1, 7]


# def two_pointersum(nums,target):
#     n=len(nums)

#     freq={}

#     for i in range(0,n):
#         remaining=target-nums[i]
#         if remaining in freq:
#             return True

#         else:
#             freq[nums[i]]=i

#     return False

# print(two_pointersum(nums,9))


# Question 3: Find the Pair of Numbers
# nums = [4, 6, 2, 8]

# def find_pairs(nums,target):
#     n=len(nums)

#     freq={}

#     for i in range(0,n):
#         remaining=target-nums[i]
#         if remaining in freq:
#             return [remaining,nums[i]]
#         freq[nums[i]]=i

# print(find_pairs(nums,10))

# nums = [1, 5, 7, -1, 5]

# def count_pairs(nums,target):
#     n=len(nums)

#     freq={}
#     count=0

#     for i in range(0,n):
#         remaining=target-nums[i]
#         if remaining in freq:
#             count+=1
#         freq[nums[i]]=i

#     return count

# print(count_pairs(nums,6))


# Question 5: Find the First Pair of Indices
nums = [1, 4, 3, 2, 5]

def countfirst_pair(nums,target):
    n=len(nums)

    freq={}

    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in freq:
            return [freq[remaining],i]
        freq[nums[i]]=i

print(countfirst_pair(nums,6))