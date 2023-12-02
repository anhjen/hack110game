"""Interactive Hunger Games Based Movie."""

import pygame, sys

pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hunger Games")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    image_path = "VillageBG.png"
    image = pygame.image.load(image_path)
    image_rect = image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((200, 200, 200)) 
        screen.blit(image, image_rect)
        pygame.display.flip()
pygame.quit()
