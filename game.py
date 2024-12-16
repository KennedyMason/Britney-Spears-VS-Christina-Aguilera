import pygame
import os


class Game:

    def __init__(self, britney_img, xtina_img, bg_img):
        
        #screen width and height
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        #central border
        self.BORDER = pygame.Rect((self.WIDTH//2)-5, 0, 10, self.HEIGHT)

        #britney and xtina icons (literally) and background image
        self.BRITNEY =  pygame.transform.scale(pygame.image.load(os.path.join('images', britney_img)), (60, 60))
        self.XTINA = pygame.transform.scale(pygame.image.load(os.path.join('images', xtina_img)), (60, 60)) 
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('images','leopard.jpg')), (self.WIDTH, self.HEIGHT))
        
        #britney and xtina speed
        self.VEL = 5

        #frames per second
        self.FPS = 60

        #bullets
        self.MAX_BULLETS = 10
        self.BULLET_VEL = 7

        #they get hit by bullets
        self.BRITNEY_HIT =pygame.USEREVENT + 2
        self.XTINA_HIT = pygame.USEREVENT + 1

        #colors
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255, 0, 0)

        #fonts
        self.HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
        self.WINNER_FONT = pygame.font.SysFont('comicsans', 100)

        #britney and xtina rectangles
        self.britney_rect = pygame.Rect(175, 250, 60, 60)
        self.xtina_rect = pygame.Rect(525, 250, 60, 60)

        #keeps track of bullets fired
        self.britneys_bullets = []
        self.xtinas_bullets = []
        
        #britney and xtina health
        self.britney_health = 10
        self.xtina_health = 10

    
    #draws window
    def draw_window(self):
        
        #background and border
        self.WIN.blit(self.BACKGROUND, (0,0))
        pygame.draw.rect(self.WIN, self.BLACK, self.BORDER)
        
        #health stats
        britney_health_text = self.HEALTH_FONT.render("Health: " + str(self.britney_health), 1, self.WHITE)
        xtina_health_text = self.HEALTH_FONT.render("Health: " + str(self.xtina_health), 1, self.WHITE)
        self.WIN.blit(britney_health_text, (10, 10))
        self.WIN.blit(xtina_health_text, (self.WIDTH - xtina_health_text.get_width() - 10, 10))


        #britney and christina
        self.WIN.blit(self.BRITNEY, (self.britney_rect.x, self.britney_rect.y))
        self.WIN.blit(self.XTINA, (self.xtina_rect.x, self.xtina_rect.y))


        #shoots bullets
        for bullets in self.britneys_bullets:
            pygame.draw.rect(self.WIN, self.RED, bullets)

        for bullets in self.xtinas_bullets:
            pygame.draw.rect(self.WIN, self.RED, bullets)


        pygame.display.update()

    
    #someone wins the game
    def draw_winner(self, text):
        draw_text = self.WINNER_FONT.render(text, 1, self.WHITE)
        self.WIN.blit(draw_text, (self.WIDTH//2) - draw_text.get_width()//2, (self.HEIGHT//2 - draw_text.get_height()//2))
        pygame.time.delay(5000)

    
    #move britney
    def britney_movement(self, keys_pressed):
        
        if keys_pressed[pygame.K_a] and self.britney_rect.x - self.VEL + self.britney_rect.width > 55: #leftF
            self.britney_rect.x -= self.VEL

        if keys_pressed[pygame.K_d] and self.britney_rect.x + self.VEL + self.britney_rect.width < self.BORDER.x + 5: #right
            self.britney_rect.x += self.VEL

        if keys_pressed[pygame.K_w] and self.britney_rect.y - self.VEL > -5: #up
            self.britney_rect.y -= self.VEL

        if keys_pressed[pygame.K_s] and self.britney_rect.y - self.VEL + self.britney_rect.height < self.HEIGHT - 5: #down
            self.britney_rect.y += self.VEL

    
    #move xtina
    def xtina_movement(self, keys_pressed):

        if keys_pressed[pygame.K_LEFT] and self.xtina_rect.x - self.VEL > self.BORDER.x + self.BORDER.width//2: #left
            self.xtina_rect.x -= self.VEL

        if keys_pressed[pygame.K_RIGHT] and self.xtina_rect.x + self.VEL + self.xtina_rect.width < self.WIDTH +5: #right
            self.xtina_rect.x += self.VEL

        if keys_pressed[pygame.K_UP] and self.xtina_rect.y - self.VEL > -5: #up
            self.xtina_rect.y -= self.VEL

        if keys_pressed[pygame.K_DOWN] and self.xtina_rect.y - self.VEL + self.xtina_rect.height < self.HEIGHT -5: #down
            self.xtina_rect.y += self.VEL


    #manages bullets
    def handle_bullets(self):
        for bullet in self.britneys_bullets:
            bullet.x += self.BULLET_VEL
            if self.xtina_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.XTINA_HIT))
                self.britneys_bullets.remove(bullet)
            elif bullet.x > self.WIDTH:
                self.britneys_bullets.remove(bullet)

        for bullet in self.xtinas_bullets:
            bullet.x -= self.BULLET_VEL
            if self.britney_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.BRITNEY_HIT))
                self.xtinas_bullets.remove(bullet)
            elif bullet.x < 0:
                self.xtinas_bullets.remove(bullet)
