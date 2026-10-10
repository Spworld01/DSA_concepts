# nums=[5,4,-1,7,8]

def maximumsubarray__(nums):
    n=len(nums)

    maxi=0
    total=0

    for i in range(0,n):
        total=0
        total=nums[i]

        for j in range(i+1,n):
            total+=nums[j]

            if total>=0:
                if total>maxi:
                    maxi=total

    return maxi

# print(maximumsubarray__(nums))


def maximumsubbarray__(nums):
    n=len(nums)

    total=0
    maxi=0

    for i in range(0,n):
        total+=nums[i]

        if total<0:
            total=0

        else:
            maxi=max(total,maxi)
    return maxi

# print(maximumsubbarray__(nums))

# nums=[7,1,5,3,6,4]

def stcokbuysell__(nums):
    n=len(nums)

    stock=float("inf")
    buy=float("-inf")

    for i in range(0,n):
        if nums[i]<stock:
            stock=nums[i]


            for j in range(i+1,n):
                if nums[j]>buy:
                    buy=nums[j]

    return buy-stock

# print(stcokbuysell__(nums))


nums= [7,1,5,3,6,4]
def stockbuyandsell__(nums):
    n=len(nums)

    buy=0
    stock=float("inf")

    for i in range(0,n):
        stock=min(nums[i],stock)

        buy=max(buy,nums[i]-stock)

    return buy

print(stockbuyandsell__(nums))


