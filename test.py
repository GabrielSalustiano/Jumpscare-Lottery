import pygame
import time
import os
import ctypes

FRAME_RATE = 30  # framerate do jumpscare

def load_frames(folder):
    frames = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            path = os.path.join(folder, file)
            img = pygame.image.load(path).convert_alpha()
            frames.append(img)
    return frames

def show_jumpscare(screen, frames, sound):
    sound.play()
    clock = pygame.time.Clock()

    for frame in frames:
        frame = pygame.transform.scale(frame, (screen.get_width(), screen.get_height()))
        screen.fill((0, 0, 0, 0))  # fundo transparente
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(FRAME_RATE)

    time.sleep(1.5)  # pequena pausa final

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.FULLSCREEN)
    pygame.display.set_caption("")

    # Windows: deixa janela transparente se possível
    hwnd = None
    if os.name == "nt":
        ctypes.windll.user32.SetProcessDPIAware()
        wm_info = pygame.display.get_wm_info()
        if 'window' in wm_info:
            hwnd = wm_info['window']

    # deixa janela quase invisível até o jumpscare
    if hwnd:
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 1, 0x02)

    # Carrega frames e som
    frames = load_frames("frames")
    sound = pygame.mixer.Sound("jumpscare.mp3")

   
    if hwnd:
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x02)
    show_jumpscare(screen, frames, sound)

    pygame.quit()


if __name__ == "__main__":
    main()
