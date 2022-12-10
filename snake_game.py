import sys

import pygame

MAX_FPS = 60
BG_GREEN = (175, 215, 70)

pygame.init()
canva = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 渲染
    canva.fill(BG_GREEN)
    pygame.display.update()
    clock.tick(MAX_FPS)