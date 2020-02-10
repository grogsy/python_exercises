# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def max_profit(prices):
    profit = 0


    # for i in range(len(prices) - 1):
    #     local_max = max(prices[i + 1:])
    #     if local_max - prices[i] > profit:
    #         profit = local_max - prices[i]
    # return profit

    # optimized solution
    if not prices:
        return 0

    lowest = prices[0]
    for i in range(len(prices)):
        if prices[i] > lowest:
            if prices[i] - lowest > profit:
                profit = prices[i] - lowest
        else:
            lowest = prices[i]

    return profit
