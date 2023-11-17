class Mobile:
    total_price = 0
    inctances = []

    def __init__(self, name: str, ram: int, memory: int, color: str, price: float, brend: str, quantity: int):
        self.name     = name
        self.ram      = ram
        self.memory   = memory
        self.color    = color
        self.price    = price
        self.brend    = brend
        self.quantity = quantity

        Mobile.total_price += self.total()
        Mobile.inctances.append(self)

    def info(self) -> str:
        return f"{self.name} costs {self.price}"

    def total(self) -> float:
        return self.price * self.quantity

m1 = Mobile(name='Samsung s21', ram=6, memory=128, color='black', price=800.00, brend='Samsung', quantity=12)
m2 = Mobile(name='Iphone 14', ram=6, memory=256, color='gray', price=900.00, brend='Iphone', quantity=7)

print(Mobile.total_price)
print(Mobile.inctances)
