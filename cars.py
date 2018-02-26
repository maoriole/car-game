import pygame

class car():
    def __init__(self, car_width, car_height, x, y, car_img):
        self.car_width = car_width
        self.car_height = car_height
        self.x = x
        self.y = y
        self.car_img = car_img
    #return var

    def draw_car(self, gameDisplay):
        gameDisplay.blit(self.car_img, (self.x, self.y))

    def move_car(self, x_change, y_change):
        self.x += x_change

        self.y += y_change