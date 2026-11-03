# # n=5873
# # num=n
# # while num>0:
# #     last=num%10
# #     print(last)
# #     num=num//10


# # n=5438
# # num=n
# # count=0
# # while num>0:
# #     count+=1
# #     num=num//10
# # print(count)

# n=1234
# num=n
# result=0
# while num>0:
#     id=num%10
#     result=(result*10)+id
#     num=num//10
# # print(n==result)


# n=1234
# num=n
# while num>0:
#     id=num%10
#     result=result+(id*10)
#     num=num//10
# # print(n==result)


# from math import sqrt
# num=4
# result=[]
# for i in range(1,int(sqrt(num))+1):
#     if num%i==0:
#         result.append(i)
#     if num//i!=i:
#         result.append(num//i)

#     result.sort()
# # print(result)


# nums=[5,6,7,8,1,9,111,1,1,5,1,1]
# freq_map=dict()
# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#     else:
#         freq_map[nums[i]]=1
# # print(freq_map)


# hash_map=dict()
# n=len(nums)
# for i in range(0,n):
#     hash_map[nums[i]]=hash_map.get(nums[i],0)+1
# # print(hash_map)


# count=0
# def func():
#     global count

#     if count==4:
#         return 
#     # print("Anirudh")
#     count+=1
#     func()
# func()


# count=0
# def func():
#     global count
#     if count==4:
#         return 
#     count+=1
#     func()
#     # print("Anirudh")
# func()


# nums = [1, 7, 8, 4, 5, 6, 9, 2]

# def selection_sort1(nums):
#     n=len(nums)

#     for i in range(0,n):
#         mini_index=i

#         for j in range(i+1,n):
#             if nums[j]<nums[mini_index]:
#                 mini_index=j


#         nums[i],nums[mini_index]=nums[mini_index],nums[i]

#     return nums




# def selection_sort2(nums):
#     n=len(nums)

#     for i in range(0,n):
#         mini_index=i

#         for j in range(i+1,n):
#             if nums[j]>nums[mini_index]:
#                 mini_index=j
#         nums[i],nums[mini_index]=nums[mini_index],nums[i]
#     return nums

# nums=[5,8,1,6,9,2,4]
# def bubble_sort(nums):
#     n=len(nums)

#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
        

#     return nums


# def bubble_sort2(nums):
#     n=len(nums)

#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             if nums[j]<nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]

#     return nums


# nums1=[1,2,3,4,5,7,6,8,9,10]
# def bubble_sort3(nums):
#     n=len(nums)

#     for i in range(n-2,-1,-1):
#         is_swap=False
#         for j in range(0,i+1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 is_swap=True

#         if is_swap==False:
#             print("True")
#         else:
#             print("False")

# nums=[3,4,5,6,7,8,9,10,1]

# def insertion_sort(nums):
#     n=len(nums)

#     for i in range(n):
#         key=nums[i]
#         j=i-1

#         while j>=0 and nums[j]<key:
#             nums[j+1]=nums[j]
#             j-=1

#         nums[j+1]=key
#     return nums
# nums=[1,3,6,7,3,5,9,10,2]

# nums = [1, 3, 6, 7, 5, 9, 10, 2]

# def merge_sort(nums):

#     if len(nums)<=1:
#         return nums

#     mid=len(nums)//2

#     left_array=nums[:mid]
#     right_array=nums[mid:]

#     left=merge_sort(left_array)
#     right=merge_sort(right_array)

#     return merge_arrray(left,right)

# def merge_arrray(left,right):
#     result=[]
#     i,j=0,0
#     n,m=len(left),len(right)
    
#     while i<n and j<m:
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1

#     while i<n:
#         result.append(left[i])
#         i+=1
#     while j<m:
#         result.append(right[j])
#         j+=1

#     return result

# arr=[10,7,8,9,1,5]

# def quicksort(arr,low,high):
#     if low<high:
#         p_ind=partition(arr,low,high)

#         quicksort(arr,low,p_ind-1)
#         quicksort(arr,p_ind+1,high)

#     return arr

# def partition(arr,low,high):
#     pivot=arr[low]

#     i=low
#     j=high

#     while i<j:
#         while arr[i]>=pivot and i<high:
#             i+=1
#         while arr[j]<pivot and j>low:
#             j-=1

#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]

#     arr[low],arr[j]=arr[j],arr[low]

#     return j




# nums=[0,0,1,1,1,2,2,3,3,4]

# def removeduplicaate_(nums):
#     n=len(nums)

