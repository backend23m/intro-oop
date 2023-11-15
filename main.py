class Person:
    class_name = "Person class"
    count = 0
    
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name  = lname
        self.age        = age

        Person.count += 1

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


p1 = Person('Ali', 'Vali', 19)
p2 = Person('Vali', 'Ali', 21)


print(p2.full_name)
