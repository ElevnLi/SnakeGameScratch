import os
import sys

import pygame

MAX_FPS = 60
BG_GREEN = (175, 215, 70)


pygame.init()
canva = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 100))
test_surface.fill(pygame.Color('red'))
snake_head_right = pygame.image.load(os.path.join('./', 'Assets', 'Graphics', 'head_right.png')).convert_alpha()
snake_head_up = pygame.image.load(os.path.join('./', 'Assets', 'Graphics', 'head_up.png')).convert_alpha()
test_rect = pygame.Rect(100, 100, 100, 200)

x = 400

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 运算
    x = x + 1
    test_rect.top -= 1
    # 渲染
    canva.fill(BG_GREEN)
    canva.blit(snake_head_right, (x, 300))
    canva.blit(snake_head_up, test_rect)
    pygame.display.update()
    clock.tick(MAX_FPS)