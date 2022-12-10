import sys
from random import randint

import pygame
from pygame.math import Vector2

COLOUR_BG = (175, 215, 70)
COLOUR_FRUIT = (183, 111, 122)
COLOUR_SNAKE = (126, 166, 114)

MAX_FPS = 60
CELL_SIZE, CELL_NUMBER = 40, 20


class Fruit:
    def __init__(self):
        self.random_place()

    def draw(self):
        # 建立rect用来当做fruit的container
        fruit_rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        # 画fruit
        pygame.draw.rect(canva, COLOUR_FRUIT, fruit_rect)

    def random_place(self):
        self.x = randint(0, CELL_NUMBER - 1)
        self.y = randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(canva, COLOUR_SNAKE, block_rect)

    @property
    def head(self):
        return self.body[-1]

    def move(self):
        current_head = self.head
        new_head = current_head + self.direction
        new_body = self.body[1:]
        new_body.append(new_head)
        self.body = new_body[:]

    def grow(self):
        current_head = self.head
        new_head = current_head + self.direction
        self.body.append(new_head)


class SnakeGame:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()

    def update(self):
        self.snake.move()
        self.check_eat()
        self.check_fail()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def check_eat(self):
        if self.fruit.pos == self.snake.head:
            # 蛇变长一节
            self.snake.grow()
            # 重新摆放水果
            self.fruit.random_place()

    def check_fail(self):
        # 蛇头有没有出界
        if (
            not 0 <= self.snake.head.x < CELL_NUMBER
            or not 0 <= self.snake.head.y < CELL_NUMBER
        ):
            self.game_over()
        # 蛇头有没有撞自己
        for block in self.snake.body[:-1]:
            if block == self.snake.head:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 150)

snake_game = SnakeGame()

canva = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            snake_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_game.snake.direction != Vector2(0, 1):
                    snake_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if snake_game.snake.direction != Vector2(0, -1):
                    snake_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if snake_game.snake.direction != Vector2(1, 0):
                    snake_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if snake_game.snake.direction != Vector2(-1, 0):
                    snake_game.snake.direction = Vector2(1, 0)

    # 渲染
    canva.fill(COLOUR_BG)
    snake_game.draw()
    pygame.display.update()
    clock.tick(MAX_FPS)
