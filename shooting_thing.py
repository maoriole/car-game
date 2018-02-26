import pygame

class shoot():
    shooting_counter = 0
    def __init__(self, x, y, color, speed=-5.0, width=10, height=15):
        self.x = x + 23/2 #shooting from the middle of the car
        self.y = y
        self.color = color
        shoot.shooting_counter += 1
        self.speed = speed
        self.width = width
        self.height = height

    def draw_shoot(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color,
                         [self.x, self.y, self.width, self.height])


    def move_shoot(self):
        self.y += self.speed