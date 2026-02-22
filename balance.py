amount = 50000
item_price = 3700
balance = amount-item_price 
print(f"Balance is {balance}")
	
	
if (balance <= 0):
	print(f"no more coins: {balance}")
else:
	coins_1000 = (balance // 1000)
	print(f" Coins of 1000 are {coins_1000}")
		
	coins_500 = (balance - coins_1000) // 500
	print(f" Coins of 500 are {coins_500}")
	
	coins_200 = (balance - coins_500) // 200
	print(f" Coins of 200 are {coins_200}")
	
	coins_100 = (balance - coins_200) // 100
	print(f" Coins of 100 are {coins_100}")
	 