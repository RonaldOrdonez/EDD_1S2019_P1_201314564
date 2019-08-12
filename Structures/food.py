import random

class Food:
    def __init__(self):
        self.x_coordinate = random.randint(0,60)  #genera un random entre 0 y 60 del tamaño del ancho de x
        self.y_coordinate = random.randint(0,20)  #genera un random entre 0 y 20 del alto de la ventan en Y
        typeFood = random.randint(0,100)
        if typeFood <=20:
            self.type_food = 0  #bocadillo malo
        else:  
            self.type_food = 1  #bocadillo bueno
    
    def print(self):
        print("x: ", self.x_coordinate)
        print("y: ", self.y_coordinate)
        print("bocadillo: ", self.type_food)

for x in range(0,10):
    food = Food()
    food.print()