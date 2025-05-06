# type: ignore
import pygame
import time
from play import Game

# Constants
TILE_SIZE = 20
FPS = 10

# size of the screen
BASE_CELL_SIZE = 20
CELL_SIZE_SCALING = {
    1: 20,
    2: 20,
    3: 15,
    4: 14,  # Increased from 12 for better visibility
    5: 14   # Increased from 10 for better visibility
}

COLOR_BG = (40, 40, 40)        # Dark gray background
COLOR_WALL = (100, 100, 100)   # Medium gray walls
COLOR_FLOOR = (60, 60, 60)     # Slightly lighter than background
COLOR_PLAYER = (50, 205, 50)   # Bright green
COLOR_ENEMY = (220, 20, 60)    # Crimson red
COLOR_ITEM = (255, 215, 0)     # Gold color for items
COLOR_TEXT = (255, 255, 255)   # White text
COLOR_UI_BG = (50, 50, 50)     # UI background
COLOR_HEALTH_BG = (80, 80, 80)  # Health bar background
COLOR_HEALTH_FILL = (0, 255, 0)  # Green health bar
COLOR_VICTORY = (255, 215, 0)  # Gold color for victory text
COLOR_WIZARD = (148, 0, 211)   # Dark violet for wizard enemies
COLOR_FIREBALL = (255, 140, 0)  # Dark orange for fireballs
COLOR_FIREBALL_CORE = (255, 69, 0)  # Redder orange for fireball center
FIREBALL_FRAMES = 10
FIREBALL_SIZES = [8, 6, 4]


def show_victory_screen(screen, width, height):
    """Show victory screen and ask to play again"""

    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    font_large = pygame.font.Font(None, 72)
    victory_text = font_large.render("🎉 VICTORY! 🎉", True, COLOR_VICTORY)
    text_rect = victory_text.get_rect(center=(width/2, height/2))
    screen.blit(victory_text, text_rect)

    # Show play again message
    font_medium = pygame.font.Font(None, 48)
    play_again_text = font_medium.render(
        "Press SPACE to play again or Q to quit", True, COLOR_TEXT)
    play_again_rect = play_again_text.get_rect(center=(width/2, height/2 + 60))
    screen.blit(play_again_text, play_again_rect)

    pygame.display.flip()

    # Wait for player input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    return False
    return False


