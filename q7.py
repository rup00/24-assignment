class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print("Brand:", self.brand,
              "\nRAM:", self.ram,
              "\nCPU:", self.cpu,
              "\nHDD:", self.hdd)


l1 = Laptop('Dell', '4GB', 'i5', '1TB')
l1.showConfig()