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

    def run(self):
        while True:

            #display cloud we added
            self.screen.blit(self.img, (100,200))

            for event in pygame.event.get():
                #if we press x, the window will close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            #to run at 60fps
            self.clock.tick(60)

Game().run()






