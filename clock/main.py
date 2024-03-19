import pygame
import datetime

pygame.init()
pygame.display.set_caption("clock")

def rot_center(image, angle, x, y):
    rot_image = pygame.transform.rotate(image, angle)
    new_rect = rot_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rot_image, new_rect


H, W = 700, 700
screen = pygame.display.set_mode((H, W))
mickey = pygame.image.load("mickeyClock.jpg")
right = pygame.image.load("rightarm.png")
left = pygame.image.load("leftarm.png")


mickey = pygame.transform.scale(mickey, (H, W))
# right = pygame.transform.smoothscale(right, (right.get_width() // 2, right.get_height() // 2))
# left = pygame.transform.scale(left, (H / 2, W / 2))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    x = (-6*minute) % 360
    y = ((-1)*second * 6) % 360

    rot_right, x = rot_center(right, x, H / 2, W / 2)
    rot_left, y = rot_center(left, y, H / 2, W / 2)
    screen.blit(mickey, (0, 0))
    screen.blit(rot_right, x)
    screen.blit(rot_left, y)

    pygame.display.update()
clock.tick(60)
pygame.quit()