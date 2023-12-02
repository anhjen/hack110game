"""Interactive Hunger Games Based Movie."""

import pygame, sys

pygame.init()

size = width, height = 1400, 750
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hunger Games")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    image_path = "assets/FirstScene.png"
    og_back = pygame.image.load(image_path)
    background = pygame.transform.scale(og_back, (width, height))
    back_rect = background.get_rect()

    image_path2 = "assets/Shrek_(character).png"
    og_shrek = pygame.image.load(image_path2)
    shrek = pygame.transform.scale(og_shrek, (width/8, height/3))
    shrek_rect = shrek.get_rect()
    shrek_rect.center = (width/1.6, height/1.4)  

    text_color = (255, 255, 255)
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Hello, Pygame!", True, text_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        screen.blit(background, back_rect)
        screen.blit(shrek, shrek_rect)
        text_rect = text_surface.get_rect(center=back_rect.center)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

pygame.quit()
