class Tortburchak:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b


class Kvadrat(Tortburchak):
    def __init__(self, a: float):
        super().__init__(a, a)


k = Kvadrat(6)
print(k.area())
