# https://www.youtube.com/watch?v=FfWpgLFMI7w&t=1007s

import pygame
import pygame_gui
import random

def main():
    
    # Necessary to start the game
    pygame.init()

    # Create a display for the game 
    screen = pygame.display.set_mode((800, 600))

    # GUI's manager
    manager = pygame_gui.UIManager((800, 600))
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text="Say Hello", manager=manager)
    
    # Create an icon for the game 
    icon = pygame.image.load("ship.png")
    pygame.display.set_icon(icon)

    # Images
    playerImg = pygame.image.load('ship.png')
    playerImg = pygame.transform.scale(playerImg, (200, 100)) 
    playerX, playerY = 320, 500

    missileImg = pygame.image.load('missile.png')
    missileImg = pygame.transform.scale(missileImg, (10, 25))
    missileY, missileX = playerY, playerX
    moveMissile = False

    invaderImg = pygame.image.load("invader.png")
    invaderImg = pygame.transform.scale(invaderImg, (100, 100))
    invaderX, invaderY = 0, 0
    invading = False

    # Font
    score_value = 0
    pygame.font.Font("freesansbold.ttf", 32)
    textX = 50
    textY = 50
    

    # Ship
    def player(x, y):
        screen.blit(playerImg, (x, y))

    # Missiles
    def missiles(x, y):
        if moveMissile:
            screen.blit(missileImg, (x, y))  

    # Invaders
    def invaders(x, y):
        screen.blit(invaderImg, (x, y))

    # Show score
    #def show_score(x, y):
     #   score = font.render()
            
                      


    clock = pygame.time.Clock()
    running = True
    while running:
        
        # FPS rate
        time_delta = clock.tick(60)
        screen.fill((100, 0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and playerX >= 0:
                    playerX -= 30
                elif event.key == pygame.K_RIGHT and playerX <= screen.get_width() - 170:
                    playerX += 30
                elif event.key == pygame.K_SPACE:
                    moveMissile = True
            
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print("Hello World!")
            manager.process_events(event)
                    
        manager.update(time_delta)
                    
        manager.draw_ui(screen)
                
                    

        player(playerX, playerY)
        
        missiles(playerX + 90, missileY)
        missileX = playerX
        if moveMissile:
            if missileY < 0:
                moveMissile = False
                missileY = playerY
            elif moveMissile:
                missileY -= 70 # Missile speed

        if invading == False:
            invaderX = int(random.randrange(0, screen.get_width() - 50))
            invaderY = 10
            invading = True
        elif invading:
            invaders(invaderX, invaderY)
            diffX = missileX - invaderX
            if -100 < diffX and diffX < 10 and missileY < invaderY :
                print("Entro") 
                invading = False
                
            elif invaderY > playerY: ##
                invading = False
            invaderY += 2 # Invader speed
            
        
            
        
        

        pygame.display.update()
main()