class Laptop:
    
    def __init__(self, brand, model, price, ram):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        
    def __str__(self):
        return f"{self.brand} {self.model} and price is {self.price} and has {self.ram}GB RAM"
    
l1 = Laptop('Dell', 'D1534', 35000, 4)
l2 = Laptop('HP', 'P123', 25000, 2)
l3 = Laptop('Lenovo', 'L345', 30000, 4)

laptops = [l1, l2, l3]

laptops.sort(key=lambda x: x.ram)

for laptop in laptops:
    print(laptop)