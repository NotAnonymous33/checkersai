import pygame
from constants import *
from board import Board

pygame.init()





clock = pygame.time.Clock()
running = True

board = Board()
pygame.display.set_caption("Checkers by Anonymous33")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or board.check_quit():
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            board.click(pos[0], pos[1])

    pos = pygame.mouse.get_pos()

    board.draw(pos[0], pos[1])
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



