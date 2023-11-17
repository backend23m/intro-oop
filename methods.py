class Mobile:
    total_price = 0
    instances = []

    def __init__(self, name: str, ram: int, memory: int, color: str, price: float, brend: str, quantity: int):
        self.name     = name
        self.ram      = ram
        self.memory   = memory
        self.color    = color
        self.price    = price
        self.brend    = brend
        self.quantity = quantity

        Mobile.total_price += self.total()
        Mobile.instances.append(self)

    def info(self) -> str:
        """get info about mobile

        Returns:
            str: description
        """
        return f"{self.name} costs {self.price}"

    def total(self) -> float:
        """get total price

        Returns:
            float: price
        """        
        return self.price * self.quantity

m1 = Mobile(name='Samsung s21', ram=6, memory=128, color='black', price=800.00, brend='Samsung', quantity=12)
m2 = Mobile(name='Iphone 14', ram=6, memory=256, color='gray', price=900.00, brend='Iphone', quantity=7)

print(Mobile.total_price)
print(Mobile.instances)

print(m1.total())