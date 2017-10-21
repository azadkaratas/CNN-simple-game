import pygame
import time
import random

pygame.init()

display_width = 400
display_height = 600

black = (33,33,33)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

car_width = 50
car_height = 50
car_speed = 10

def youScored(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    
def car(x,y):
    things(x,y,car_width,car_height,red)

def crash():
    message_display('You Crashed!')
    
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()    
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    pygame.display.update()    
    game_loop()
    
def game_loop():    
    x= (display_width * 0.45)
    y= (display_height * 0.8)
    
    thing_speed = 7
    thing_width = 150
    thing_height = 60
    thing_starty = -thing_height
    thing_startx = random.randrange(0,display_width-thing_width)

    x_change = 0
    score = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            # MOVEMENT OF CAR 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if x<=0:
                        x_change = 0
                    else:
                        x_change = -car_speed
                elif event.key == pygame.K_d: 
                    if x>= display_width - car_width:
                        x_change = 0
                    else:
                        x_change = car_speed
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
        
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty += thing_speed
        
        car(x,y)
        youScored(score)

        if x> display_width - car_width:
            x = display_width - car_width
        elif x<0:
            x = 0 
                        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,(display_width-thing_width))
            score += 1
            
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width<thing_startx+thing_width:
                crash()
            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
