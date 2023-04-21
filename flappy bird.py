import pygame
import random
pygame.init()
screen_width = 1920
screen_height = 1080
positionx1=1920
positionx2=2880
positiony1=random.randint(200, 1080)
positiony2=random.randint(200,1080)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
player = pygame.Rect(500, 100, 50, 50)
barrier1 = pygame.Rect(positionx1, positiony1, 75, 10000)
barrier2 = pygame.Rect(positionx1, positiony1 - 10300, 75, 10000)
barrier3 = pygame.Rect(positionx2, positiony2, 75, 10000)
barrier4 = pygame.Rect(positionx2, positiony2 - 10300, 75, 10000)
velocity = 1.2
move = 0
ticks = 10
speed=-10
running = True
justjumped=False
score=0
oldscore=score
scored1 = False
scored2 = False
while running:
    if player.y < 1080:
        move += velocity
    player.y = player.y + move
    if player.y > 1080:
        running = False
    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not justjumped:
        move = -15
        justjumped = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if ticks == 0:
        justjumped = False
        ticks = 10
    else:
        ticks += -1
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), barrier1)
    pygame.draw.rect(screen, (255, 255, 255), barrier2)
    pygame.draw.rect(screen, (255, 255, 255), barrier3)
    pygame.draw.rect(screen, (255, 255, 255), barrier4)
    pygame.display.update()
    positionx1 += speed
    positionx2 += speed
    if player.x > positionx1 and player.x < positionx1 + 100:
        if player.y > positiony1 or player.y < positiony1 - 300:
            running = False
    if player.x > positionx2 and player.x < positionx2 + 100:
        if player.y > positiony2 or player.y < positiony2 - 300:
            running = False
    if positionx1 < 480 and not scored1:
        score += 1
        scored1 = True
    if positionx2 < 480 and not scored2:
        score += 1
        scored2 = True
    if positionx1 < -100:
        positionx1 = 1920
        positiony1 = random.randint(200, 1080)
        scored1 = False
    if positionx2 < -100:
        positionx2 = 1920
        positiony2 = random.randint(200, 1080)
        scored2 = False
    if score == oldscore + 5:
        oldscore = score
        speed += -2
    barrier1 = pygame.Rect(positionx1, positiony1, 75, 10000)
    barrier2 = pygame.Rect(positionx1, positiony1 - 10300, 75, 10000)
    barrier3 = pygame.Rect(positionx2, positiony2, 75, 10000)
    barrier4 = pygame.Rect(positionx2, positiony2 - 10300, 75, 10000)
    clock.tick(60)
pygame.quit()
print(score)
