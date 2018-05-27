import drawBot
from random import randint

def draw():
    for i in range(0, 100):
        drawBot.newDrawing()
        drawBot.newPage(1000, 1000)
        drawBot.radialGradient(
            (randint(1,500), randint(1,500)),                         # startPoint
            (randint(1,800), randint(1,800)),                         # endPoint
            [(randint(0,1), randint(0,1), randint(0,1)), (randint(0,1), randint(0,1), randint(0,1)), (randint(0,1), randint(0,1), randint(0,1))],  # colors
            [randint(0,1), randint(0,1), randint(0,1)],                         # locations
            randint(0,1),                                  # startRadius
            randint(0,800)                                # endRadius
        )
# draw a rectangle
        drawBot.rect(randint(0,100), randint(0,100), randint(0,1000), randint(0,1000))

# draw the path
        drawBot.drawPath()
        drawBot.blendMode("multiply")
# set a color
        drawBot.rect(randint(1,10), randint(1,10), randint(1,100), randint(1,100))

# draw oval x, y, width, height
        drawBot.oval(randint(1,500), randint(1,500), randint(1,500), randint(1,500))
        drawBot.oval(randint(1,500), randint(1,500), randint(1,500), randint(1,500))
        drawBot.cmykFill(randint(0,1), randint(0,1), randint(0,1), randint(0,1))
# draw a rectangle
        drawBot.rect(randint(1,10), randint(1,10), randint(1,1000), randint(1,1000))
# set an other color
        drawBot.cmykFill(randint(0,1), randint(0,1), randint(0,1), randint(0,1))
# overlap a second rectangle
        drawBot.rect(randint(1,500), randint(1,500), randint(1,600), randint(1,600))
        drawBot.saveImage(str(i) + '.png' )
        drawBot.endDrawing()
        print(str(i) + ' done.')

if __name__ == '__main__':
    draw()
