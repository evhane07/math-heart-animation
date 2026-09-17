import math
import random
import sys
import pygame

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cœur Mathématique Animé (Parametric Heart)")
clock = pygame.time.Clock()


def heart_function(t, scale=15):
    """Équation paramétrique classique du cœur"""
    x = 16 * (math.sin(t) ** 3)
    y = -(
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )
    return x * scale, y * scale


class Particle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.uniform(1.5, 3.5)
        self.alpha = random.randint(150, 255)
        self.color = (255, random.randint(50, 120), random.randint(100, 180))
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, 0.5)


    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.alpha -= 2
        
              
    def draw(self, surface):
        if self.alpha > 0:
            s = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(
                s,
                (*self.color, max(0, self.alpha)),
                (self.size, self.size),
                self.size,
            )
            surface.blit(s, (self.x - self.size, self.y - self.size))