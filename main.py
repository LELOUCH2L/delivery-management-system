from delivery_management_system import *

customer1 = Customer("Alice", "X-001")
customer1.introduce()

customer2 = Customer("Bob", "X-002")
customer2.introduce()

driver1 = Driver("David", "motorcycle")
driver1.introduce()

print()

order1 = customer1.place_order("Laptop")
order1.assign_driver(driver1)
print(order1.summary())

print()

order2 = customer2.place_order("Headphones")
order2.assign_driver(driver1)
print(order2.summary())

print()

driver1.deliver(order1)
driver1.deliver(order2)

print()

print("Final Status:")
print(f"Order for {order1.item} → {order1.status}")
print(f"Order for {order2.item} → {order2.status}")
