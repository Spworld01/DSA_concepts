# Brutforce
nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]

def firstandlast_(nums,target):
    n=len(nums)
    first=-1
    last=-1
    for i in range(n):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i
    return [first,last]
print(firstandlast_(nums,3))

class Solution:
    def lowerbond_(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        ib=-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ib=mid
                high=mid-1
            else:
                low=mid+1
        return ib
    
    def upperbond__(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        up=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                up=mid
                high=mid-1
            else:
                low=mid+1

        return up

    def firstlast2__(self,nums,target):
        Ib=self.lowerbond_(nums,target)
        if Ib==-1:
            return [-1,-1]
        Up=self.upperbond__(nums,target)

        return [Ib,Up-1]
obj=Solution()
print(obj.firstlast2__(nums,3))