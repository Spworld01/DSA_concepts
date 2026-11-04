# Question 2 – Target Sum 3Sum
nums2= [2, -1, 0, 1, -2, 3, 4]
# target = 3
def threesum(nums):
    ans=[]
    n=len(nums)
    nums.sort()
    for i in range(n):
        if i!=0 and nums[i]==nums[i-1]:
            continue

        j=i+1
        k=n-1
        while j<k:
            total_sum=nums[i]+nums[j]+nums[k]
            if total_sum<3:
                j+=1
            elif total_sum>3:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1

    return ans

# Question 3 – 3Sum with Duplicates
nums3 = [-2, -2, -1, 0, 0, 1, 1, 2, 2]

def threesum3(nums,target):
    ans=[]
    n=len(nums)
    nums.sort()
    for i in range(n):
        if i!=0 and nums[i]==nums[i-1]:
            continue

        j=i+1
        k=n-1
        while j<k:
            total_sum=nums[i]+nums[j]+nums[k]
            if total_sum<target:
                j+=1
            elif total_sum>target:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1

    return ans

# Question 4 – Count Triplets
nums4= [1, 2, 3, 4, 5, 6]
def threesum4(nums,target):
    ans=[]
    n=len(nums)
    nums.sort()
    count=0
    for i in range(n):
        # if i!=0 and nums[i]==nums[i-1]:
        #     continue

        j=i+1
        k=n-1
        while j<k:
            total_sum=nums[i]+nums[j]+nums[k]
            if total_sum<target:
                j+=1
            elif total_sum>target:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                count+=1
                j+=1
                k-=1
                # while j<k and nums[j]==nums[j-1]:
                #     j+=1
                # while j<k and nums[k]==nums[k+1]:
                #     k-=1

    return count


# Question 5 – 3Sum Closest Variant
nums5= [-4, -1, 1, 2, 5, 8]
# target = 7

nums5 = [-4, -1, 1, 2, 5, 8]

def threesum5(nums, target):
    n = len(nums)
    nums.sort()

    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(n):
        j = i + 1
        k = n - 1

        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]

            if abs(total_sum - target) < abs(closest_sum - target):
                closest_sum = total_sum

            if total_sum < target:
                j += 1
            elif total_sum > target:
                k -= 1
            else:
                return total_sum

    return closest_sum


print(threesum5(nums5, 7))