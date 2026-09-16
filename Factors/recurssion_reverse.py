num=[5,7,3,2,6,1,5,9]
def func(nums,left,right):
    if left>=right:
        return nums
    nums[left],nums[right]=nums[right],nums[left]
    return func(nums,left +1,right-1)

print(func(num,0,7))

