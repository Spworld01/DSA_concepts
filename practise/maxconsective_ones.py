
nums=[1,0,1,1,0,1,1,1]
class Solution:
    def findMaxConsectiveones(self,nums:list[int])->int:
        n=len(nums)

        maxi=0
        count=0

        i=0
        while i<n:
            if nums[i]==1:
                count+=1
            else:
                maxi=max(maxi,count)
                count=0

            i+=1

        return max(count,maxi)
sol=Solution()
print(sol.findMaxConsectiveones(nums))

        