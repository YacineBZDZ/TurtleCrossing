import  turtle  as  t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.speedup = MOVE_INCREMENT


    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = t.Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars :
            car.backward(self.speedup)
    def UpLvl(self):
            self.speedup += MOVE_INCREMENT