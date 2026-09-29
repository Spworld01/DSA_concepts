# 1. Merge Two Sorted Arrays (Without Duplicates)

nums1 = [1, 2, 2, 4, 6]
nums2 = [2, 3, 4, 5, 7]

def mergetwo_sortarray1(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    result=[]

    i=0
    j=0

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

print(mergetwo_sortarray1(nums1,nums2))

# 2. Merge Two Sorted Arrays (With Duplicates)

nums1 = [1, 3, 5, 7]
nums2 = [2, 3, 6, 7, 8]

def mergetwosot_array2(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    result=[]
    i=0
    j=0

    while i<n and j<m:
        if nums1[i]<nums2[j]:
            result.append(nums1[i])
            i+=1

        else:
            result.append(nums2[j])
            j+=1

    while i<n:
        result.append(nums1[i])
        i+=1

    while j<m:
        result.append(nums2[j])
        j+=1

    return result

print(mergetwosot_array2(nums1,nums2))

3. Find the Union of Two Sorted Arrays

nums1 = [1, 1, 2, 3, 4, 5]
nums2 = [2, 3, 4, 4, 5, 6]

def mergetwosort_array(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    result=[]

    i=0
    j=0

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

print(mergetwosort_array(nums1,nums2))

# 4. Find the Intersection of Two Sorted Arrays
nums1 = [1, 2, 2, 3, 4, 5]
nums2 = [2, 2, 3, 5, 6]

def mergesortarray_4(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    i=0
    j=0

    result=[]

    while i<n and j<m:
        if nums1[i]==nums2[j]:
            if  len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
            j+=1

        elif nums1[i]<nums2[j]:
            i+=1

        else:
            j+=1

    return result

print(mergesortarray_4(nums1,nums2))


 