# start modules
import random
from turtle import Screen
import pgzrun
import sys
from pgzero.actor import Actor
# create constants
WIDTH = 800
HEIGHT = 600
SCORE = 0
GAP = 210
gameOver = False
# print welcome
print ("The game is about to start!")
print ('"Click the mouse to "flap" upwards "' )
print ("Dodge the pipes and the floor")
print ("Good luck and have fun!")
# make background
background = Actor("bg")
background.x = 400
background.y = 300
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300
# make pipes
list = []
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = 0
list.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800
list.append(bottomPipe1)
topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200
list.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = 560
list.append(bottomPipe2)
topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120
list.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710
list.append(bottomPipe3)
# draw everything to screen

def draw():
    global SCORE
    if gameOver == True:
        screen.fill((0, 0, 0))
        screen.draw.text(
            "GAME OVER!",
            center=(400, 220),
            color=(255, 0, 0),
            fontsize=60)
        screen.draw.text(
            f"My score was: {SCORE}",
            center=(400, 300),
            color=(255, 255, 255),
            fontsize=30)
        screen.draw.text(
            "Thank you for playing!",
            center=(400, 370),
            color=(255, 255, 255),
            fontsize=20)
    else:
        # draw background
            background.draw()
            # draw characters
            bird.draw()
            for pipe in list:
                pipe.draw()
           
# update everything
def update():
    global SCORE
    global gameOver
    if gameOver == False:
        # update bird
        bird.y = bird.y + 1.5
        # update pipes
        for pipe in list:
            pipe.x = pipe.x - 1
        newPipeY = random.randint(155, 445)
        for index in range(len(list)):
            if list[index].x < -list[index].width:
                list[index].x = WIDTH
                if list[index].image == "top":
                    list[index].y = newPipeY - (300 + GAP / 2)
                else:
                    list[index].y = newPipeY + 300 + GAP / 2
                    SCORE += 1
# bird hits bottom of screen
        if bird.y > HEIGHT:
                print("GAME OVER!")
                print(f"Final score: {SCORE}")
                gameOver = True
            # bird hits pipes
        for i in range(0, len(list), 2):
            if bird.colliderect(list[i]):
                print()
        for i in range(0, len(list), 1):
            if bird.colliderect(list[i]):
                print("GAME OVER!")
                print(f"Final score: {SCORE}")
                gameOver = True
# moving
def on_mouse_down():
    bird.y = bird.y - 40
# runs everything
pgzrun.go()