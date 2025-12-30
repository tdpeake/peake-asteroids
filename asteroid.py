from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_vector = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius -ASTEROID_MIN_RADIUS
            asteroid_baby1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_baby2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_baby1.velocity = new_vector* 1.2
            asteroid_baby2.velocity = new_vector2 * 1.2


