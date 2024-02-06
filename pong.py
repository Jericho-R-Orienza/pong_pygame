import pygame

#Init colors
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

#Init game window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong")

#Starting cords and speed of player
player_x = 580
player_y = 580
player_speed_x = 0

#initial cords and speed of ball
ball_x = 10
ball_y = 10
ball_speed_x = 5
ball_speed_y = 5

#init score
score = 0

#create the player (paddle) and restrict its movement to between the edges of window
def drawPaddle(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,WHITE,[x,y,100,20]) #paddle is just a rectangle

# Game's main loop
game_lost = False
clock = pygame.time.Clock()
while not game_lost:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_lost = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -7
            elif event.key == pygame.K_RIGHT:
                player_speed_x = 7
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_speed_x = 0
                
    # Update player position
    player_x += player_speed_x
    # Ensure player stays within screen bounds
    player_x = max(0, min(player_x, 700))

    # Update ball position and handle collisions
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Wall collision for ball
    if ball_x <= 0 or ball_x >= 785:
        ball_speed_x *= -1
    elif ball_y <= 0:
        ball_speed_y *= -1

    # Paddle collision
    if player_x < ball_x < player_x + 100 and ball_y == 565:
        ball_speed_y *= -1
        score += 1

    # Bottom boundary collision
    if ball_y > 600:
        ball_speed_y *= -1
        print(f"GAME OVER! You scored: {score}")
        quit()

    # Drawing
    screen.fill(BLACK)
    drawPaddle(screen, player_x, player_y)
    pygame.draw.rect(screen, WHITE, [ball_x, ball_y, 15, 15])

    # Scoreboard
    font = pygame.font.SysFont('Times New Roman', 20, True, False)
    text = font.render(f"SCORE = {score}", True, WHITE)
    screen.blit(text, [650, 50])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()    