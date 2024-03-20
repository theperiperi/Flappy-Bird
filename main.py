import pygame
import os
from sprites import Bird, Pipe
from soundboard import play_flap_sound, play_hit_sound, play_point_sound

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Import Sound Effects from soundboard.py
from soundboard import play_flap_sound, play_hit_sound, play_point_sound

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

background_img = pygame.image.load("sprites\\background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

def main():
    bird = Bird(WIDTH, HEIGHT)
    bird.load_image()

    pipes = [Pipe(WIDTH, HEIGHT)]
    for pipe in pipes:
        pipe.load_image()

    clock = pygame.time.Clock()

    score = 0
    game_over = False
    font = pygame.font.Font(None, 36)

    # High Score
    high_score = 0

    # Flag for playing hit sound only once
    hit_sound_played = False

    def reset_game():
        nonlocal bird, pipes, score, game_over, hit_sound_played
        bird = Bird(WIDTH, HEIGHT)
        bird.load_image()

        pipes = [Pipe(WIDTH, HEIGHT)]
        for pipe in pipes:
            pipe.load_image()

        score = 0
        game_over = False
        hit_sound_played = False

    def display_game_over(score, high_score):
        nonlocal hit_sound_played  # Declare as nonlocal to modify the variable from main's scope
        # Play hit sound only once
        if not hit_sound_played:
            play_hit_sound()
            hit_sound_played = True

        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))

        if score > high_score:
            high_score_text = font.render("Woo Hoo! New High Score!", True, BLACK)
        else:
            high_score_text = font.render("Better Luck Next Time!", True, BLACK)
        screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2 + 40))

        play_again_text = font.render("Play Again", True, BLACK)
        play_again_rect = play_again_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        pygame.draw.rect(screen, WHITE, play_again_rect)
        screen.blit(play_again_text, play_again_rect.topleft)

        return play_again_rect

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_over and event.key == pygame.K_SPACE:
                    bird.jump()
                    play_flap_sound()
                elif game_over and event.key == pygame.K_RETURN:
                    reset_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and play_again_rect.collidepoint(event.pos):
                    reset_game()

        if not game_over:
            bird.update(HEIGHT)
            for pipe in pipes:
                pipe.update()

                if not pipe.passed and pipe.x + pipe.w < bird.x - bird.width // 2:
                    pipe.passed = True
                    score += 10

                    # Play point sound for every 10th point (every multiple of 100)
                    if score % 100 == 0:
                        play_point_sound()

                if pipe.offscreen(WIDTH):
                    pipes.remove(pipe)

                if bird.x + bird.width // 2 > pipe.x and bird.x - bird.width // 2 < pipe.x + pipe.w:
                    if bird.y - bird.height // 2 < pipe.top or bird.y + bird.height // 2 > pipe.bottom:
                        game_over = True

            if pipes[-1].x < WIDTH - 150:
                pipes.append(Pipe(WIDTH, HEIGHT))
                pipes[-1].load_image()

        screen.blit(background_img, (0, 0))
        bird.show(screen)
        for pipe in pipes:
            pipe.show(screen)

        if game_over:
            play_again_rect = display_game_over(score, high_score)
        else:
            score_text = font.render("Score: " + str(score), True, BLACK)
            screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
