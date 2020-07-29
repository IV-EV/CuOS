import pygame

#Initialise pygame
pygame.init()

#Define colours
GREEN = (51, 204, 51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set window properties and open it
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CuOS")


#Boolean variable used to exit loop below
on = True

#Variable used to control refresh rate
refresh = pygame.time.Clock()

#Main loop, used to capture user input events, implement game logic,
#and refresh the screen
while on:

    #main event loop
    for event in pygame.event.get(): #when user performs action
        #if that action is to quit
        if event.type == pygame.QUIT:
            #set on to False to exit main loop
            on = False

    #game logic will go here


    #drawing code should go here

    #start by clearing screen to white
    screen.fill(WHITE)
    #draw shapes here






    #set refresh rate and refresh screen
    refresh.tick(60)
    pygame.display.flip()



#stop game engine once we're out of the main loop
pygame.quit()
