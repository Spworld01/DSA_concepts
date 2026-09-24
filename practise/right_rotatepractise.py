# 1. Right rotate by 1
# nums = [1, 2, 3, 4, 5]

# def rightrotate(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# n=len(nums)
# k=1
# k=k%n

# rightrotate(nums,0,n-1)
# rightrotate(nums,0,k-1)
# rightrotate(nums,k,n-1)

# print(nums)

# 2. Right rotate by k
# nums= [1, 2, 3, 4, 5, 6, 7]

# def rightrotatek_(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# n=len(nums)
# k=3
# k=k%n

# rightrotatek_(nums,0,n-1)
# rightrotatek_(nums,0,k-1)
# rightrotatek_(nums,k,n-1)

# print(nums)

# 3. k is greater than the array length
# nums = [1, 2, 3, 4, 5]

# def greaterthanarray_(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# n=len(nums)
# k=7
# k=k%n

# greaterthanarray_(nums,0,n-1)
# greaterthanarray_(nums,0,k-1)
# greaterthanarray_(nums,k,n-1)
# print(nums)

# 4. Handle k = 0
nums = [10, 20, 30, 40, 50]

def handle_k(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

n=len(nums)
k=0
k=k%n

handle_k(nums,0,n-1)
handle_k(nums,0,k-1)
handle_k(nums,k,n-1)
print(nums)
