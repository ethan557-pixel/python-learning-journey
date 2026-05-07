name = "Ethan" 
age = 32
city = "Nashville"
new_city = "New York"

print(f"My name is {name}, I am {age} years old, ")
print(f"i live in {city} and I will be {age + 1} years old next year.")
print(f"in 5 years, I will be {age + 5} years old and living in {new_city} and living in a highrise apartment.")



price = 19.999999
discount = 0.15
final_price = price * (1 - discount)


print(f"Original price: ${price:.2f}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")

print(f"{'name':<10} {'score':>10}")
print(f"{'Ethan':<10} {95:>10}")
print(f"{'Jordan':<10} {82:>10}")
print(f"{'Maya':<10} {74:>10}")



def receipt(items):
    print(f"/n{'=' * 30}")
    print(f"{'RECEIPT':^30}")
    print(f"{'=' * 30}")


    total = 0
    for item, price in items.items():
        print(f"{item:<20} ${price:>6.2f}")
        total += price
    print(f"{'=' * 30}")
    print(f"{'TOTAL':<20} ${total:>6.2f}")
    print(f"{'=' * 30}")

order = {
    "Tacos": 8.99,
    "Burrito": 10.99,
    "Quesadilla": 9.99,
    "Cervesa": 3.50,
    "Spicy Peppy": 1.50
}

receipt(order)