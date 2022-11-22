import pygame
import sys
import random

pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()

class Square:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color
    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.length, self.length))

class Food(Square):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, length, color)
    def generate(self):
        self.x = random.randrange(0, 475, 25)
        self.y = random.randrange(0, 475, 25)

class Snake(Square):
    def __init__(self, x, y, length, color, direction):
        super().__init__(x, y, length, color)
        self.direction = direction
    def move(self):
        if self.direction == 1:
            self.x += 25
        elif self.direction == 2:
            self.y += 25
        elif self.direction == 3:
            self.x -= 25
        elif self.direction == 4:
            self.y -= 25

snake_cells = [Snake(150, 225, 25, "green", 1)]
food = Food(350, 225, 25, "red") 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_cells[0].direction != 2 or snake_cells[0].direction != 4:
                    snake_cells[0].direction = 4
            if event.key == pygame.K_RIGHT:
                if snake_cells[0].direction != 1 or snake_cells[0].direction != 3:
                    snake_cells[0].direction = 1
            if event.key == pygame.K_DOWN:
                if snake_cells[0].direction != 2 or snake_cells[0].direction != 4:
                    snake_cells[0].direction = 2
            if event.key == pygame.K_LEFT:
                if snake_cells[0].direction != 1 or snake_cells[0].direction != 3:
                    snake_cells[0].direction = 3

            

    display.fill("black")

    food.draw()

    for cell in snake_cells:
        cell.draw()
        cell.move()
        if cell.x == food.x and cell.y == food.y:
            food.generate()

        if cell.x > 500 or cell.x < 0 or cell.y > 500 or cell.y < 0:
            pygame.quit()
            sys.exit()

    
    
    pygame.display.update()
    clock.tick(8)