import pygame

pygame.init()

screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

while running:
    
    
    for event in pygame.event.get(): # check if the game is being quit
        if event.type == pygame.QUIT:
              running = False




    screen.fill((0,0,0))
      
    for event in pygame.event.get():
        print(event.type)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print (pos)




    pygame.display.flip()
