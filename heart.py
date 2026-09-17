import math
# import random
# import sys
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
