nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
# Brutforce
def countoccurennce__(nums,target):
    n=len(nums)
    first=-1
    last=-1

    for i in range(0,n):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i

    if first == -1:
        return 0
    return (last-first)+1

class Solution:
    def lowerbound(self, nums, target):
        n = len(nums)
        ib = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ib = mid
                high = mid - 1
            else:
                low = mid + 1

        return ib

    def upperbound(self, nums, target):
        n = len(nums)
        ub = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub

    def firstlast2__(self, nums, target):
        IB = self.lowerbound(nums, target)

        if IB == len(nums) or nums[IB] != target:
            return 0

        UB = self.upperbound(nums, target)

        return UB - IB
obj=Solution()
print(obj.firstlast2__(nums,3))
