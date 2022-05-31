weight = 41.5
flat_charge = 20.00
flat_charge_premium = 125.00

# Ground Shipping
if weight <= 2 and weight > 0:
  cost = (weight * 1.50) + flat_charge
  print("The cost using Ground Shipping: $", cost)
  print("The cost using Premium Ground Shipping: $", flat_charge_premium)
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + flat_charge
  print("The cost using Ground Shipping: $", cost)
  print("The cost using Premium Ground Shipping: $", flat_charge_premium)
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00) + flat_charge
  print("The cost using Ground Shipping: $", cost)
  print("The cost using Premium Ground Shipping: $", flat_charge_premium)
elif weight > 10:
  cost = (weight * 4.75) + flat_charge
  print("The cost using Ground Shipping: $", cost)
  print("The cost using Premium Ground Shipping: $", flat_charge_premium)
else:
  print("Error")

#Drone Shipping

if weight <= 2 and weight > 0:
  cost = (weight * 4.50)
  print("The cost using Drone Shipping: $", cost)
elif weight > 2 and weight <= 6:
  cost = (weight * 9.00)
  print("The cost using Drone Shipping: $", cost)
elif weight > 6 and weight <= 10:
  cost = (weight * 12.00)
  print("The cost using Drone Shipping: $", cost)
elif weight > 10:
  cost = (weight * 14.25)
  print("The cost using Drone Shipping: $", cost)
else:
  print("Error")