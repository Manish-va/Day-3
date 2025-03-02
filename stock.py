def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
#prices = [7, 1, 5, 3, 6, 4]
prices= [2 , 7, 5, 1, 8]
print(maxProfit(prices))  