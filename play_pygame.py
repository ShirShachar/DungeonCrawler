# type: ignore
import pygame
import time
from play import Game

# Constants
TILE_SIZE = 20
FPS = 10

# Base cell size and scaling
BASE_CELL_SIZE = 20
CELL_SIZE_SCALING = {
    1: 20,
    2: 20,
    3: 15,
    4: 12,
    5: 10   # Level 5: 50% of original size
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


def show_victory_screen(screen, width, height):
    """Show victory screen and ask to play again"""
    # Create semi-transparent overlay
    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    # Show victory message
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
    # Create semi-transparent overlay
    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    # Show game over message
    font_large = pygame.font.Font(None, 72)
    game_over_text = font_large.render("💀 GAME OVER 💀", True, COLOR_ENEMY)
    text_rect = game_over_text.get_rect(center=(width/2, height/2))
    screen.blit(game_over_text, text_rect)

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


def show_level_transition_screen(screen, width, height, next_level):
    """Show level transition screen"""
    # Create semi-transparent overlay
    overlay = pygame.Surface((width, height + 120))
    overlay.fill(COLOR_BG)
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))

    # Show level message
    font_large = pygame.font.Font(None, 72)
    level_text = font_large.render(f"Level {next_level}", True, COLOR_VICTORY)
    text_rect = level_text.get_rect(center=(width/2, height/2))
    screen.blit(level_text, text_rect)

    # Show continue message
    font_medium = pygame.font.Font(None, 48)
    continue_text = font_medium.render(
        "Press SPACE to continue", True, COLOR_TEXT)
    continue_rect = continue_text.get_rect(center=(width/2, height/2 + 60))
    screen.blit(continue_text, continue_rect)

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


def show_welcome_screen(screen, width, height):
    """Show welcome screen with game title and start instructions"""
    # Create background
    screen.fill(COLOR_BG)

    # Draw main title
    font_title = pygame.font.Font(None, 120)  # Large font for title
    title_text = font_title.render("DUNGEON", True, COLOR_VICTORY)
    title_rect = title_text.get_rect(center=(width/2, height/2 - 60))
    screen.blit(title_text, title_rect)

    # Draw subtitle
    # Slightly smaller for subtitle
    font_subtitle = pygame.font.Font(None, 100)
    subtitle_text = font_subtitle.render("CRAWLER", True, COLOR_VICTORY)
    subtitle_rect = subtitle_text.get_rect(center=(width/2, height/2 + 20))
    screen.blit(subtitle_text, subtitle_rect)

    # Draw instructions with shadow effect
    font_medium = pygame.font.Font(None, 48)
    # Shadow
    start_text_shadow = font_medium.render(
        "Press SPACE to Start", True, COLOR_BG)
    start_rect_shadow = start_text_shadow.get_rect(
        center=(width/2 + 2, height - 150 + 2))
    screen.blit(start_text_shadow, start_rect_shadow)
    # Main text
    start_text = font_medium.render("Press SPACE to Start", True, COLOR_TEXT)
    start_rect = start_text.get_rect(center=(width/2, height - 150))
    screen.blit(start_text, start_rect)

    # Draw game description with shadow effect
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


def main():
    pygame.init()  # type: ignore

    while True:  # Main game loop that allows for restart
        # Initial window size for welcome screen
        window_width = 800
        window_height = 600
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Dungeon Crawler")

        # Show welcome screen
        if not show_welcome_screen(screen, window_width, window_height):
            pygame.quit()
            return

        current_level = 1
        game = Game(current_level)

        # Calculate cell size based on level
        cell_size = CELL_SIZE_SCALING[current_level]
        window_width = game.dungeon.width * cell_size
        window_height = game.dungeon.height * cell_size + 60  # Extra space for UI
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(f"Dungeon Crawler - Level {current_level}")

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        last_move = None

        # Game running loop
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

            # Draw everything
            screen.fill(COLOR_BG)

            # Draw dungeon
            for y in range(game.dungeon.height):
                for x in range(game.dungeon.width):
                    rect = pygame.Rect(x * cell_size, y *
                                       cell_size, cell_size, cell_size)
                    if game.dungeon.map[y][x] == '#':
                        pygame.draw.rect(screen, COLOR_WALL, rect)
                    else:
                        pygame.draw.rect(screen, COLOR_FLOOR, rect)

            # Draw items
            for item in game.items:
                rect = pygame.Rect(item.x * cell_size,
                                   item.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, COLOR_ITEM, rect)

            # Draw enemies
            for enemy in game.enemies:
                rect = pygame.Rect(enemy.x * cell_size,
                                   enemy.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, COLOR_ENEMY, rect)

            # Draw player
            player_rect = pygame.Rect(
                game.player.x * cell_size, game.player.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, COLOR_PLAYER, player_rect)

            # Draw UI
            health_text = font.render(
                f"Health: {game.player.health}", True, COLOR_TEXT)
            enemies_text = font.render(
                f"Enemies: {len(game.enemies)}", True, COLOR_TEXT)
            level_text = font.render(
                f"Level: {current_level}", True, COLOR_TEXT)
            # Show potions in gold color
            potions_text = font.render(
                f"Potions: {len(game.inventory)}", True, COLOR_ITEM)

            # Add keyboard controls
            controls_font = pygame.font.Font(
                None, 24)  # Smaller font for controls
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
                        # Store current inventory
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
