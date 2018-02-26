import pygame, random


class thing():
    def __init__(self,thing_startx, thing_starty, thing_speed, thing_width, thing_height, color, thing_increase_speed, thing_increase_width):
        self.thing_startx =  thing_startx
        self.thing_starty = thing_starty
        self.thing_speed = thing_speed
        self.thing_width = thing_width
        self.thing_height = thing_height
        self.thing_color = color
        self.thing_increase_speed = thing_increase_speed
        self.thing_increase_width = thing_increase_width




    def draw_thing(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.thing_color, [self.thing_startx, self.thing_starty, self.thing_width, self.thing_height])

    def change_thing_startx(self, display_width):
        self.thing_startx = random.randrange(0, display_width)

    def change_thing_starty_speed(self):
        self.thing_starty += self.thing_speed

    def change_thing_starty_reset(self):
        self.thing_starty = 0 - self.thing_height


    def change_thing_speed(self):
        if self.thing_speed < 25:
            self.thing_speed += self.thing_increase_speed

    def change_thing_width(self):
        self.thing_width += self.thing_increase_width

    def change_thing_height(self):
        pass

    def change_thing_color(self, new_color):
        self.thing_color = new_color