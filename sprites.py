import pygame
import random

class Bird:
    def __init__(self, WIDTH, HEIGHT):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -10
        self.width = 40  # Width without loading the image yet
        self.height = 30  # Height without loading the image yet

    def load_image(self):
        self.image = pygame.image.load("bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def show(self, screen):
        screen.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))

    def update(self, HEIGHT):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

        if self.y > HEIGHT:
            self.y = HEIGHT
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def jump(self):
        self.velocity += self.lift


class Pipe:
    def __init__(self, WIDTH, HEIGHT):
        self.gap = 200
        self.top = random.randint(100, HEIGHT - self.gap - 100)
        self.bottom = self.top + self.gap
        self.x = WIDTH
        self.w = 80  # Width without loading the image yet
        self.h = 400  # Height without loading the image yet
        self.speed = 3
        self.passed = False

    def load_image(self):
        self.image = pygame.image.load("pipe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def show(self, screen):
        screen.blit(self.image, (self.x, self.top - self.h))
        screen.blit(pygame.transform.flip(self.image, False, True), (self.x, self.bottom))

    def update(self):
        self.x -= self.speed

    def offscreen(self, WIDTH):
        return self.x < -self.w