import pygame

#Init colors
BLACK = (0,0,0)
WHITE = (255,255,255)


pygame.init()

#Init game window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong")

#Starting coords of player
player_x, player_y = 580

#initial player speed
player_seed_x, player_speed_y = 0

#initial cords and speed of ball
ball_x, ball_y = 10
ball_speed_x, ball_speed_y = 5

#init score
score = 0

#create the player (paddle) and restrict its movement to between the edges of window
def drawPaddle(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,WHITE,[x,y,100,20]) #paddle is just a rectangle
    
pygame.quit()    