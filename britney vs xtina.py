import pygame
import os

#set screen size and caption
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("britney spears and christina aguilera fight to the death")

FPS = 60 #frames per sec
VEL = 5 #velocity
BULLET_VEL = 7 #bullet velocity
MAX_BULLETS = 10

#they get hit by bullets
BRITNEY_HIT =pygame.USEREVENT + 1
XTINA_HIT = pygame.USEREVENT + 2

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 0, 0)

#border
BORDER = pygame.Rect((WIDTH//2)-5, 0, 10, HEIGHT)

#pictures
BRITNEY_OG_IMAGE = pygame.image.load(os.path.join('images', 'britney.png'))
BRITNEY = pygame.transform.scale(BRITNEY_OG_IMAGE, (55, 40)) #resized

XTINA_OG_IMAGE = pygame.image.load(os.path.join('images', 'xtina.png'))
XTINA = pygame.transform.scale(XTINA_OG_IMAGE, (55, 40)) #resized

    

#draws window
def draw_window(britney_rect, xtina_rect, britneys_bullets, xtinas_bullets):
    WIN.fill(WHITE)
    pygame.draw.recy(WIN, BLACK, BORDER)
    WIN.blit(BRITNEY_OG_IMAGE, (britney_rect.x, britney_rect.y))
    WIN.blit(XTINA_OG_IMAGE, (xtina_rect.x, xtina_rect.y))
    
    for bullets in britneys_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullets in xtinas_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()

#move britney
def britney_movement(keys_pressed, britney_rect):

    if keys_pressed[pygame.K_a] and britney_rect.x - VEL > 0: #left
        britney_rect.x -= VEL

    if key_pressed[pygame.K_d] and britney_rect.x + VEL + britney_rect.width < BORDER.x: #right
        britney_rect.x += VEL

    if key_pressed[pygame.K_w] and britney_rect.y - VEL > 0: #up
        britney_rect.y += VEL

    if key_pressed[pygame.K_d] and britney_rect.y + VEL + britney_rect.height < HEIGHT - 15: #down
        britney_rect.y -= VEL

#move xtina
def xtina_movement(keys_pressed, xtina_rect):

    if keys_pressed[pygame.K_LEFT] and xtina_rect.x - VEL > BORDER.x + BORDER.width: #left
        xtina_rect.x -= VEL

    if key_pressed[pygame.K_RIGHT] and xtina_rect.x + VEL + xtina_rect.width < WIDTH: #right
        xtina_rect.x += VEL

    if key_pressed[pygame.K_UP] and xtina_rect.x - VEL > 0: #up
        xtina_rect.y += VEL

    if key_pressed[pygame.K_DOWN] and xtina_rect.y + VEL + xtina_rect.height < HEIGHT - 15: #down
        xtina_rect.y -= VEL

#manages bullets
def handle_bullets(britneys_bullets, xtinas_bullets, britney_rect, xtina_rect):
    for bullet in britneys_bullets:
        bullet.x += BULLET_VEL
        if xtina_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(XTINA_HIT))
            britneys_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            britneys_bullets.remove(bullet)

    for bullet in xtinas_bullets:
        bullet.x -= BULLET_VEL
        if britney_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BRITNEY_HIT))
            xtinas_bullets.remove(bullet)
        elif bullet.x < WIDTH:
            xtinas_bullets.remove(bullet)

def main():

    britney_rect = pygame.Rect(175, 250, 55, 40)
    xtina_rect = pygame.Rect(525, 250, 55, 40)

    britneys_bullets = []
    xtinas_bullets = []

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS) #game runs at 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(britneys_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(britney_rect.x + britney_rect.width, britney_rect.y + britney_rect.height//2 - 2, 10, 5)
                    britneys_bullets.append(bullet) 

                if event.key == pygame.K_RCTRL and len(xtinas_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(xtina_rect.x, xtina_rect.y + xtina_rect.height//2 - 2, 10, 5)
                    xtinas_bullets.append(bullet) 
        
        #britney and christina move on screen
        key_pressed = pygame.key.get_pressed()
        britney_movement(key_pressed, britney_rect)
        xtina_movement(key_pressed, xtina_rect)

        #manages bullet collisions
        handles_bullets(britneys_bullets, xtinas_bullets, britney_rect, xtina_rect)

        #draw window
        draw_window(britney_rect, xtina_rect, britneys_bullets, xtinas_bullets)
        
    
    #loop ends, game quits
    pygame.quit()