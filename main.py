import pygame
import random
import time
import os

CHANCE = 15000  # chance por segundo (1 em X)
FRAME_RATE = 30  # framerate do jumpscare

def load_frames(folder):
    frames = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            path = os.path.join(folder, file)
            img = pygame.image.load(path)
            frames.append(img)
    return frames

def show_jumpscare(frames, sound):
    # Cria a janela só durante o jumpscare
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")

    sound.play()
    clock = pygame.time.Clock()

    for frame in frames:
        frame = pygame.transform.scale(frame, (screen.get_width(), screen.get_height()))
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    time.sleep(0.3)
    pygame.display.quit()  # fecha a janela

def main():
    pygame.init()
    pygame.mixer.init()  # inicializa o mixer antes de criar o Sound

    frames = load_frames("frames")
    sound = pygame.mixer.Sound("jumpscare.mp3")  # agora o mixer já está inicializado

    while True:
        time.sleep(1)
        if random.randint(1, CHANCE) == 1:
            show_jumpscare(frames, sound)

if __name__ == "__main__":
    main()
