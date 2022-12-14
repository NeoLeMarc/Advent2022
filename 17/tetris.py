#!/usr/bin/env python3
import pygame, random, sys


colors =  [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

height = 2000 
width = 7
injectionPoint = 1
above = 3
numberOfFigures = 0
# Basic idea: 
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318

## New figure is inserted two columns from the left wall and bottom is three units above the highest rock
lastYPos = height - 5 

class Figure:
    x = 0
    y = 0
    nextFigure = 0

    figures = [
               [[12, 13, 14, 15],  -3],
               [[5, 8, 9, 10, 13], -1],
               [[5, 9, 13, 12],  -1],
               [[0, 4, 8, 12], 0],
               [[8, 9, 12, 13], -2],
             ]

    def __init__(self, x, y):
        global numberOfFigures
        global lastYPos
        self.x = x
        self.y = y
        self.type = Figure.nextFigure
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0
        Figure.nextFigure += 1 # rotate through figures
        Figure.nextFigure = Figure.nextFigure % len(Figure.figures)
        self.offset = self.figures[self.type][1]
        numberOfFigures += 1
        if numberOfFigures == 2022:
            print("Done!")
            print(lastYPos)
            sys.exit(1)

    def image(self):
        return self.figures[self.type][0]

class Tetris:
    state = "start"
    field = []
    
    score = 0
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 6 
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.state = "start"
        self.score = 0

        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        global lastYPos
        global numberOfFigures
        self.score = ("%i - %i" % (numberOfFigures, lastYPos))
        ## need to edit here
        self.figure = Figure(2, lastYPos - 2) # at least need to edit type

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                                intersection = True
        return intersection


    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeroes = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeroes += 1

            if zeroes == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]

        #self.score += lines ** 2

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()


    def freeze(self):
        global lastYPos
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        # remember last y pos to insert at right point
        lastYPos = self.figure.y - self.figure.offset - 5 # figure offset + move to lower left coord
        #self.break_lines()
        self.new_figure()
        #if self.intersects():
        #    self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x
        


pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Elftris")

done = False
clock = pygame.time.Clock()
fps = 20000
game = Tetris(height, width)
counter = 0

# Movement code - needs to be read from file later
movepos = 0
movementCode = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1

    if counter > 100000:
        counter = 0

    if counter % 1 == 0:
        if game.state == "start":
            movement = movementCode[movepos]
            movepos += 1
            movepos = movepos % len(movementCode) 
            #print(movepos)
            #print(movement)

            if movement == "<":
                game.go_side(-1)
            elif movement == ">":
                game.go_side(1)
            else:
                raise Exception("Unexpected movement")


            game.go_down()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
