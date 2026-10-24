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
    print("Anirudh")
func()