nums=[5,6,7,7,1,9,111,1,1,5,1,1]
def Hashing_(nums):
    hash_map={}
    n=len(nums)

    for i in range(0,n):
        hash_map[nums[i]]=hash_map.get(nums[i],0)+1

    return hash_map


print(Hashing_(nums))

