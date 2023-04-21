import pygame
import random
def draw(a,b,c):
    pygame.draw.rect(a,b,c)
pygame.init()
screen_width = 1920
screen_height = 1080
direction="south"
coords=[(900,0),(900,50)]
snake = pygame.Rect(900,100, 50, 50)
food = pygame.Rect(random.randint(0,1920) // 50 * 50, random.randint(0,1080) // 50 * 50, 50, 50)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
ticks=10
ticksupdate=ticks
length=0
lengthlist=[]
color=(255,255,255)
seconds=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and not direction == "east":
        direction="west"
    if key[pygame.K_d] and not direction == "west":
        direction="east"
    if key[pygame.K_w] and not direction == "south":
        direction="north"
    if key[pygame.K_s] and not direction =="north":
        direction="south"
    if key[pygame.K_e]:
        length+=1
    if ticks==0:
        add=snake.x,snake.y
        coords.append(add)
        if direction == "north":
            snake.y+=-50
        if direction == "south":
            snake.y+=50
        if direction == "east":
            snake.x+=50
        if direction == "west":
            snake.x+=-50
        ticks=10
    else:
        ticks+=-1
    if snake.x == food.x and snake.y == food.y:
        food = pygame.Rect(random.randint(0, 1920) // 50 * 50, random.randint(0, 1080) // 50 * 50, 50, 50)
        length+=1
        lengthlist.append(length)
    pygame.display.update()
    screen.fill((0, 0, 0))
    for i in lengthlist:
        tail = pygame.Rect(coords[len(coords) - i][0], coords[len(coords) - i][1], 50, 50)
        draw(screen, color, tail)
        if snake.x == tail.x and snake.y == tail.y:
            pygame.quit()
    draw(screen, (255,0,0), food)
    draw(screen, color, snake)
    clock.tick(60)
    if snake.x > 1920 or snake.x < 0 or snake.y > 1080 or snake.y < 0:
        pygame.quit()
pygame.quit()
