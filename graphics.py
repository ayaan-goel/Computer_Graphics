import pygame
import pymunk.pygame_util

pygame.init()
pymunk.pygame_util.positive_y_is_up = False
draw_options = None
background = None

def setup_draw(space, surface):
    """Setup drawing options and load background after display is ready."""
    global draw_options, background
    draw_options = pymunk.pygame_util.DrawOptions(surface)
    # Load background once the display has been set
    background = pygame.image.load("assets/background.png").convert()

def draw(space, surface):
    """Draw the physics world and background."""
    surface.blit(background, (0, 0))  # Draw background first
    space.debug_draw(draw_options)
