import pygame
import sys
import random
import os

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Suppress pygame support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

# Load images with appropriate sizes
bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (40, 30))  # Resize bird image

pipe_img = pygame.image.load("pipe.png").convert_alpha()
pipe_img = pygame.transform.scale(pipe_img, (80, 400))  # Resize pipe image

background_img = pygame.image.load("background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)  # Dark green for pipes

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -10
        self.width = bird_img.get_width()  # Get bird image width
        self.height = bird_img.get_height()  # Get bird image height

    def show(self):
        screen.blit(bird_img, (self.x - self.width // 2, self.y - self.height // 2))

    def update(self):
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
    def __init__(self):
        self.gap = 200
        self.top = random.randint(100, HEIGHT - self.gap - 100)
        self.bottom = self.top + self.gap
        self.x = WIDTH
        self.w = pipe_img.get_width()  # Get pipe image width
        self.h = pipe_img.get_height()  # Get pipe image height
        self.speed = 3
        self.passed = False

    def show(self):
        screen.blit(pipe_img, (self.x, self.top - self.h))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.bottom))

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        return self.x < -self.w

def main():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()

    score = 0
    game_over = False
    font = pygame.font.Font(None, 36)

    def reset_game():
        nonlocal bird, pipes, score, game_over
        bird = Bird()
        pipes = [Pipe()]
        score = 0
        game_over = False

    def display_game_over():
        game_over_text = font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - game_over_text.get_height()//2))

        play_again_text = font.render("Play Again", True, BLACK)
        play_again_rect = play_again_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        pygame.draw.rect(screen, WHITE, play_again_rect)
        screen.blit(play_again_text, play_again_rect.topleft)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_over and event.key == pygame.K_SPACE:
                    bird.jump()
                elif game_over and event.key == pygame.K_RETURN:
                    reset_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and play_again_rect.collidepoint(event.pos):
                    reset_game()

        if not game_over:
            # Update
            bird.update()
            for pipe in pipes:
                pipe.update()

                if not pipe.passed and pipe.x + pipe.w < bird.x - bird.width // 2:
                    pipe.passed = True
                    score += 10

                if pipe.offscreen():
                    pipes.remove(pipe)

                if bird.x + bird.width // 2 > pipe.x and bird.x - bird.width // 2 < pipe.x + pipe.w:
                    if bird.y - bird.height // 2 < pipe.top or bird.y + bird.height // 2 > pipe.bottom:
                        # Collision occurred
                        game_over = True

            # Add new pipes
            if pipes[-1].x < WIDTH - 150:
                pipes.append(Pipe())

        # Display
        screen.blit(background_img, (0, 0))
        bird.show()
        for pipe in pipes:
            pipe.show()

        if game_over:
            display_game_over()
        else:
            score_text = font.render("Score: " + str(score), True, BLACK)
            screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
