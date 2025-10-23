import pygame

font = pygame.font.SysFont("Arial", 28)

def draw_text(surface, text, pos, color=(255, 255, 255)):
    """Render centered text."""
    msg = font.render(text, True, color)
    rect = msg.get_rect(center=pos)
    surface.blit(msg, rect)

def draw_menu(surface):
    """Draw initial instructions."""
    surface.fill((0, 0, 50))
    draw_text(surface, "Physics Puzzle Game", (400, 250))
    draw_text(surface, "Click to drop balls", (400, 300))
    draw_text(surface, "Press [R] to Reset, [Esc] to Quit", (400, 350))
    pygame.display.flip()
