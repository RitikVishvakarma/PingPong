import pygame
import sys
import os
pygame.init()

pygame.mixer.init()
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# Creating Whindow
x = 100
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
width = 1000
height = 600
gameWindow = pygame.display.set_mode((width, height))

# Game Title
pygame.display.set_caption("Pong Game")
pygame.display.update()
font = pygame.font.SysFont(None, 40)

# Game specific variables
exit_game = False
ball_x = int(width/2) - 7
ball_y = int(height/2) - 7
velocity_x = 5
velocity_y = 5
ball_size = 15
fps = 120
player_x = width-10
player_y = int(height/2)
player_size_x = 10
player_size_y = 140
opponent_x = 0
opponent_y = int(height/2) - 70
opponent_size_x = 10
opponent_size_y = 140
player_speed = 0
opponent_speed = 7

def ball_an():
    global ball_x, ball_y, velocity_x, velocity_y, height, width

    ball_x = ball_x + velocity_x
    ball_y = ball_y + velocity_y

    if ball_y <= 0 or ball_y >= height:
        pygame.mixer.music.load('Music/beep.mp3')
        pygame.mixer.music.play()
        velocity_y *= -1
        
    if ball_x <= 0 or ball_x >= width:
        sys.exit()
        

def player_an():
    global player_y, player_speed, height
    player_y += player_speed
    if player_y <= 0:
        player_y = 0
    if player_y >= height-140:
        player_y = height-140    

def opponent_an():
    global opponent_speed, opponent_x, opponent_y, height
    if opponent_y <= ball_y:
        opponent_y += opponent_speed
    if opponent_y > ball_y:
        opponent_y -=opponent_speed
    if opponent_y <= 0:
        opponent_y = 0
    if opponent_y >= height-140:
        opponent_y = height-140

clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_an()

    player_an()

    opponent_an()
    
    # Draw in Window
    gameWindow.fill(black)
    ball = pygame.draw.rect(gameWindow, white, [ball_x, ball_y, ball_size, ball_size])
    player = pygame.draw.rect(gameWindow, white, [player_x, player_y, player_size_x, player_size_y])
    opponent = pygame.draw.rect(gameWindow, white, [opponent_x, opponent_y, opponent_size_x, opponent_size_y])
    pygame.draw.aaline(gameWindow, white, (width/2, 0), (width/2, height))
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.music.load('Music/beep.mp3')
        pygame.mixer.music.play()
        velocity_x *= -1

    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()