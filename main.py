import pygame
import os
from game import Game


pygame.font.init()
pygame.display.set_caption("britney spears and christina aguilera fight to the death")

game = Game("britney.jpg", "xtina.jpg", "leopard.jpg")

def main():

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(game.FPS) #game runs at 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(game.britneys_bullets) < game.MAX_BULLETS:
                    bullet = pygame.Rect(game.britney_rect.x + game.britney_rect.width, game.britney_rect.y + game.britney_rect.height//2 - 2, 10, 5)
                    game.britneys_bullets.append(bullet) 

                if event.key == pygame.K_RCTRL and len(game.xtinas_bullets) < game.MAX_BULLETS:
                    bullet = pygame.Rect(game.xtina_rect.x + game.xtina_rect.width,  game.xtina_rect.y + game.xtina_rect.height//2 - 2, 10, 5)
                    game.xtinas_bullets.append(bullet) 
        
            #health decreases if hit
            if event.type == game.BRITNEY_HIT:
                game.britney_health -= 1

            if event.type == game.XTINA_HIT:
                game.xtina_health -= 1
        
            #determining if someone has won
            winner_text = ""

            if game.britney_health <= 0:
                winner_text = "CHRISTINA WINS"

            if game.xtina_health <= 0:
                winner_text = "BRITNEY WINS"

            if winner_text != "":
                game.draw_winner(winner_text)
                run = False

        #britney and christina move on screen
        key_pressed = pygame.key.get_pressed()
        game.britney_movement(key_pressed)
        game.xtina_movement(key_pressed)

        #manages bullet collisions
        game.handle_bullets()

        #draw window
        game.draw_window()
        
    if key_pressed[pygame.K_SPACE]:
        main()


main()