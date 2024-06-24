import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))

# Load the OGG file
sound_C5 = pygame.mixer.Sound("piano/Piano.ff.C5.ogg")
sound_Db5 = pygame.mixer.Sound("piano/Piano.ff.Db5.ogg")
sound_D5 = pygame.mixer.Sound("piano/Piano.ff.D5.ogg")
sound_Eb5 = pygame.mixer.Sound("piano/Piano.ff.Eb5.ogg")
sound_E5 = pygame.mixer.Sound("piano/Piano.ff.E5.ogg")

sound_F5 = pygame.mixer.Sound("piano/Piano.ff.F5.ogg")
sound_Gb5 = pygame.mixer.Sound("piano/Piano.ff.Gb5.ogg")
sound_G5 = pygame.mixer.Sound("piano/Piano.ff.G5.ogg")
sound_Ab5 = pygame.mixer.Sound("piano/Piano.ff.Ab5.ogg")
sound_A5 = pygame.mixer.Sound("piano/Piano.ff.A5.ogg")
sound_Bb5 = pygame.mixer.Sound("piano/Piano.ff.Bb5.ogg")
sound_B5 = pygame.mixer.Sound("piano/Piano.ff.B5.ogg")

sound_C6 = pygame.mixer.Sound("piano/Piano.ff.C6.ogg")
sound_Db6 = pygame.mixer.Sound("piano/Piano.ff.Db6.ogg")
sound_D6 = pygame.mixer.Sound("piano/Piano.ff.D6.ogg")
sound_Eb6 = pygame.mixer.Sound("piano/Piano.ff.Eb6.ogg")
sound_E6 = pygame.mixer.Sound("piano/Piano.ff.E6.ogg")

sound_F6 = pygame.mixer.Sound("piano/Piano.ff.F6.ogg")
sound_Gb6 = pygame.mixer.Sound("piano/Piano.ff.Gb6.ogg")
sound_G6 = pygame.mixer.Sound("piano/Piano.ff.G6.ogg")
sound_Ab6 = pygame.mixer.Sound("piano/Piano.ff.Ab6.ogg")
sound_A6 = pygame.mixer.Sound("piano/Piano.ff.A6.ogg")
sound_Bb6 = pygame.mixer.Sound("piano/Piano.ff.Bb6.ogg")
sound_B6 = pygame.mixer.Sound("piano/Piano.ff.B6.ogg")
sound_C7 = pygame.mixer.Sound("piano/Piano.ff.C7.ogg")
sound_D7 = pygame.mixer.Sound("piano/Piano.ff.D7.ogg")
sound_E7 = pygame.mixer.Sound("piano/Piano.ff.E7.ogg")

sounds = {
    pygame.K_q: sound_C5,
    pygame.K_2: sound_Db5,
    pygame.K_w: sound_D5,
    pygame.K_3: sound_Eb5,
    pygame.K_e: sound_E5,
    pygame.K_r: sound_F5,
    pygame.K_5: sound_Gb5,
    pygame.K_t: sound_G5,
    pygame.K_6: sound_Ab5,
    pygame.K_y: sound_A5,
    pygame.K_7: sound_Bb5,
    pygame.K_u: sound_B5,
    pygame.K_i: sound_C6,
    pygame.K_9: sound_Db6,
    pygame.K_o: sound_D6,
    pygame.K_0: sound_Eb6,
    pygame.K_p: sound_E6,
    pygame.K_LEFTBRACKET: sound_F6,
    pygame.K_EQUALS: sound_Gb6,
    pygame.K_RIGHTBRACKET: sound_G6,
    pygame.K_BACKSLASH: sound_Ab6,
    pygame.K_a: sound_A6,
    pygame.K_s: sound_Bb6,
    pygame.K_d: sound_B6,
    pygame.K_f: sound_C7,
    pygame.K_g: sound_D7,
    pygame.K_h: sound_E7,
}

num_channels = len(sounds)
pygame.mixer.set_num_channels(num_channels)

# Map keys to channels
channels = {key: pygame.mixer.Channel(index) for index, key in enumerate(sounds.keys())}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds:
                channels[event.key].play(sounds[event.key])


pygame.quit()
