#to calculate profit or loss amount

print(" enter cost price and selling price:")
cost_price=int(input())
selling_price=int(input())

profit= selling_price-cost_price

if(profit>=0):print("the profit is:",profit)
else: print("the loss is:",-profit)