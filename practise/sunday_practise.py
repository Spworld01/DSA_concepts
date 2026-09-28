# To find second Largest 
nums=[55,32,97,-55,32,88,21]

def second_largest(nums):
    n=len(nums)

    largest=nums[0]
    second=nums[0]

    for i in range(0,n):
        if largest<nums[i]:
            second=largest
            largest=nums[i]

        elif nums[i]>second and nums[i]!=largest:
            second=nums[i]

    return second


print(second_largest(nums))