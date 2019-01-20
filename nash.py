import pygame
import pygame.font
from pygame.locals import *
  
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Constants
IDLE = -1
WIDTH = 700
HEIGHT = 500
 
 
class Player():
    def __init__(self):
        self.timer = 0
 
    def spin(self,screen):
        if self.timer < 20:
            screen.blit(self.char_front,[250, 250])
        elif self.timer >= 20 and self.timer < 40:
            screen.blit(self.char_right,[250, 250])
        elif self.timer >= 40 and self.timer < 60:
            screen.blit(self.char_back,[250, 250])
        elif self.timer >= 60 and self.timer < 80:
            screen.blit(self.char_left,[250, 250])
        else:
            self.timer = 0
            screen.blit(self.char_front,[250, 250])
        self.timer += 1
        return
    # end spin()
# end Player()
 
class Nash(Player):
    def __init__(self):
        super().__init__()
        self.name = "Nash"
         
        self.char_front = pygame.image.load("nash.jpg").convert()
        self.char_front.set_colorkey(WHITE)
        self.char_front = pygame.transform.scale(self.char_front, [50,50])
     
        self.char_left = pygame.image.load("nash.jpg").convert()
        self.char_left.set_colorkey(BLACK)
        self.char_left = pygame.transform.scale(self.char_left,[50,50])
 
        self.char_right = pygame.transform.flip(self.char_left,True,False)
 
        self.char_back = pygame.image.load("nash.jpg").convert()
        self.char_back.set_colorkey(BLACK)
        self.char_back = pygame.transform.scale(self.char_back,[50, 50])
 
        self.pos = [250, 250]
        self.prev = 0
         
        # -1 is a key to remember prev (for idle)
        # 0 for down
        # 1 for right
        # 2 for up
        # 3 for left
        self.direction = 0;
    #end ctor()
 
    def update_pos(self,screen):
        if self.direction == 0:
            if self.pos[1] + 1 < HEIGHT - 50:
                self.pos[1] += 1
                self.prev = 0
            screen.blit(self.char_front, self.pos)       
        elif self.direction == 1:
            if self.pos[0] + 1 < WIDTH - 50:
                self.pos[0] += 1
                self.prev = 1
            screen.blit(self.char_right, self.pos)
        elif self.direction == 2:
            if self.pos[1] - 1 > 0:
                self.pos[1] -= 1
                self.prev = 2
            screen.blit(self.char_back, self.pos)
        elif self.direction == 3:
            if self.pos[0] - 1 > 0:
                self.pos[0] -= 1
                self.prev = 3
            screen.blit(self.char_left, self.pos)
        else:
            #if self.direction == IDLE:
            if self.prev == 0:
                screen.blit(self.char_front, self.pos)
            elif self.prev == 1:
                screen.blit(self.char_right, self.pos)
            elif self.prev == 2:
                screen.blit(self.char_back, self.pos)
            else:
                if self.prev == 3:
                    screen.blit(self.char_left,self.pos)
                 
    # end update_pos()
#end Albert()
         
     
def main():
    pygame.init()
 
    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
      
    pygame.display.set_caption("NASH")
      
    # Loop until the user clicks the close button.
    done = False
      
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Intro_Trigger is true until the player hits play
    intro_trigger = True
    choose_character = False
    flickr_count = 0
 
    pygame.font.init()
    #fonts
    basicfont = pygame.font.SysFont(None, 48)
    #Titlefont =  pygame.font.SysFont('Calibri',50,True,False)
    #Authorfont = pygame.font.SysFont('Calibri',30,False,True)
    #Namefont = pygame.font.SysFont('Calibri', 20, False,False)
    #Startfont = pygame.font.SysFont('Arial', 30, True, False)
     
     
    background_img = pygame.image.load("dark.jpg").convert()
    nash = Nash()
      
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break;
            if event.type == pygame.KEYDOWN:
                if choose_character == True and event.key == pygame.K_RETURN:
                    choose_character = False;
                if intro_trigger == True and event.key == pygame.K_RETURN:
                    intro_trigger = False
                    choose_character = True
                if event.key == pygame.K_DOWN:
                    nash.direction = 0
                elif event.key == pygame.K_RIGHT:
                    nash.direction = 1
                elif event.key == pygame.K_UP:
                    nash.direction = 2
                elif event.key == pygame.K_LEFT:
                    nash.direction = 3                   
            if event.type == pygame.KEYUP:
                nash.direction = IDLE
             
                 
             
 
        # --- Game logic should go here
         
      
        # --- Screen-clearing code goes here
      
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
      
        # If you want a background image, replace this clear with blit'ing the
        # background image.
         
      
        # Intro Page
        if intro_trigger:
            screen.blit(background_img, [0,0])
 
            if flickr_count < 20:
                #start = Startfont.render("Hit Start to Play",True, WHITE) 
                #screen.blit(start,[75,400])
                flickr_count += 1
            else:
                flickr_count +=1
                if flickr_count > 30:
                    flickr_count = 0
            #title = Titlefont.render("Insert Name Here",True, BLACK)
            #screen.blit(title, [60, 100])
             
            #authors = Authorfont.render("Created by Chris Quinones and Albert Lo", True, BLACK)
            #illustrator = Authorfont.render("sutff", True,BLACK)
            #screen.blit(authors, [60,150])
            #screen.blit(illustrator, [60,175])
 
        # Choose character screen
        elif choose_character:
            screen.fill(RED)
 
            #name = Namefont.render(nash.name,True,BLACK)
            nash.spin(screen)
            #screen.blit(name,[285, 345])
             
 
        # Regular gameplay
        else:
            screen.fill(WHITE)
            nash.update_pos(screen)
             
      
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
      
        # --- Limit to 60 frames per second
        clock.tick(60)
      
    # Close the window and quit.
    pygame.quit()
# end main()
 
if __name__ == "__main__":
    main()