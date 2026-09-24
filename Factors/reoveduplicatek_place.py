nums=[3,9,5,6,7,2]

def rightrotatek(nums):
    n=len(nums)

    temp=nums[n-1]
    i=n-2
    while i<-1:
        nums[i]!=nums[i+1]

    return nums

print(rightrotatek(nums))