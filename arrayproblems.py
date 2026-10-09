nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]

def mergesortarray__(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    i=0
    j=0
    result=[]

    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1

    while i<n:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1

    while j<m:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1

    return result
# print(mergesortarray__(nums1,nums2))

nums=[0,1,2,4]
def misssingnumber__(nums):
    n=len(nums)

    for i in range(0,n+1):
        if i not in nums:
            return i

# print(misssingnumber__(nums))


nums=[1,0,3,4]
def missingnumber__(nums):
    n=len(nums)
    sum=0

    for i in range(0,n):
        sum+=nums[i]

    return n*(n+1)//2-sum

# print(missingnumber__(nums))

nums=[10,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0]

def maxconsectiveones_(nums):
    n=len(nums)
    count=0
    highest=0

    for i in range(0,n):
        if nums[i]==0:
            count+=1
        else:
            if count>highest:
                highest=count

            count=0
    
    return max(count,highest)
# print(maxconsectiveones_(nums))

nums=[2,7,11,15]

def twosum__(nums,target):

    n=len(nums)

    i=0
    j=i+1

    while i<n:
        j=i+1

        while j<n:
            if nums[i]+nums[j]==target:
                return (i,j)

            j+=1
        i+=1


print(twosum__(nums,9))


