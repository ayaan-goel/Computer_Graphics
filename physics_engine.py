import pymunk
from random import randrange

def create_space():
    """Initialize physics space with gravity."""
    space = pymunk.Space()
    space.gravity = (0, 900)
    return space

def add_static_floor(space, width, height):
    """Creates floor surface."""
    floor = pymunk.Segment(space.static_body, (0, height - 50), (width, height - 50), 10)
    floor.elasticity = 0.8
    floor.friction = 1.0
    space.add(floor)
    return floor

def create_ball(space, pos, radius=40):
    """Generates a dynamic ball with random color and given radius."""
    mass = radius / 5
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.8
    shape.friction = 0.5
    shape.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255), 255)
    space.add(body, shape)
    return shape
