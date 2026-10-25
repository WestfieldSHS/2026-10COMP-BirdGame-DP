# start modules
import random
import pgzrun
import sys
from pgzero.actor import Actor
# create constants
WIDTH = 800
HEIGHT = 600
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

topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = 0
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800
topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200
bottonPipe2 = Actor("bottom")
bottonPipe2.x = 532
bottonPipe2.y = 560
topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710
# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    for pipe in pipes:
        draw(pipe)
# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    for x in pipes:
        x = x - 1
    # bird hits bottom of screen
    if bird.y > HEIGHT:
        print("GAME OVER!")
        sys.exit()
    # bird hits pipes

# moving
def on_mouse_down():
    bird.y = bird.y - 50
# runs everything
pgzrun.go()