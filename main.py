from agent import Activator, Inhibitor
import random
import pygame
from pygame.locals import *

activators = [
    Activator(random.randint(0,720), random.randint(0,400)),
    Activator(random.randint(0,720), random.randint(0,400)),
    Activator(random.randint(0,720), random.randint(0,400))
]

inhibitors = [
    Inhibitor(random.randint(0,720), random.randint(0,400)),
    Inhibitor(random.randint(0,720), random.randint(0,400)),
    Inhibitor(random.randint(0,720), random.randint(0,400)),
    Inhibitor(random.randint(0,720), random.randint(0,400))
]

def generate_activator_inhibitor():
    chance = random.randint(1,2)
    if chance == 1:
        activators.append(Activator(random.randint(0,720), random.randint(0,400)))
    else:
        inhibitors.append(Inhibitor(random.randint(0,720), random.randint(0,400)))

def check_collision(activators, inhibitors):
    for activator in activators:
        for inhibitor in inhibitors:
            if activator.get_front() == inhibitor.get_front():
                activator.active = False
                print("KIA")


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
display_width = 720
display_height = 400

screen= pygame.display.set_mode((display_width,display_height))
pygame.init()
running = True
screen.fill(black)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(random.randint(1,7) == 3):
        generate_activator_inhibitor()

    for inhibitor in inhibitors:
        inhibitor.propagate()
        pygame.draw.ellipse(screen, red, ( inhibitor.front_x , inhibitor.front_y, 4, 4))

    for activator in activators:
        activator.propagate()
        pygame.draw.ellipse(screen, white, ( activator.front_x , activator.front_y, 4, 4))

    # print("Inhibitors: ", len(inhibitors), ":: Activators: ", len(activators))
    check_collision(activators, inhibitors)
    pygame.display.update()


pygame.quit()