def show_game_over_screen(screen, width, height):
    """Show game over screen and ask to play again"""

    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    font_large = pygame.font.Font(None, 72)
    game_over_text = font_large.render("💀 GAME OVER 💀", True, COLOR_ENEMY)
    text_rect = game_over_text.get_rect(center=(width/2, height/2))
    screen.blit(game_over_text, text_rect)

    font_medium = pygame.font.Font(None, 48)
    play_again_text = font_medium.render(
        "Press SPACE to play again or Q to quit", True, COLOR_TEXT)
    play_again_rect = play_again_text.get_rect(center=(width/2, height/2 + 60))
    screen.blit(play_again_text, play_again_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    return False
    return False


def show_level_transition_screen(screen, width, height, next_level):
    """Show level transition screen"""

    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    font_large = pygame.font.Font(None, 72)
    level_text = font_large.render(f"Level {next_level}", True, COLOR_VICTORY)
    text_rect = level_text.get_rect(center=(width/2, height/2))
    screen.blit(level_text, text_rect)

    font_medium = pygame.font.Font(None, 48)
    continue_text = font_medium.render(
        "Press SPACE to continue", True, COLOR_TEXT)
    continue_rect = continue_text.get_rect(center=(width/2, height/2 + 60))
    screen.blit(continue_text, continue_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    return False
    return False


def show_welcome_screen(screen, width, height):
    """Show welcome screen with game title and start instructions"""

    screen.fill(COLOR_BG)

    font_title = pygame.font.Font(None, 120)
    title_text = font_title.render("DUNGEON", True, COLOR_VICTORY)
    title_rect = title_text.get_rect(center=(width/2, height/2 - 60))
    screen.blit(title_text, title_rect)

    font_subtitle = pygame.font.Font(None, 100)
    subtitle_text = font_subtitle.render("CRAWLER", True, COLOR_VICTORY)
    subtitle_rect = subtitle_text.get_rect(center=(width/2, height/2 + 20))
    screen.blit(subtitle_text, subtitle_rect)

    font_medium = pygame.font.Font(None, 48)

    start_text_shadow = font_medium.render(
        "Press SPACE to Start", True, COLOR_BG)
    start_rect_shadow = start_text_shadow.get_rect(
        center=(width/2 + 2, height - 150 + 2))
    screen.blit(start_text_shadow, start_rect_shadow)

    start_text = font_medium.render("Press SPACE to Start", True, COLOR_TEXT)
    start_rect = start_text.get_rect(center=(width/2, height - 150))
    screen.blit(start_text, start_rect)

    font_small = pygame.font.Font(None, 32)
    # Shadow
    desc_text_shadow = font_small.render(
        "Navigate through dungeons, defeat enemies, collect potions!", True, COLOR_BG)
    desc_rect_shadow = desc_text_shadow.get_rect(
        center=(width/2 + 2, height - 100 + 2))
    screen.blit(desc_text_shadow, desc_rect_shadow)
    # Main text
    desc_text = font_small.render(
        "Navigate through dungeons, defeat enemies, collect potions!", True, COLOR_TEXT)
    desc_rect = desc_text.get_rect(center=(width/2, height - 100))
    screen.blit(desc_text, desc_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    return False
    return False


def animate_fireball(screen, start_pos, end_pos, cell_size):
    start_x = start_pos[0] * cell_size + cell_size // 2
    start_y = start_pos[1] * cell_size + cell_size // 2
    end_x = end_pos[0] * cell_size + cell_size // 2
    end_y = end_pos[1] * cell_size + cell_size // 2
    original_screen = screen.copy()
    for frame in range(FIREBALL_FRAMES + 1):
        screen.blit(original_screen, (0, 0))
        progress = frame / FIREBALL_FRAMES
        current_x = start_x + (end_x - start_x) * progress
        current_y = start_y + (end_y - start_y) * progress
        for i, size in enumerate(FIREBALL_SIZES):
            trail_progress = max(0, progress - i * 0.1)
            if trail_progress <= 1:
                trail_x = start_x + (end_x - start_x) * trail_progress
                trail_y = start_y + (end_y - start_y) * trail_progress
                pygame.draw.circle(screen, COLOR_FIREBALL,
                                   (int(trail_x), int(trail_y)), size)
        pygame.draw.circle(screen, COLOR_FIREBALL_CORE,
                           (int(current_x), int(current_y)), 4)
        pygame.display.flip()
        pygame.time.wait(20)
    screen.blit(original_screen, (0, 0))
    pygame.display.flip()


def main():
    pygame.init()

    while True:  # Main game loop that allows for restart
        # Initial window size for welcome screen
        window_width = 800
        window_height = 600
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Dungeon Crawler")

        # welcome screen
        if not show_welcome_screen(screen, window_width, window_height):
            pygame.quit()
            return

        current_level = 1
        game = Game(current_level)

        cell_size = CELL_SIZE_SCALING[current_level]
        window_width = game.dungeon.width * cell_size
        window_height = game.dungeon.height * cell_size + 60  # Extra space for UI
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(f"Dungeon Crawler - Level {current_level}")

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        last_move = None

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return
                    elif event.key == pygame.K_f:
                        game.attack_enemy()
                    elif event.key == pygame.K_u:
                        for item in game.inventory:
                            if item.effect == 'heal':
                                old_health = game.player.health
                                game.player.health = min(
                                    100, game.player.health + 3)
                                healed_amount = game.player.health - old_health
                                game.inventory.remove(item)

                                # Show healing message
                                heal_text = font.render(
                                    f"Healed for {healed_amount} HP!", True, COLOR_HEALTH_FILL)
                                screen.blit(
                                    heal_text, (10, window_height - 80))
                                pygame.display.flip()
                                # Show message for half a second
                                pygame.time.wait(500)
                                break
                    elif event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                        last_move = event.key
                        m_x, m_y = 0, 0
                        if event.key == pygame.K_w:
                            m_y = -1
                        elif event.key == pygame.K_s:
                            m_y = 1
                        elif event.key == pygame.K_a:
                            m_x = -1
                        elif event.key == pygame.K_d:
                            m_x = 1

                        new_x = game.player.x + m_x
                        new_y = game.player.y + m_y

                        if game.dungeon.map[new_y][new_x] != '#':
                            game.player.x = new_x
                            game.player.y = new_y

                            # Check for items at the new position
                            # Create a copy of the list to modify it safely
                            for item in game.items[:]:
                                if item.x == game.player.x and item.y == game.player.y:
                                    game.inventory.append(item)
                                    game.items.remove(item)
                                    # Add UI feedback for item collection
                                    pickup_text = font.render(
                                        f"Picked up {item.name}!", True, COLOR_TEXT)
                                    screen.blit(
                                        pickup_text, (10, window_height - 80))
                                    pygame.display.flip()
                                    # Show message for half a second
                                    pygame.time.wait(500)

                            game.enemies_move()

                            # Animate wizard fireballs if any were shot
                            for enemy in game.enemies:
                                if hasattr(enemy, 'can_shoot') and enemy.can_shoot:
                                    fireball = enemy.try_shoot_fireball(
                                        game.player.x, game.player.y, game.dungeon.map)
                                    if fireball:
                                        animate_fireball(
                                            screen, (enemy.x, enemy.y), (game.player.x, game.player.y), cell_size)
                                        game.player.health -= fireball['damage']
                                        damage_text = font.render(
                                            f"Took {fireball['damage']} fireball damage!", True, COLOR_FIREBALL)
                                        screen.blit(
                                            damage_text, (10, window_height - 80))
                                        pygame.display.flip()
                                        pygame.time.wait(500)

            # create the sceen
            screen.fill(COLOR_BG)

            for y in range(game.dungeon.height):
                for x in range(game.dungeon.width):
                    rect = pygame.Rect(x * cell_size, y *
                                       cell_size, cell_size, cell_size)
                    if game.dungeon.map[y][x] == '#':
                        pygame.draw.rect(screen, COLOR_WALL, rect)
                    else:
                        pygame.draw.rect(screen, COLOR_FLOOR, rect)

            # Draw items (health potions as hearts)
            for item in game.items:
                rect = pygame.Rect(item.x * cell_size,
                                   item.y * cell_size, cell_size, cell_size)

                # Clear background first
                pygame.draw.rect(screen, COLOR_FLOOR, rect)

                # Draw a heart shape for health items
                item_center_x = item.x * cell_size + cell_size // 2
                item_center_y = item.y * cell_size + cell_size // 2
                heart_size = int(cell_size * 0.4)

                # Top-left circle of heart
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),  # Red color
                    (item_center_x - heart_size//2, item_center_y - heart_size//4),
                    heart_size//2
                )

                # Top-right circle of heart
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),  # Red color
                    (item_center_x + heart_size//2, item_center_y - heart_size//4),
                    heart_size//2
                )

                # Bottom triangle of heart
                heart_triangle = [
                    (item_center_x - heart_size, item_center_y - heart_size//4),
                    (item_center_x + heart_size, item_center_y - heart_size//4),
                    (item_center_x, item_center_y + heart_size)
                ]
                pygame.draw.polygon(screen, (255, 0, 0), heart_triangle)

            # Draw enemies with larger emoji-like appearances
            for enemy in game.enemies:
                rect = pygame.Rect(enemy.x * cell_size,
                                   enemy.y * cell_size, cell_size, cell_size)

                # Fill background with floor color first for visibility
                pygame.draw.rect(screen, COLOR_FLOOR, rect)

                if hasattr(enemy, 'can_shoot') and enemy.can_shoot:
                    # Wizard enemy (purple with hat and angry eyes)
                    # Purple base face - make larger
                    enemy_center = (enemy.x * cell_size + cell_size //
                                    2, enemy.y * cell_size + cell_size // 2)
                    # Make face larger (almost filling the cell)
                    # Increase scaling for levels 4 and 5
                    scaling_factor = 0.48
                    if current_level >= 4:
                        # More moderate scaling that won't cause characters to overlap cells
                        scaling_factor = 0.65  # Reduced from 0.80 to avoid overlapping

                    # For level 5, reduce further to ensure better proportions
                    if current_level == 5:
                        scaling_factor = 0.60

                    enemy_radius = int(cell_size * scaling_factor)
                    pygame.draw.circle(screen, COLOR_WIZARD,
                                       enemy_center, enemy_radius)

                    # Black outline for visibility
                    pygame.draw.circle(screen, (0, 0, 0), enemy_center, enemy_radius, max(
                        1, int(cell_size * 0.05)))

                    # Wizard hat (triangle)
                    hat_points = [
                        (enemy.x * cell_size + cell_size // 2, enemy.y *
                         cell_size),  # Top of hat at top of cell
                        (enemy.x * cell_size + cell_size // 6, enemy.y *
                         cell_size + cell_size // 2),  # Wider base
                        (enemy.x * cell_size + 5 * cell_size //
                         6, enemy.y * cell_size + cell_size // 2)
                    ]
                    pygame.draw.polygon(screen, COLOR_VICTORY, hat_points)
                    pygame.draw.polygon(screen, (0, 0, 0), hat_points, max(
                        1, int(cell_size * 0.03)))  # Outline

                    # Angry eyes (slanted lines) - larger
                    eye_size = max(2, int(cell_size * 0.12))
                    left_eye_start = (
                        enemy_center[0] - enemy_radius // 2 - eye_size, enemy_center[1] - eye_size)
                    left_eye_end = (
                        enemy_center[0] - enemy_radius // 2 + eye_size, enemy_center[1] + eye_size)
                    right_eye_start = (
                        enemy_center[0] + enemy_radius // 2 - eye_size, enemy_center[1] + eye_size)
                    right_eye_end = (
                        enemy_center[0] + enemy_radius // 2 + eye_size, enemy_center[1] - eye_size)

                    pygame.draw.line(screen, (0, 0, 0), left_eye_start, left_eye_end, max(
                        2, int(cell_size * 0.08)))
                    pygame.draw.line(screen, (0, 0, 0), right_eye_start, right_eye_end, max(
                        2, int(cell_size * 0.08)))

                    # Fireball indicator if in range of player
                    if enemy.is_in_range(game.player.x, game.player.y):
                        center_x = enemy.x * cell_size + cell_size // 2
                        center_y = enemy.y * cell_size + \
                            (cell_size * 4) // 5  # Lower position
                        pygame.draw.circle(
                            # Larger
                            screen, COLOR_FIREBALL, (center_x, center_y), cell_size // 3)
                        # Add flame effect
                        pygame.draw.circle(
                            screen, COLOR_FIREBALL_CORE, (center_x, center_y), cell_size // 5)
                else:
                    # Regular enemy (red angry face) - make larger
                    enemy_center = (enemy.x * cell_size + cell_size //
                                    2, enemy.y * cell_size + cell_size // 2)
                    # Make face larger (almost filling the cell)
                    # Increase scaling for levels 4 and 5
                    scaling_factor = 0.48
                    if current_level >= 4:
                        # More moderate scaling that won't cause characters to overlap cells
                        scaling_factor = 0.65  # Reduced from 0.80 to avoid overlapping

                    # For level 5, reduce further to ensure better proportions
                    if current_level == 5:
                        scaling_factor = 0.60

                    enemy_radius = int(cell_size * scaling_factor)
                    pygame.draw.circle(screen, COLOR_ENEMY,
                                       enemy_center, enemy_radius)

                    # Draw black outline
                    pygame.draw.circle(screen, (0, 0, 0), enemy_center, enemy_radius, max(
                        1, int(cell_size * 0.05)))

                    # Angry eyes (slanted lines) - larger and thicker
                    eye_size = max(2, int(cell_size * 0.12))
                    left_eye_start = (
                        enemy_center[0] - enemy_radius // 2 - eye_size, enemy_center[1] - eye_size)
                    left_eye_end = (
                        enemy_center[0] - enemy_radius // 2 + eye_size, enemy_center[1] + eye_size)
                    right_eye_start = (
                        enemy_center[0] + enemy_radius // 2 - eye_size, enemy_center[1] + eye_size)
                    right_eye_end = (
                        enemy_center[0] + enemy_radius // 2 + eye_size, enemy_center[1] - eye_size)

                    pygame.draw.line(screen, (0, 0, 0), left_eye_start, left_eye_end, max(
                        2, int(cell_size * 0.08)))
                    pygame.draw.line(screen, (0, 0, 0), right_eye_start, right_eye_end, max(
                        2, int(cell_size * 0.08)))

                    # Frowning mouth (upside down arc) - larger
                    mouth_width = int(cell_size * 0.32)
                    mouth_rect = pygame.Rect(
                        enemy_center[0] - mouth_width,
                        enemy_center[1] + mouth_width // 2,
                        mouth_width * 2,
                        mouth_width
                    )
                    pygame.draw.arc(
                        screen,
                        (0, 0, 0),
                        mouth_rect,
                        3.14,  # Start angle (π radians)
                        6.28,  # End angle (2π radians = full circle)
                        max(2, int(cell_size * 0.07))  # Thicker line
                    )

            # Draw player as a perfect happy smiley face
            player_rect = pygame.Rect(
                game.player.x * cell_size, game.player.y * cell_size, cell_size, cell_size)

            # Fill cell with floor color first
            pygame.draw.rect(screen, COLOR_FLOOR, player_rect)

            # Draw face background (bright yellow circle)
            face_center = (game.player.x * cell_size + cell_size //
                           2, game.player.y * cell_size + cell_size // 2)

            # Larger face for higher levels
            scaling_factor = 0.48
            if current_level >= 4:
                # More moderate scaling that won't cause characters to overlap cells
                scaling_factor = 0.65  # Reduced from 0.80 to avoid overlapping

            # For level 5, reduce further to ensure better proportions
            if current_level == 5:
                scaling_factor = 0.60

            # Larger face to fill the cell
            face_radius = int(cell_size * scaling_factor)
            pygame.draw.circle(screen, (50, 205, 50),
                               face_center, face_radius)  # Green face using COLOR_PLAYER

            # Draw black outline for more visibility
            pygame.draw.circle(screen, (0, 0, 0), face_center,
                               face_radius, max(1, int(cell_size * 0.05)))

            # Draw eyes (circular black dots)
            eye_radius = max(2, int(cell_size * 0.1))
            eye_y_pos = face_center[1] - int(cell_size * 0.12)
            left_eye_pos = (face_center[0] - int(cell_size * 0.15), eye_y_pos)
            right_eye_pos = (face_center[0] + int(cell_size * 0.15), eye_y_pos)
            pygame.draw.circle(screen, (0, 0, 0),
                               left_eye_pos, eye_radius)  # Left eye
            pygame.draw.circle(screen, (0, 0, 0),
                               right_eye_pos, eye_radius)  # Right eye

            # Draw happy smile (curved black arc) - make it HAPPIER with a bigger smile
            smile_width = int(cell_size * 0.4)  # Wider smile
            smile_height = int(cell_size * 0.3)  # More curved smile
            smile_rect = pygame.Rect(
                face_center[0] - smile_width // 2,
                face_center[1] - smile_height // 4,
                smile_width,
                smile_height
            )
            # Draw smile with thicker line
            pygame.draw.arc(
                screen,
                (0, 0, 0),
                smile_rect,
                0,  # Start angle (radians)
                3.14,  # End angle (radians, π = half circle)
                max(2, int(cell_size * 0.07))  # Thicker line width
            )

            health_text = font.render(
                f"Health: {game.player.health}", True, COLOR_TEXT)
            enemies_text = font.render(
                f"Enemies: {len(game.enemies)}", True, COLOR_TEXT)
            level_text = font.render(
                f"Level: {current_level}", True, COLOR_TEXT)

            potions_text = font.render(
                f"Potions: {len(game.inventory)}", True, COLOR_ITEM)

            # Add keyboard controls
            controls_font = pygame.font.Font(None, 24)
            move_text = controls_font.render("Move: WASD", True, COLOR_TEXT)
            attack_text = controls_font.render("Attack: F", True, COLOR_TEXT)
            heal_text = controls_font.render("Use Potion: U", True, COLOR_TEXT)
            quit_text = controls_font.render("Quit: Q", True, COLOR_TEXT)

            # Draw all UI elements
            screen.blit(health_text, (10, window_height - 50))
            screen.blit(enemies_text, (200, window_height - 50))
            screen.blit(level_text, (400, window_height - 50))
            screen.blit(potions_text, (600, window_height - 50))

            # Draw controls at the bottom
            screen.blit(move_text, (10, window_height - 25))
            screen.blit(attack_text, (200, window_height - 25))
            screen.blit(heal_text, (400, window_height - 25))
            screen.blit(quit_text, (600, window_height - 25))

            pygame.display.flip()
            clock.tick(60)

            # Check game state
            if game.player.health <= 0:
                if show_game_over_screen(screen, window_width, window_height):
                    running = False  # Break the game loop to restart
                else:
                    pygame.quit()
                    return
            elif len(game.enemies) == 0:
                if current_level < 5:
                    # Show level transition screen
                    if show_level_transition_screen(screen, window_width, window_height, current_level + 1):
                        current_health = game.player.health  # Store current health

                        current_inventory = game.inventory[:]
                        current_level += 1
                        game = Game(current_level)
                        game.player.health = current_health  # Restore health in new level
                        game.inventory = current_inventory  # Restore inventory in new level
                        pygame.display.set_caption(
                            f"Dungeon Crawler - Level {current_level}")
                        # Recalculate window size for new level with scaled cell size
                        cell_size = CELL_SIZE_SCALING[current_level]
                        window_width = game.dungeon.width * cell_size
                        window_height = game.dungeon.height * cell_size + 60
                        screen = pygame.display.set_mode(
                            (window_width, window_height))
                    else:
                        pygame.quit()
                        return
                else:
                    if show_victory_screen(screen, window_width, window_height):
                        running = False  # Break the game loop to restart
                    else:
                        pygame.quit()
                        return


if __name__ == "__main__":
    print("=================")
    print("Welcome to Rogue-lite Dungeon Crawler game!")
    print("Goodluck")
    time.sleep(3)
    main()
