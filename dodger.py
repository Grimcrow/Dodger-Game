import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

#SETTING FRAMES PER SEC//Speed of the game
FPS = 20

#THE DIMENTIONS OF THE GAME WINDOW
WHEIGHT = 300
WWIDTH = 500
windowSurface = pygame.display.set_mode((WWIDTH, WHEIGHT), 0, 32)

pygame.display.set_caption('DODGER')

#SET UP COLOR
#         R  G  B
BLACK = ( 0, 0, 0)

#PLAYER OBJECT
player = pygame.Rect(0,260,20,20)
playerImage = pygame.image.load('player.png')
playerStrechedImage = pygame.transform.scale(playerImage,(20,20))

#ENEMY OBJECT
enemyImage = pygame.image.load('baddie.png')
enemyImage = pygame.transform.scale(enemyImage,(10, 10))

#CHERRY OBJECT
cherryImage = pygame.image.load('cherry.png')
cherryImage = pygame.transform.scale(cherryImage,(10, 10))

dcherry = {1 : pygame.Rect(random.randint(0, WWIDTH - 5), 0, 5, 5 )}

enemy = []
for i in range(1):
    enemy.append(pygame.Rect(random.randint(0, WWIDTH - 5) + 3, 0, 5, 5))

enemypos = {}
i = 1

for a in enemy:
    d = {i : a}
    enemypos.update(d)
    i += 1

i = 1
touched = 0

#SET UP KEYBOARD VARS
moveLeft = False
moveRight = False

MOVESPEED = 6

#SET UP MUSIC
pickup = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play( -1, 0.0)
musicPlaying = True

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #CAPTURE KEY PRESSES
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.start( -1, 0.0)

    #SET BACKGROUND COLOR
    windowSurface.fill(BLACK)

    #MOVE THE PLAYER
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED

    if moveRight and player.right < WWIDTH:
        player.right += MOVESPEED

    #DRAW BLOCK ONTO IMAGE
    windowSurface.blit( playerStrechedImage, player)

    enemyadd = []
    for i in range(1):
        enemyadd.append(pygame.Rect(random.randint(0, WWIDTH - 5), 0, 5, 5))

    if i < len(enemyadd):
        dt = {len(enemypos)+1: enemyadd[i]}
        if random.randint(0, 11) % 5 == 0:
            FPS += 0.09
            enemypos.update(dt)

        i += 1
    else:
        i = 1

    #CHECK IF PLAYER COLLIDED
    for en in enemypos:
        if player.colliderect(enemypos[en]):
            touched += 0.5

            if musicPlaying:
                pickup.play()

            if touched == 10:
                pygame.quit()
                sys.exit()

    if dcherry:
        if player.colliderect(dcherry[1]):
            if touched :
                touched -= 1


    for en in enemypos:

        if enemypos[en].top < WHEIGHT + 10:
            windowSurface.blit(enemyImage, enemypos[en])
            enemypos[en] = pygame.Rect(enemypos[en].left, enemypos[en].top + 2, 5, 5)

    if dcherry[1].top < WHEIGHT + 10:
        windowSurface.blit(cherryImage, dcherry[1])
        dcherry[1] = pygame.Rect(dcherry[1].left, dcherry[1].top + 3, 5, 5)

    else:
        dcherry[1] = pygame.Rect(random.randint(0, WWIDTH - 5), 0, 5, 5)




    pygame.display.update()
    print touched
    mainClock.tick(FPS)




