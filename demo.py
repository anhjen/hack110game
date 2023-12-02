import pygame, sys

from random import randint

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

LIGHT_BLUE = (51, 153, 255)
RED = (240, 20, 20)
GOLD = (255, 204, 0)

pygame.init()

clock = pygame.time.Clock()

player = pygame.Rect(5, height/2, 100, 100)

running = True

obstacle_top = pygame.Rect(0, -150, width , height/2)
obstacle_bottom = pygame.Rect(0, height/2 + 150, width, height/2)

obstacle_list = [obstacle_top, obstacle_bottom]

goal = pygame.Rect(width -75, height/2, 50, 50)

collision_count = 0
coin_count = 0

pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(LIGHT_BLUE)

    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, obstacle_top)
    pygame.draw.rect(screen, RED, obstacle_bottom)

    pygame.draw.circle(screen, GOLD, goal.center, goal.width +50)

    for obstacle in obstacle_list:
        if player.colliderect(obstacle):
            pygame.mouse.set_pos(5, height/2)
            collision_count += 1
            if collision_count == 100:
                running = False
    
    if player.colliderect(goal):
        coin_count += 1
        goal.centerx = random.randit(75, width -75)
        if coin_count == 10:
            print("You won! Slay!")
            runnning = False
    

    player.center = pygame.mouse.get_pos()

    pygame.display.flip()

    clock.tick(60)
