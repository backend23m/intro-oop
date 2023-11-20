class Tortburchak(object):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b


class Kvadrat(Tortburchak):
    def __init__(self, a: float):
        super().__init__(a, a)

    def __str__(self):
        return f"{self.a}X{self.b}"

    def __gt__(self, s):
        return self.area()


k1 = Kvadrat(434123432)
k2 = Kvadrat(5)

s = "fdsafdsafasdfadsfads"

print(k1.__sizeof__())
print(s.__sizeof__())
