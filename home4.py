class Mother:
    def __init__(self, age, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age
        self.height = 168

class Father:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hobby = "Play volleyball"
class GrandFather:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hobby = "Play volleyball"

class GrandMother:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hobby = "Play volleyball"
class Child(Mother, Father):
    def print_info(self):
        print(self.age)
        print(self.hobby)
        print(self.height)
dan = Child(age ="32 old")
dan.print_info()