import pygame
import sys

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x, y = 375, 275  # стартовая позиция
size = 50        # размер квадратика
speed = 5        # скорость

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Математический трюк: True=1, False=0, поэтому вычитание даёт направление
    x += speed * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    y += speed * (keys[pygame.K_DOWN]  - keys[pygame.K_UP])

    # Не даём уйти за границы окна
    x = max(0, min(x, W - size))
    y = max(0, min(y, H - size))

    screen.fill((255, 255, 255))  # белый фон
    pygame.draw.rect(screen, (0, 0, 0), (x, y, size, size))  # чёрный квадрат
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
