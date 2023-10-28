from turtle import Turtle
import random
COLORS = ["red", "blue", "purple", "yellow", "green", "orange", "pink"]
CAR_MOVEMENT = 5
MOVEMENT_INCREMENT = 2

class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_MOVEMENT

    def car_create(self):
        random_nr = random.randint(1, 6)
        if random_nr == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-220, 220)
            new_car.goto(x=250, y=random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for x in self.all_cars:
            x.backward(self.car_speed)



    def accelerate(self):
        self.car_speed += MOVEMENT_INCREMENT




































