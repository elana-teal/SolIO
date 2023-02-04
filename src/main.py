import gui
import sys
import model
from model import Card, CardType, Color
import time
import pygame

def play(game : model.Game):
    pygame.init()
    gui.init()

    pygame.display.set_caption('SolIO')
    Icon = pygame.image.load('res/icon.png')
    pygame.display.set_icon(Icon)

    size = width, height = gui.SCREEN_SIZE
    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    game.generates()
                if event.key == pygame.K_s:
                    game.auto()
            

        gui.draw_game(game, screen)
        pygame.display.flip()
        time.sleep(0.5)

#
game = model.Game()
#game.generates()

# For testing purpose
game.setState(columns=[
    [Card(CardType.NUMERAL,Color.RED,value=1)],
    [Card(CardType.NUMERAL,Color.GREEN,value=1)],
    [],
    [Card(CardType.NUMERAL,Color.RED,value=2)],
    [Card(CardType.NUMERAL,Color.BLUE,value=2)],
    [],
    [],
    []],
    reserves=[[Card(CardType.NUMERAL,Color.BLUE,value=1)],[],[]]
    )
play(game)