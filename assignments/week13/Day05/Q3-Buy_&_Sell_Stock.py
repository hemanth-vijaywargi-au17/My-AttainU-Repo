def maxProfit(prices):
    left = 0    # Buying Price
    right = 1   # Selling Price
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:    # If Profitable Update Max_Profit
            max_profit = max(max_profit, prices[right]-prices[left])
        else:
            left = right    # Set Buying Price to the lesser Selling Price

        right += 1

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
