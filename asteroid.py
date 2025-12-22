import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(surface=screen, color="white",
                            center=self.position,
                            radius=self.radius,
                            width=LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle: float = random.uniform(20, 50)
            v1: pygame.Vector2 = self.velocity.rotate(angle)
            v2: pygame.Vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(*self.position, radius=new_radius)
            asteroid2= Asteroid(*self.position, radius=new_radius)
            asteroid1.velocity = v1 * 1.2
            asteroid2.velocity = v2 * 1.2
        
        