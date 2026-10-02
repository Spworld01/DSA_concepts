nums=[7,2,1,5,6,4,8]

def StockBuy_sell(prices):
    n=len(prices)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                p=prices[j]-prices[i]
                max_profit=max(max_profit,p)

    return max_profit

print(StockBuy_sell(nums))


def Stock_Buysell(prices):
    n=len(prices)

    max_profit=0
    min_profit=float("inf")

    for i in range(0,4):
        min_profit=min(min_profit,nums[i])

        max_profit=max(max_profit,prices[i]-min_profit)

    return max_profit

print(Stock_Buysell(nums))