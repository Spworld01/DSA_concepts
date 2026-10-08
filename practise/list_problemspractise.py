

# def rightrotate_(nums,k):
#     n=len(nums)
 
#     for i in range(0,k):
#         temp=nums[n-1]
#         for j in range(n-2,-1,-1):
#             nums[j+1]=nums[j]

#         nums[0]=temp

#     return nums

# print(rightrotate_(nums,2))


# nums=[3,9,5,6,7,2]

# def rightrotate_(nums,k):
#     n=len(nums)
#     k=k%n

#     def reversearray__(nums,left,right):
#         while left<right:
#             nums[left],nums[right]=nums[right],nums[left]
#             left+=1
#             right-=1

#     reversearray__(nums,0,n-1)
#     reversearray__(nums,0,k-1)
#     reversearray__(nums,k,n-1)

#     return nums

# print(rightrotate_(nums,3))

nums=[1,2,4,0,3,0,0,3,5,1]

def movezero__(nums):
    n=len(nums)
    i=0
    j=i+1

    while i<n:
        if nums[i]==0:
            break
        i+=1
        
        while j<n:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1



    return nums

print(movezero__(nums))