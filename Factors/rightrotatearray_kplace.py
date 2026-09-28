nums = [7, 3, 9, 1]

def rightrotate_(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

n=len(nums)
k=9
k=k%n

# rightrotate_(nums,0,n-1)
rightrotate_(nums,0,k-1)
rightrotate_(nums,k,n-1)
rightrotate_(nums,0,n-1)


print(nums)

