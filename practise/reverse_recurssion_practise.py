# 1. Reverse a List — Beginner
# nums = [1, 2, 3, 4, 5]
# def reverse_recurssion(nums,left,right):
#     if left>=right:
#         return nums

#     nums[left],nums[right]=nums[right],nums[left]
#     return reverse_recurssion(nums,left+1,right-1)

# print(reverse_recurssion(nums,0,4))
# 2. Reverse Only a Part of a List
# nums = [10, 20, 30, 40, 50, 60, 70]
# def reversepart(nums,left,right):
#     if left>=right:
#         return  nums

#     nums[left],nums[right]=nums[right],nums[left]
#     return reversepart(nums,left+1,right-1)

# print(reversepart(nums,2,5))

# 3. Reverse a String Using Recursion
s=list("hello")

def reversestring(str,left,right):
    if left>=right:
        return "".join(str)

    str[left],str[right]=str[right],str[left]
    
    return reversestring(str,left+1,right-1)

print(reversestring(s,0,len(s)-1))

