numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# double the numbers using map and lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)



class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year    
    def describe(self):
        return f"{self.year} {self.make} {self.model}"  
car1 = car("Toyota", "Camry", 2020)
car2 = car("Honda", "Civic", 2019)
print(car1.describe())
print(car2.describe())  

car_age = lambda car: 2026 - car.year
print(f"{car1.describe()} is {car_age(car1)} years old.")





class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def discount(self, percentage):
        return self.price * (1 - percentage)

products = [
    Product("Laptop", 999.99, "Electronics"),
    Product("Smartphone", 499.99, "Electronics"),
    Product("Headphones", 19.99, "Audio"),
    Product("Keyboard", 89.99, "Accessories"),
    Product("Mouse", 14.99, "Accessories"),
]

# Filter under $20
cheap = list(filter(lambda p: p.price < 20, products))
print("Under $20:")
for p in cheap:
    print(f"  {p.name}: ${p.price:.2f}")

# Sort by price
sorted_products = sorted(products, key=lambda p: p.price)
print("\nSorted by price:")
for p in sorted_products:
    print(f"  {p.name} ({p.category}): ${p.price:.2f}")