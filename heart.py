import math
import random
import turtle

# Configuration de la fenêtre
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cœur Mathématique Animé")

# initialisation du curseur
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

# couleurs des rayons
colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

# Tracé progressif rayon par rayon
for i in range(128):
    t.penup()
    t.goto(0, 68)

    angle = i * (math.pi * 2) / 128
    x = 16 * (math.sin(angle) ** 3) * 15
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 15

    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)

    # étoile au bout de chaque ligne
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()
