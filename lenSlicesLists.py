# Len's Slices:
toppins = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppins)
print("We sell", num_pizzas, "different kind of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
print("The cheapest pizza is:", cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)