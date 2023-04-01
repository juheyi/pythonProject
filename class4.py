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
        self.work = "Work in the garden"


class GrandMother:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cook = "Cook sup"


class Child(Mother, Father, GrandFather, GrandMother):
    def print_info(self):
        print(self.age)
        print(self.hobby)
        print(self.height)
        print(self.work)
        print(self.cook)


dan = Child(age="15 old")
dan.print_info()