import pygame
import math
import time

pygame.init()
font = pygame.font.SysFont("Arial", 28)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", 30)

# Use Bazooka font if available, otherwise fallback
try:
    GAME_OVER_FONT_NAME = "Bazooka"
    bazooka_font_big = pygame.font.SysFont(GAME_OVER_FONT_NAME, 80)
    bazooka_font_medium = pygame.font.SysFont(GAME_OVER_FONT_NAME, 50)
except:
    GAME_OVER_FONT_NAME = "Arial Black"
    bazooka_font_big = pygame.font.SysFont(GAME_OVER_FONT_NAME, 80)
    bazooka_font_medium = pygame.font.SysFont(GAME_OVER_FONT_NAME, 50)


def load_image(path, size=(800, 600)):
    img = pygame.image.load(path).convert()
    img = pygame.transform.scale(img, size)
    return img


def draw_text(surface, text, pos, color=(0, 0, 0), font_type=font):
    msg = font_type.render(text, True, color)
    rect = msg.get_rect(center=pos)
    surface.blit(msg, rect)


def draw_menu(surface):
    home_bg = load_image("assets/home_bg.png")
    surface.blit(home_bg, (0, 0))

    draw_text(surface, "Physics Puzzle Game", (400, 200), (0, 0, 0))
    draw_text(surface, "Click START to Begin", (400, 280), (0, 0, 0))

    start_button = pygame.Rect(350, 350, 100, 50)
    pygame.draw.rect(surface, (0, 200, 0), start_button, border_radius=10)
    draw_text(surface, "START", start_button.center, (0, 0, 0))

    pygame.display.flip()
    return start_button


def draw_hud(surface, time_left, ball_count):
    WHITE = (255, 255, 255)
    SHADOW = (0, 0, 0)
    x1, y1 = 10, 10
    x2, y2 = 680, 10

    # Shadow (offset)
    surface.blit(font.render(f"Time: {time_left}s", True, SHADOW), (x1 + 2, y1 + 2))
    surface.blit(font.render(f"Balls: {ball_count}", True, SHADOW), (x2 + 2, y2 + 2))
    # Main text
    surface.blit(font.render(f"Time: {time_left}s", True, WHITE), (x1, y1))
    surface.blit(font.render(f"Balls: {ball_count}", True, WHITE), (x2, y2))


def draw_game_controls(surface):
    """Draw restart (🔁), home (🏠), and abort (⏹) icons at top center — no background."""
    icon_size = 40
    spacing = 60
    total_width = 3 * icon_size + 2 * spacing
    start_x = (800 - total_width) // 2 + icon_size // 2
    y_pos = 30

    restart_button = pygame.Rect(start_x - icon_size // 2, y_pos - icon_size // 2, icon_size, icon_size)
    home_button = pygame.Rect(start_x + icon_size + spacing - icon_size // 2, y_pos - icon_size // 2, icon_size, icon_size)
    quit_button = pygame.Rect(start_x + 2 * (icon_size + spacing) - icon_size // 2, y_pos - icon_size // 2, icon_size, icon_size)

    draw_text(surface, "🔁", restart_button.center, (255, 255, 255), emoji_font)
    draw_text(surface, "🏠", home_button.center, (255, 255, 255), emoji_font)
    draw_text(surface, "⏹", quit_button.center, (255, 255, 255), emoji_font)

    return restart_button, home_button, quit_button


def draw_game_over(surface, score):
    """Display Game Over screen with animated pulsing white text."""
    gameover_bg = load_image("assets/gameover_bg.png")
    surface.blit(gameover_bg, (0, 0))

    title = "Time's Up!"
    score_text = f"Your Score: {score}"

    # 💫 Pulse animation (based on time)
    t = time.time()
    scale = 1.0 + 0.08 * math.sin(t * 4)  # slightly faster & bigger pulse

    def draw_shadow_text(text, pos, font_name, base_size, color, scale=1.0):
        """Draw pulsing text with shadow effect."""
        font_size = int(base_size * scale)
        scaled_font = pygame.font.SysFont(font_name, font_size, bold=True)
        shadow = scaled_font.render(text, True, (0, 0, 0))
        msg = scaled_font.render(text, True, color)
        rect = msg.get_rect(center=pos)
        surface.blit(shadow, (rect.x + 4, rect.y + 4))
        surface.blit(msg, rect)

    # Draw pulsing “Time’s Up!” and static “Your Score”
    draw_shadow_text(title, (400, 150), GAME_OVER_FONT_NAME, 90, (255, 255, 255), scale)
    draw_shadow_text(score_text, (400, 250), GAME_OVER_FONT_NAME, 55, (255, 255, 255), 1.0)

    # Buttons
    restart_button = pygame.Rect(250, 360, 120, 50)
    home_button = pygame.Rect(450, 360, 120, 50)

    draw_text(surface, "🔁", restart_button.center, (255, 255, 255), emoji_font)
    draw_text(surface, "🏠", home_button.center, (255, 255, 255), emoji_font)

    return restart_button, home_button
