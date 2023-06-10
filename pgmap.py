from classes import *
from locations import *
import random
import pygame
import time
import threading


def pygo():
    pygame.init()
    

# Set the dimensions of the window
    window_width = 550
    window_height = 550
    tile_size = 50
    space_size = 10
    
    # Define colors
    WHITE = (249, 244, 245)
    RED = (255, 0, 0)
    BLACK = (46,49,56)

    # Create a Pygame window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Game Map")
    clock = pygame.time.Clock()
    running  =True
    window.fill(BLACK)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False

    

        for x in range(len(map_array)):
            
            for y in range(len(map_array[0])):
                tile = map_array[x][y]
                rect = pygame.Rect(x * (tile_size + space_size), y * (tile_size + space_size), tile_size, tile_size)

                if tile == me.location:
                    pygame.draw.rect(window, RED, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)

        pygame.display.update()
        clock.tick(60)
        
        # Draw the map
        

        # Control the frame rate
    

pygothread = threading.Thread(target=pygo)
pygothread.daemon = True
pygothread.start()