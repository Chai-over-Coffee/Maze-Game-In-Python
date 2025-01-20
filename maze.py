import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
START_POS = (50, 50)
END_POS = (750, 550)
LIVES = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

player_pos = list(START_POS)
player_size = 20

walls = [
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 200, 20, 400),
    pygame.Rect(200, 300, 600, 20),
    pygame.Rect(300, 400, 20, 200)
]

clock = pygame.time.Clock()
lives = LIVES
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

  
    for wall in walls:
        if player_rect.colliderect(wall):
            lives -= 1
            player_pos = list(START_POS)
            if lives == 0:
                game_over = True
    
    if player_rect.colliderect(pygame.Rect(END_POS[0], END_POS[1], player_size, player_size)):
        print("You win!")
        pygame.quit()
        sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player_rect)
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)
    pygame.draw.rect(screen, (0, 255, 0), (END_POS[0], END_POS[1], player_size, player_size))
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(text, (10, 10))

    if game_over:
        text = font.render("Game Over", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(30)