import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon) 
background =pygame.image.load('space_background.jpg')
background= pygame.transform.scale(background,(800,600))
mixer.music.load('background.wav')
mixer.music.play(-1)

playerImg = pygame.image.load('spaceship1.png')
playerImg = pygame.transform.scale(playerImg,(40,40))
playerX=370
playerY=480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY =[]
enemyX_change =[]
enemyY_change =[]
num_of_enemies = 5 

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyImg.append(pygame.transform.scale(enemyImg[i],(50,50)))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(25,90))
    enemyX_change.append(0.25)
    enemyY_change.append(35)


bulletImg = pygame.image.load('laser.png')
bulletImg = pygame.transform.scale(bulletImg,(40,40))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .55
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',20)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',40)

def show_score(x,y):
    score = font.render(f"Score : {score_value}",True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text,(275,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))
    if distance < 20:
        return True
    return False

running = True
start = 0
timer = "stop"
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

         
    playerX += playerX_change

    for i in range(num_of_enemies):

        if enemyY[i] > 420:
            for j in range(num_of_enemies):
                enemyY[j] =2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX[i] = 0
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 760:
            enemyX[i] = 760
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(25,90)

        enemy(enemyX[i],enemyY[i],i)

    if playerX <=0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760
    
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    if bulletY <0:
        bulletY = 480
        bullet_state = "ready"
        

    player(playerX,playerY) 
    show_score(textX, textY)
    pygame.display.update()