import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 700
HEIGHT = 500

SCREEN_BOUNDARIES = pygame.Rect(0, 0, WIDTH, HEIGHT)

RECT_OFFSET_X = 50
RECT_OFFSET_Y = 20
RECT_WIDTH = 5
RECT_HEIGHT = 50

BALL_SIZE = 16

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.speed = 1
        self.direction = random.uniform(0, 1) * 2 * math.pi

    def change_direction(self, direction):
        self.direction = direction

    def move_ip(self):
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed
  
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pong")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
left_y_speed = 0

# Speed in pixels per frame
right_y_speed = 0

left_rect = pygame.Rect(RECT_OFFSET_X, RECT_OFFSET_Y, RECT_WIDTH, RECT_HEIGHT)
right_rect = pygame.Rect(WIDTH - RECT_OFFSET_X, RECT_OFFSET_Y, RECT_WIDTH, RECT_HEIGHT)
ball = Ball()

pygame.display.flip()

while not done:
    for event in pygame.event.get():

        print(ball.x, ball.y)


        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_UP:
                left_y_speed = -3
            elif event.key == pygame.K_DOWN:
                left_y_speed = 3

            elif event.key == pygame.K_w:
                right_y_speed = -3
            elif event.key == pygame.K_s:
                right_y_speed = 3

            
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                left_y_speed = 0

            elif event.key == pygame.K_w or event.key == pygame.K_s:
                right_y_speed = 0

        
    left_rect.move_ip(0, left_y_speed)
    right_rect.move_ip(0, right_y_speed)
    ball.move_ip()

    left_rect.clamp_ip(SCREEN_BOUNDARIES)
    right_rect.clamp_ip(SCREEN_BOUNDARIES)


    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, left_rect, 0)
    pygame.draw.rect(screen, WHITE, right_rect, 0)
    pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

    pygame.display.flip()

# Close everything down
pygame.quit()