nums = [3, 1, 2, 4, 6, 7, 8]

def quick_sort(nums,low,high):
    if low<high:

        p_ind=partition(nums,low,high)

        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)

def partition(nums,low,high):
    pivot=nums[low]

    i=low
    j=high

    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1

        while nums[j]>pivot and j>low:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]

    return j

quick_sort(nums,0,len(nums)-1)
print(nums)

# 1. Basic Quick Sort
nums = [5, 3, 8, 4, 2, 7, 1, 6]

def  partition(nums,low,high):
    pivot=nums[low]

    i=low
    j=high

    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1

        while nums[j]>pivot and j>low:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]
    return j

partition(nums,0,len(nums)-1)
print(nums)

# 2. Understand Partition

nums = [4, 2, 7, 1, 3, 6, 5]

def quick_sort2(nums,low,high):
    if low<high:
        p_ind=partition2(nums,low,high)

        quick_sort2(nums,low,p_ind)
        quick_sort2(nums,p_ind+1,high)

def partition2(nums,low,high):
    pivot=nums[low]
    i=low
    j=high

    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>low:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]
    return j

quick_sort2(nums,0,len(nums)-1)
print(nums)


# 3. Descending Quick Sort

nums = [5, 1, 8, 3, 2, 7]

def quick_sort3(nums,low,high):
    if low<high:

        p_ind=partition3(nums,low,high)

        quick_sort3(nums,low,p_ind-1)
        quick_sort3(nums,p_ind+1,high)

def partition3(nums,low,high):

    pivot=nums[low]

    i=low
    j=high

    while i<j:
        while i<=high-1 and nums[i]>=pivot:
            i+=1

        while j>=low+1 and nums[j]<pivot:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]

    return j

quick_sort3(nums,0,len(nums)-1)
print(nums)

# 4. Quick Sort with Duplicates

nums = [4, 2, 4, 1, 3, 2, 5, 4]

def quicksort4(nums,low,high):
    if low<high:
        p_ind=partition4(nums,low,high)

        quicksort4(nums,low,p_ind-1)
        quicksort4(nums,p_ind+1,high)

def  partition4(nums,low,high):
    pivot=nums[low]

    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1

        while nums[j]>pivot and j>low:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]

    return j

quicksort4(nums,0,len(nums)-1)
print(nums)

# GFG / Interview Style

arr = [10, 7, 8, 9, 1, 5]

class Solution:
    def quicksort(self,arr,low,high):
        if low<high:
            p_ind=self.partition(arr,low,high)
            self.quicksort(arr,low,p_ind-1)
            self.quicksort(arr,p_ind+1,high)


    def partition(self,arr,low,high):
        pivot=arr[low] 
    

        i=low
        j=high


        while i<j:
            while arr[i]<=pivot and i<=high-1:
                i+=1

            while arr[j]>pivot and j>low:
                j-=1

            if i<j:
                arr[i],arr[j]=arr[j],arr[i]

        arr[low],arr[j]=arr[j],arr[low]

    
        return j


obj=Solution()
obj.quicksort(arr,0,len(arr)-1)
print(arr)
