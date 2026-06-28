import pygame

from code.Entity import Entity


class Player(Entity):
    def __init__(self,name:str, position:tuple ):
        super().__init__(name,position)

        self.ground_y = position[1]

        self.gravity = 1
        self.jump_force = -15
        self.velocity_y =0
        self.speed_y = 0
        self.on_ground = True







    def update(self):
        self.move()



    def move(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y > self.ground_y:
            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.on_ground = True


    def jump (self):
        if self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False