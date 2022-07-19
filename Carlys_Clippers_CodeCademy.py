# Creating list of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Creating list of prices
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# The number of purchases for each hairstyle last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
 
print("Average Haircut Price: " , average_price)

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]

print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7

print(average_daily_revenue)