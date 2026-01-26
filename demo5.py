prices = [7, 6, 4, 3, 1]

mi = min(prices)
max_profit = 0

if prices.index(mi) == len(prices) - 1:
    print(0)

for i in range(prices.index(mi) + 1, len(prices)):
    if prices[i] > max_profit:
        max_profit = 0
        max_profit += prices[i]
    
    

print(max_profit - mi)