import pygame
import pymunk
import time
from physics_engine import create_space, add_static_floor, create_ball
from graphics import setup_draw, draw
from ui import draw_menu, draw_hud, draw_game_over, draw_game_controls

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Puzzle Game")
clock = pygame.time.Clock()

# Game States
WELCOME, PLAYING, GAME_OVER = "WELCOME", "PLAYING", "GAME_OVER"
state = WELCOME

# Game variables
ball_count = 0
start_time = None
elapsed_time = 0
space = None

# Buttons
start_button = draw_menu(surface)
restart_button = None
home_button = None
quit_button = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # --- MENU SCREEN ---
            if state == WELCOME and start_button.collidepoint(pos):
                space = create_space()
                add_static_floor(space, WIDTH, HEIGHT)
                setup_draw(space, surface)
                start_time = time.time()
                ball_count = 0
                state = PLAYING

            # --- GAMEPLAY ---
            elif state == PLAYING:
                # Check for top control buttons
                if restart_button and restart_button.collidepoint(pos):
                    space = create_space()
                    add_static_floor(space, WIDTH, HEIGHT)
                    setup_draw(space, surface)
                    start_time = time.time()
                    ball_count = 0

                elif home_button and home_button.collidepoint(pos):
                    start_button = draw_menu(surface)
                    state = WELCOME

                elif quit_button and quit_button.collidepoint(pos):
                    # Force end → show game over screen with score
                    state = GAME_OVER

                # Add ball on left-click
                elif event.button == 1:
                    create_ball(space, pos, radius=40)
                    ball_count += 1

            # --- GAME OVER ---
            elif state == GAME_OVER:
                if restart_button and restart_button.collidepoint(pos):
                    space = create_space()
                    add_static_floor(space, WIDTH, HEIGHT)
                    setup_draw(space, surface)
                    start_time = time.time()
                    ball_count = 0
                    state = PLAYING
                elif home_button and home_button.collidepoint(pos):
                    start_button = draw_menu(surface)
                    state = WELCOME

    # --- GAME LOGIC ---
    if state == PLAYING:
        elapsed_time = int(time.time() - start_time)
        time_left = max(0, 10 - elapsed_time)

        if time_left <= 0:
            state = GAME_OVER
            continue

        space.step(1 / FPS)
        draw(space, surface)

        # HUD and Control Buttons
        draw_hud(surface, time_left, ball_count)
        restart_button, home_button, quit_button = draw_game_controls(surface)

        pygame.display.flip()

    elif state == WELCOME:
        pass  # Menu already drawn

    elif state == GAME_OVER:
        # 🔁 Continuously redraw the pulsing game-over text
        restart_button, home_button = draw_game_over(surface, ball_count)
        pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
