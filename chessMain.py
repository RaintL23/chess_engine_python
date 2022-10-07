"""
This is the main driver file. It will responsible for handling user input and displaying the Current GameState object.
"""

import pygame as p
import chessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMESION = 8 #dimensions for a chess board are 8x8
SQ_SIZE = HEIGHT // DIMESION
MAX_FPS = 15 #for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main.
'''
def load_images():
    pieces = ['wp','bp','bB','wB','bK','wK','bQ','wQ','bN','wN','wR','bR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("resources/images/pieces/"+piece+".png"),(SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'
    pass

'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.gameState()
    load_images() #only do this once, before the while loop
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
    
    pass

'''
Responsible for all the graphics within a current game state.
'''
def draw_game_state(screen,gs):
    draw_board(screen) #draw squares on the board
    # add in piece highlightning or move suggestions (later)
    draw_pieces(screen,gs.board) #draw pieces on top of those squares
    pass

'''
Draw squares on the board. The top left square is always light.
'''
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMESION):
        for c in range(DIMESION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    pass

'''
Draw pieces on the board using the current GameState.board
'''
def draw_pieces(screen, board):
    for r in range(DIMESION):
        for c in range(DIMESION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    pass

if __name__ == "__main__":
    main()