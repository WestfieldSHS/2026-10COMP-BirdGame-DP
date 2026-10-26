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
List = []
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = 0
List.append(topPipe1)
bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800
List.append(bottomPipe1)
topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200
List.append(topPipe2)
bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = 560
List.append(bottomPipe2)
topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120
List.append(topPipe3)
bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710
List.append(bottomPipe3)
# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    for pipe in List:
        pipe.draw()
# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    for pipe in List:
        pipe.x = pipe.x - 1
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