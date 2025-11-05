import pygame
import pymunk.pygame_util
import os

pygame.init()
pymunk.pygame_util.positive_y_is_up = False
draw_options = None
background = None


def setup_draw(space, surface):
    """Prepare the background and draw options."""
    global draw_options, background
    draw_options = pymunk.pygame_util.DrawOptions(surface)

    base_path = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(base_path, "assets", "game_bg.png")

    # Load and scale to fill (cover-style)
    original = pygame.image.load(bg_path).convert()
    background = scale_to_fill(original, surface.get_size())


def scale_to_fill(image, screen_size):
    """
    Scale and crop the image to completely fill the screen
    (like CSS background-size: cover).
    """
    img_w, img_h = image.get_size()
    screen_w, screen_h = screen_size

    img_ratio = img_w / img_h
    screen_ratio = screen_w / screen_h

    # Determine scale factor (zoom)
    if img_ratio > screen_ratio:
        # Image is wider -> scale based on height, crop sides
        new_h = screen_h
        new_w = int(new_h * img_ratio)
    else:
        # Image is taller -> scale based on width, crop top/bottom
        new_w = screen_w
        new_h = int(new_w / img_ratio)

    scaled_img = pygame.transform.smoothscale(image, (new_w, new_h))

    # Center-crop to exactly fit screen size
    x = (new_w - screen_w) // 2
    y = (new_h - screen_h) // 2
    cropped = scaled_img.subsurface((x, y, screen_w, screen_h)).copy()

    return cropped


def draw(space, surface):
    """Draw the scaled background and Pymunk debug shapes."""
    surface.blit(background, (0, 0))
    space.debug_draw(draw_options)
