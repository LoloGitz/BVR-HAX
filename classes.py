class Person:
    def  __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    
    def birthday(self, years: int):
        for i in range(years):
            self.age += 1
            plural = ""
            if (self.age != 1):
                plural = "s"

            print("happy birthday! you're " + str(self.age) + " year" + plural + " old now.")

    def get_info(self) -> tuple[str, int]:
        return self.name, self.age


p = Person("Lawrence", 15)

name, age = p.get_info()
print(name, age)

p.birthday(5)

print(p.get_info())

