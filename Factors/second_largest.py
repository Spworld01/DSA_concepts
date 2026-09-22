nums=[55,32,97,-55,45,32,88,21]

def second_largest(nums):
    n=len(nums)
    largest=nums[0]
    second=nums[0]

    for i in range(0,n):
        if nums[i]>largest:
            second=largest
            largest=nums[i]

        if nums[i]>second and nums[i]<largest:
            second=nums[i]

    return second

print(second_largest(nums))