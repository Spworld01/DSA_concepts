nums = [3,9,5,6,7,2,10,9]

def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1


n=len(nums)
k=3
k=k%n

reverse(nums,0,n-1)
reverse(nums,0,k-1)
reverse(nums,k,n-1)


print(nums)