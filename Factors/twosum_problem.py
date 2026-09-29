nums=[5,9,1,2,4,15,6,3]

def two_sumpointer(nums,target):
    n=len(nums)

    hash_map={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i

print(two_sumpointer(nums,11))