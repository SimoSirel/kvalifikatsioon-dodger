__author__ = 'simo.sirel'

#data for game from player
obstacle_count=0
while obstacle_count<5 or obstacle_count>100:
    obstacle_count=int(input("how many obstacles you want?"))


import pygame,classes,time

#define initial variables and start game
pygame.init()
running=True
size=width,height=800,600
screen = pygame.display.set_mode(size)

#define used font
myfont = pygame.font.SysFont("monospace", 15)
end=myfont.render("Press SPACE to start again or ESC to quit.", 10, [0,0,0])

#define variables that are needed to redefine when the game restarts
lives = 3
debris = pygame.sprite.Group()
start = time.time()
lost = False
for _ in range(int(obstacle_count)):
    asteroid=classes.obstacle()
    debris.add(asteroid)

#create player class
ship=classes.Ship(5)
ships=pygame.sprite.Group(ship)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and lost == False: ship.moveleft()
            if event.key == pygame.K_RIGHT and lost == False: ship.moveright()
            if event.key == pygame.K_ESCAPE and lost == True: running = False
            if event.key == pygame.K_SPACE and lost == True:
                #if player chooses to restart game then there variables are needed to redefine
                ship.reinit()
                lives=3
                debris=pygame.sprite.Group()
                for _ in range(15):
                    asteroid=classes.obstacle()
                    debris.add(asteroid)
                start = time.time()
                lost = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                ship.stop()

    if pygame.sprite.spritecollide(ship, debris, True):
        lives-=1


    screen.fill([255,255,255])

    if lives <=0:
        if lost == False:
            stop = time.time()
            score = myfont.render("you survived for "+str(round(stop-start,3))+" seconds", 10, [0,0,0])
        lost = True
        screen.blit(end,(200,200))
        screen.blit(score,(200,250))

    #evrything is drawn to screen
    ships.draw(screen)
    debris.draw(screen)
    ships.update()
    debris.update()
    pygame.time.Clock().tick(60)
    pygame.display.flip()
pygame.quit()