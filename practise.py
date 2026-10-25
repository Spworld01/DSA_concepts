# n=5873
# num=n
# while num>0:
#     last=num%10
#     print(last)
#     num=num//10


# n=5438
# num=n
# count=0
# while num>0:
#     count+=1
#     num=num//10
# print(count)

n=1234
num=n
result=0
while num>0:
    id=num%10
    result=(result*10)+id
    num=num//10
# print(n==result)


n=1234
num=n
while num>0:
    id=num%10
    result=result+(id*10)
    num=num//10
# print(n==result)


from math import sqrt
num=4
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
    if num//i!=i:
        result.append(num//i)

    result.sort()
# print(result)


nums=[5,6,7,8,1,9,111,1,1,5,1,1]
freq_map=dict()
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
# print(freq_map)


hash_map=dict()
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
# print(hash_map)


count=0
def func():
    global count

    if count==4:
        return 
    # print("Anirudh")
    count+=1
    func()
func()


count=0
def func():
    global count
    if count==4:
        return 
    count+=1
    func()
    # print("Anirudh")
func()


nums = [1, 7, 8, 4, 5, 6, 9, 2]

def selection_sort1(nums):
    n=len(nums)

    for i in range(0,n):
        mini_index=i

        for j in range(i+1,n):
            if nums[j]<nums[mini_index]:
                mini_index=j


        nums[i],nums[mini_index]=nums[mini_index],nums[i]

    return nums




def selection_sort2(nums):
    n=len(nums)

    for i in range(0,n):
        mini_index=i

        for j in range(i+1,n):
            if nums[j]>nums[mini_index]:
                mini_index=j
        nums[i],nums[mini_index]=nums[mini_index],nums[i]
    return nums

nums=[5,8,1,6,9,2,4]
def bubble_sort(nums):
    n=len(nums)

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        

    return nums


def bubble_sort2(nums):
    n=len(nums)

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums


nums1=[1,2,3,4,5,7,6,8,9,10]
def bubble_sort3(nums):
    n=len(nums)

    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True

        if is_swap==False:
            print("True")
        else:
            print("False")

print(bubble_sort3(nums1))

    
        