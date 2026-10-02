# Question 1: Maximum Profit (Basic)
prices = [7, 1, 5, 3, 6, 4]

def Stock_prices(nums):
    n=len(nums)

    max_prices=0
    min_prices=float("inf")

    for i in range(0,n):
        min_prices=min(min_prices,nums[i])

        max_prices=max(max_prices,nums[i]-min_prices)

    return max_prices

print(Stock_prices(prices))

# Question 2: Maximum Profit with Buy and Sell Days
prices1=[3, 8, 1, 9, 2, 10]


def Stock_prices2(prices):
    n=len(prices)

    max_prices=0
    min_prices=float("inf")
    
    buy_index=-1
    sell_index=-1
    min_index=-1

    for i in range(0,n):
        
        if prices[i]<min_prices:
            min_prices=preces[i]
            min_index=i

        profit=prices[i]-min_prices

        if profit>max_profit:
            max_profit=profit
            buy_index=min_index
            sell_index=i
            

        

        max_prices=max(max_prices,prices[i]-min_prices)

        dicti[prices[i]]=i

    
    return

print(Stock_prices2(prices1))

