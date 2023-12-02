"""Starting Slide."""

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

    image_path = "assets/hunger-games.png"
    og_back = pygame.image.load(image_path)
    background = pygame.transform.scale(og_back, (width, height))
    back_rect = background.get_rect()

    text_color = (255, 255, 255)
    font = pygame.font.Font(None, 36)
    box_x, box_y = (width - width) // 2, 160
    text_x, text_y = box_x, box_y

    text_surface = font.render("Start", True, text_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        screen.blit(background, back_rect)
        screen.blit(shrek, shrek_rect)
        text_rect = text_surface.get_rect(topleft=(text_x, text_y))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

pygame.quit()
