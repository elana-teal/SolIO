import gui
import sys
import model
import pygame

def play(game : model.Game):
    pygame.init()
    gui.init()

    size = width, height = gui.SCREEN_SIZE
    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN \
            and event.key == pygame.K_r: 
                game.generates()

        game.auto()
        gui.draw_game(game, screen)
        pygame.display.flip()


game = model.Game()
game.generates()
#gui.display(game)
play(game)