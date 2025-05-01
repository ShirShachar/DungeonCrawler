# type: ignore
import pygame
import time
from play import Game

# Constants
TILE_SIZE = 20
FPS = 10

# Clean Color Scheme
COLOR_BG = (40, 40, 40)        # Dark gray background
COLOR_WALL = (100, 100, 100)   # Medium gray walls
COLOR_FLOOR = (60, 60, 60)     # Slightly lighter than background
COLOR_PLAYER = (50, 205, 50)   # Bright green
COLOR_ENEMY = (220, 20, 60)    # Crimson red
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


def main():
    pygame.init()

    while True:  # Main game loop
        game = Game()
        width = game.dungeon.width * TILE_SIZE
        height = game.dungeon.height * TILE_SIZE
        # Add extra height for the UI
        screen = pygame.display.set_mode((width, height + 120))
        pygame.display.set_caption("Dungeon Delver (Pygame)")
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    m_x, m_y = 0, 0
                    if event.key == pygame.K_w:
                        m_y = -1
                    elif event.key == pygame.K_s:
                        m_y = 1
                    elif event.key == pygame.K_a:
                        m_x = -1
                    elif event.key == pygame.K_d:
                        m_x = 1
                    elif event.key == pygame.K_f:
                        game.attack_enemy()
                    elif event.key == pygame.K_u:
                        for item in game.inventory:
                            if item.effect == 'heal':
                                game.player.health = min(
                                    100, game.player.health + item.value)
                                game.inventory.remove(item)
                                break
                    elif event.key == pygame.K_q:
                        return

                    # Move player if not attacking or using item
                    if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                        new_x = game.player.x + m_x
                        new_y = game.player.y + m_y
                        if game.dungeon.map[new_y][new_x] != '#':
                            game.player.x = new_x
                            game.player.y = new_y
                            game.enemies_move()

            # Fill background
            screen.fill(COLOR_BG)

            # Draw dungeon
            for y in range(game.dungeon.height):
                for x in range(game.dungeon.width):
                    rect = pygame.Rect(x * TILE_SIZE, y *
                                       TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if game.dungeon.map[y][x] == '#':
                        pygame.draw.rect(screen, COLOR_WALL, rect)
                    else:
                        pygame.draw.rect(screen, COLOR_FLOOR, rect)

            # Draw player
            px, py = game.player.x, game.player.y
            prect = pygame.Rect(px * TILE_SIZE, py *
                                TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLOR_PLAYER, prect)

            # Draw enemies
            for enemy in game.enemies:
                erect = pygame.Rect(enemy.x * TILE_SIZE,
                                    enemy.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, COLOR_ENEMY, erect)

            # Draw UI background
            pygame.draw.rect(screen, COLOR_UI_BG, (0, height, width, 120))

            # Draw health bar
            health_percent = game.player.health / 100
            health_width = 200
            health_rect = pygame.Rect(10, height + 10, health_width, 20)
            health_fill_rect = pygame.Rect(
                10, height + 10, health_width * health_percent, 20)
            pygame.draw.rect(screen, COLOR_HEALTH_BG, health_rect)
            pygame.draw.rect(screen, COLOR_HEALTH_FILL, health_fill_rect)

            # Draw health text
            font_small = pygame.font.Font(None, 36)
            health_text = font_small.render(
                f"Health: {game.player.health}", True, COLOR_TEXT)
            screen.blit(health_text, (10, height + 35))

            # Draw enemy count
            enemies_text = font_small.render(
                f"Enemies: {len(game.enemies)}", True, COLOR_TEXT)
            screen.blit(enemies_text, (10, height + 60))

            # Draw controls
            font_large = pygame.font.Font(None, 36)
            controls_text = font_large.render(
                "WASD: Move | F: Attack | U: Potion | Q: Quit", True, COLOR_TEXT)
            text_rect = controls_text.get_rect(center=(width/2, height + 100))
            screen.blit(controls_text, text_rect)

            pygame.display.flip()
            clock.tick(FPS)

            # Check game over conditions
            if game.player.health <= 0:
                if not show_game_over_screen(screen, width, height):
                    return
                break  # Start new game
            elif len(game.enemies) == 0:
                if not show_victory_screen(screen, width, height):
                    return
                break  # Start new game

    pygame.quit()


if __name__ == "__main__":
    print("=================")
    print("Welcome to Rogue-lite Dungeon Crawler game!")
    print("Goodluck")
    time.sleep(3)
    main()
