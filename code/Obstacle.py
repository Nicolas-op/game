from code.Const import WIN_WIDTH
from code.Entity import Entity

class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.speed= 5
        self.active = True

    def move(self):
        if not self.active:
            return

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.active = False