#     if len(nums)<1:
#         return 1

#     i=0
#     j=i+1

#     while j<n:
#         if nums[i]!=nums[j]:
#             i+=1
#             nums[i],nums[j]=nums[j],nums[i]
            
#         j+=1

#     return i+1




# nums1=[1,2,4,0,3,0,0,3,5,1]

# def movezero__(nums):
#     n=len(nums)

#     i=0
    

#     while i<n:
#         if nums[i]==0:
#             break
#         i+=1
    
#     if i==n:
#         return nums 
    

#     j=i+1

#     while j<n:
#         if nums[j]!=0:
#             nums[i],nums[j]=nums[j],nums[i]
#             i+=1

#         j+=1
    
#     return nums


# def linearsearch__(nums,target):
#     n=len(nums)

#     for i in range(n):
#         if nums[i]==target:
#             return i
#         return -1

# nums3=[5,9,1,2,4,15,6,3]

# def twosum__(nums, target):
#     n = len(nums)

#     hash_map = {}

#     for i in range(n):
#         remaining = target - nums[i]

#         if remaining in hash_map:
#             return [hash_map[remaining], i]

#         hash_map[nums[i]] = i

    
# nums=[-2,+1,-3,4,-1,2,1,-5,4]

# def maximunsub(nums):
#     n=len(nums)
#     maxi=float("-inf")
#     for i in range(0,n):
#         total=0
#         for j in range(i,n):
#             total=total+nums[j]
#             maxi=max(maxi,total)
#         return maxi
 

# def maximumsubarray2(nums):
#     n=len(nums)

#     maxi=float("-inf")
#     total=0
#     for i in range(0,n):
#         total=total+nums[i]
#         maxi=max(maxi,total)
#         if total<0:
#             total=0

#     return maxi


# nums5=[7,1,5,3,6,4]

# def stockbuysell_(nums):
#     n=len(nums)

#     lowest=0
#     Low=float("+inf")
#     profit=float("-inf")

#     for i in range(0,n):

#         lowest=nums[i]
#         Low=min(lowest,Low)

#         profit=max(profit,nums[i]-Low)

#     return profit


# num4=[5,10,-3,-1,10,6]

# def Rearrange(nums):
#     n=len(nums)

#     pos=[]
#     neg=[]

#     for i in range(0,n):
#         if nums[i]>=0:
#             pos.append(nums[i])
#         else:
#             neg.append(nums[i])
    
#     for i in range(0,len(pos)):
#         nums[2*i]=pos[i]
#         nums[(2*i)+1]=neg[i]
#     return nums



# matrix=[]
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         value=int(input())
#         row.append(value)

#     matrix.append(row)


# def dmatrix_():
#     rows=int(input("Enter a rows:"))
#     cols=int(input("enter a cols:"))

#     matrix2=[]

#     for i in range(rows):
#         value=list(map(int,input().split()));
#         matrix2.append(value)

#     return matrix2

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # def matrix3_(nums):

# #     rows=len(nums)
# #     cols=len(nums[0])

# #     for i in range(rows):
# #         for j in range(0,cols):
# #             print(nums[i][j],end=" ")
# #         print()

# # print(matrix3_(nums))






# # nums = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]

# # rows = len(nums)
# # cols = len(nums[0])

# # for i in range(rows):
# #     for j in range(cols):
# #         if i + j == cols - 1:
# #             print(nums[i][j], end=" ")
        
        
# # for i in range(rows):
# #     print(nums[i][cols - 1 - i], end=" ")


# # nums = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
# # result=[]
# # r=len(nums)
# # c=len(nums[0])

# # for i in range(c):
# #     row=[]
# #     for j in range(r):
# #         row.append(nums[j][i])
# #     result.append(row)
# 1. Find the transpose of a matrix

Input=[[1, 2, 3],[4, 5, 6]]

def matrix__(matrix):
    row=len(matrix)
    cols=len(matrix[0])

    result=[[0] *row for _ in range(cols)]
    for i in range(row):
        for j in range(cols):
            result[j][i]=matrix[i][j]

    return result

# 2. Search in a 2D Matrix
matrix3= [[1, 3, 5],
          [7, 9, 11],
          [13, 15, 17]]


def searchmatrix__(matrix,target):
    row=len(matrix)
    cols=len(matrix)

    for i in range(row):
        for j in range(cols):
            if matrix[i][j]==target:
                return True

    return False

print(searchmatrix__(matrix3,3))