import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Sound Effects
flap_sound = pygame.mixer.Sound("soundboard\\flap.mp3")
flappy_bird_hit_sound = pygame.mixer.Sound("soundboard\\flappy_bird_hit.mp3")
point_sound = pygame.mixer.Sound("soundboard\\point.mp3")

def play_flap_sound():
    flap_sound.play()

def play_hit_sound():
    flappy_bird_hit_sound.play()

def play_point_sound():
    point_sound.play()
