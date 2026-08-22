#121 Best time to buy and sell a stock 
prices = [7,1,5,3,6,4]
profit=0
min_price=prices[0]
for i in range(1,len(prices)):
    if prices[i]<min_price:
        min_price=prices[i]
    current_profit=prices[i]-min_price

    if current_profit>profit:
        profit=current_profit
print(profit)



        
        
    
