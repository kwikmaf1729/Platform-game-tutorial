import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()  
        #change name of window
        pygame.display.set_caption("ninja game")
        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        #this adds the image but we still have to load it on the screen
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')

        #the tuple is (x,y) where top left screen is (0,0)
        self.img_pos = [160,260]

        self.movement = [False, False]

    def run(self):
        while True:

            #update the screen each time with just a sky colour
            #where the argument is (r,g,b)
            self.screen.fill((14,219,248)) 

            #move the image based on movement
            self.img_pos[1] += self.movement[1] - self.movement[0]
 
            #display cloud we added.
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                #if we press x, the window will close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #movement up or down
                    
                #if the key goes down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    

                #if the key is lifted up again (user stops pressing)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
        

            pygame.display.update()
            #to run at 60fps
            self.clock.tick(60)

Game().run()






