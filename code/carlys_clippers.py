hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0 

for price in prices:
    total_price += price

average_price = total_price / len(prices)
#print(total_price)
print(f"Average Haircut Price: {average_price}")

# Use a list comprehension to make a list called new_prices, which has each element in price minus 5.
new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range((len(hairstyles))):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: ${0}".format(total_revenue))

average_daily_revenue = total_revenue / 7

print("Average Daily Revenue: ${0}".format(average_daily_revenue))

# Comprehension list: mylist = [expression, for statement, conditional]
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
prices_under_30 = [new_prices[i] for i in range(len(new_prices)) if new_prices[i] < 30]

cuts_prices_under_30 = list(zip(cuts_under_30, prices_under_30))

# print(cuts_under_30)
# print(prices_under_30)

print(cuts_prices_under_30)