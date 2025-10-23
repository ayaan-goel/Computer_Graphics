import pygame
import pymunk
from physics_engine import create_space, add_static_floor, create_ball
from graphics import setup_draw, draw
from ui import draw_menu

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Puzzle Game")
clock = pygame.time.Clock()

# Initialize physics world
space = create_space()
add_static_floor(space, WIDTH, HEIGHT)
setup_draw(space, surface)

def run_game():
    global space
    running = True
    draw_menu(surface)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    space = create_space()
                    add_static_floor(space, WIDTH, HEIGHT)
                    setup_draw(space, surface)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    create_ball(space, pos, radius=40)

        # Update physics
        space.step(1 / FPS)
        draw(space, surface)
        pygame.display.flip()
        clock.tick(FPS)

run_game()
pygame.quit()
