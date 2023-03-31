import random
class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.satiety = 0
        self.play = 1
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.satiety += 0.15
        self.happiness -= 20
        self.play -= 0.2


    def to_sleep(self):
        print("I will sleep")
        self.happiness += 3
        self.play -= 0.2

    def to_chill(self):
        print("Rest time")
        self.happiness += 5
        self.satiety -= 0.2
        self.play += 0.5

    def is_alive(self):
        if self.satiety < -0.5:
            print("Emaciated…")
            self.alive = False
        elif self.happiness <= 0:
            print("Depression…")
            self.alive = False
        elif self.satiety > 5:
            print("Fat…")
            self.alive = False
        elif self.play < 0:
            print("Sad…")
            self.alive = False



    def end_of_day(self):
        print(f"Happiness = {self.happiness}")
        print(f"Satiety = {round(self.satiety, 2)}")
        print(f"Play = {self.play}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

    def to_play(self):
        print("I will to play")
        self.happiness += 0.5
        self.happiness += 5
        self.satiety -= 0.2
        self.play += 0.5

cat = Student(name="Cat")
dog = Student(name="Dog")
for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)
    if dog.alive == False:
        break
    dog.live(day)