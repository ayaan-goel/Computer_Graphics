import pygame
import pymunk
import random

# 🎨 Define your 5 fixed ball colors
BALL_COLORS = [
    (0, 255, 255),    # Neon Blue (cyan glow)
    (57, 255, 20),    # Neon Green (electric lime)
    (191, 0, 255),    # Neon Purple (vivid violet)
    (255, 255, 0),    # Neon Yellow (laser yellow)
    (255, 83, 13),    # Neon Orange (hot orange)
    (255, 20, 147),   # Neon Pink (electric pink)
]



def create_space():
    """Create a new Pymunk space with gravity."""
    space = pymunk.Space()
    space.gravity = (0, 900)  # Downward gravity (pixels/s²)
    return space


def add_static_floor(space, width, height):
    """Add a static floor at the bottom of the screen."""
    floor_y = height - 50
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (0, floor_y), (width, floor_y), 5)
    shape.elasticity = 0.8
    shape.friction = 0.8
    space.add(body, shape)
    return shape


def create_ball(space, position, radius=None):
    """Create a colorful ball with random size and color."""
    # 🎯 Randomize ball radius if not provided
    if radius is None:
        radius = random.randint(10, 100)  # between 20 and 60 pixels

    mass = 1
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = position

    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.8
    shape.friction = 0.5

    # Pick a random color from your 5 choices
    color = random.choice(BALL_COLORS)
    shape.color = pygame.Color(*color, 255)

    space.add(body, shape)
    return shape


def draw_balls(space, surface):
    """Draw all colored balls (supports random sizes)."""
    for shape in space.shapes:
        if isinstance(shape, pymunk.shapes.Circle):
            pos = int(shape.body.position.x), int(shape.body.position.y)
            radius = int(shape.radius)
            color = shape.color
            pygame.draw.circle(surface, color, pos, radius)
