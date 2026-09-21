
# 1. Basic Merge Sort
# arr = [7, 2, 9, 1, 5, 3]
# def merge_array(arr):
#     if len(arr)<=1:
#         return arr

#     mid=len(arr)//2

#     left_arr=arr[:mid]
#     right_arr=arr[mid:]

#     left=merge_array(left_arr)
#     right=merge_array(right_arr)

#     return merge_sort(left,right)

# def merge_sort(left,right):
#     result=[]

#     i,j=0,0
#     n,m=len(left),len(right)

#     while i<n and j<m:
#         if left[i]<right[j]:
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

# print(merge_array(arr))


# 2. Merge Two Sorted Arrays
# left = [1, 4, 7]
# right = [2, 3, 8]

# def merge_sort2(left,right):
#     result=[]
#     i,j=0,0
#     n,m=len(left),len(right)

#     while i<n and j<m:
#         if left[i]<right[j]:
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

# print(merge_sort2(left,right))

# 3. Merge Sort in Descending Order
# arr = [5, 1, 8, 3, 2, 9]

# def merge_array3(arr):
#     if len(arr)<=1:
#         return arr

#     mid=len(arr)//2

#     left_arr=arr[:mid]
#     right_arr=arr[mid:]

#     left=merge_array3(left_arr)
#     right=merge_array3(right_arr)

#     return merge_sort(left,right)

# def merge_sort(left,right):
#     result=[]

#     i,j=0,0
#     n,m=len(left),len(right)

#     while i<n and j<m:
#         if left[i]>right[j]:
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

# print(merge_array3(arr))

# 4. Count Inversions Using Merge Sort
  
arr = [5, 4, 3, 2, 1]

def merge_sort(arr):
    count=0

    if len(arr)<=1:
        return arr

    mid=len(arr)//2

    left_array=arr[:mid]
    right_array=arr[mid:]

    left=merge_sort(left_array)
    right=merge_sort(right_array)

    
    return merge_array4(left,right)

def merge_array4(left,right):
    result=[]

    i,j=0,0
    n,m=len(left),len(right)


    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while i<n:
        result.append(left[i])
        i+=1

    while j<m:
        result.append(right[j])
        j+=1
    print(count)
    return result


print(merge_sort(arr))



    
