equation = input("Enter equation: ")
botrange = -100
toprange =  100
stretch = 1
shiftx = 0
shifty = 0
if botrange == "":
    botrange = -10
else:
    botrange = int(botrange)
if toprange == "":
    toprange = 10
else:
    toprange = int(toprange)
inbetween = 500
equation = equation.replace("^","**").replace("2x","2*x").replace("3x","3*x").replace("4x","4*x").replace("5x","5*x").replace("6x","6*x").replace("7x","7*x").replace("8x","8*x").replace("9x","9*x").replace(")(",")*(")
def plugin(b):
    return float(eval(equation.replace("x","("+str(b)+")")))
plot = []
for i in range(botrange*200,toprange*200):
    if i == 0:
        try:
            plot.append((i / 200, -plugin(i / 200)))
        except:
            pass
    else:
        plot.append((i/100,-plugin(i/100)))
import pygame
pygame.init()
screen_width = 500
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_e]:
        stretch += 1
    if key[pygame.K_q]:
        stretch += -1
    if key[pygame.K_d]:
        shiftx += -1
    if key[pygame.K_a]:
        shiftx += 1
    if key[pygame.K_w]:
        shifty += 1
    if key[pygame.K_s]:
        shifty += -1
    screen.fill((0, 0, 0))
    xaxis = pygame.Rect(shiftx-2500, 150+shifty, 5000, 1)
    yaxis = pygame.Rect(250+shiftx,shifty-1500,1,3000)
    for i in range(-500,501):
        xticks = pygame.Rect(250+0+i*5*stretch+shiftx,147+shifty,1,6)
        pygame.draw.rect(screen, (50,50,50), xticks)
    for i in range(-300,301):
        yticks = pygame.Rect(247+shiftx,150+0+i*5*stretch+shifty,6,1)
        pygame.draw.rect(screen, (50,50,50), yticks)
    pygame.draw.rect(screen, (50,50,50), xaxis)
    pygame.draw.rect(screen, (50, 50, 50), yaxis)
    for i in plot:
        point = (stretch*i[0]+250+shiftx,stretch*i[1]+150+shifty,1,1)
        pygame.draw.rect(screen, (255,255,255), point)
    pygame.display.update()
    clock.tick(20)
pygame.quit()
