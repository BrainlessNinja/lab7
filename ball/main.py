import pygame

# Initialize pygame
pygame.init()

# Set the dimensions of the window
size = (800, 600)
screen = pygame.display.set_mode(size)

# Create a red ball
ball_radius = 25
ball_pos = [size[0] // 2, size[1] // 2]  # Start at center of screen
ball_color = pygame.Color('red')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_pos[1] - ball_radius - 20 >= 0:
                ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN and ball_pos[1] + ball_radius + 20 <= size[1]:
                ball_pos[1] += 20
            elif event.key == pygame.K_LEFT and ball_pos[0] - ball_radius - 20 >= 0:
                ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT and ball_pos[0] + ball_radius + 20 <= size[0]:
                ball_pos[0] += 20

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()