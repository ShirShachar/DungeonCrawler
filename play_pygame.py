# type: ignore
import pygame
import time
from play import Game

# Constants
TILE_SIZE = 20
FPS = 10

# Colors
COLOR_WALL = (255, 255, 255)  # White
COLOR_FLOOR = (200, 200, 200)  # Light grey
COLOR_PLAYER = (0, 200, 0)
COLOR_ENEMY = (200, 0, 0)
COLOR_TEXT = (255, 192, 203)  # Pink text
COLOR_BG_TEXT = (0, 0, 0)  # Black background for text


def main():
    pygame.init()
    game = Game()
    width = game.dungeon.width * TILE_SIZE
    height = game.dungeon.height * TILE_SIZE
    # Add extra height for the text
    screen = pygame.display.set_mode((width, height + 120))
    pygame.display.set_caption("Dungeon Delver (Pygame)")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                    # Debug print
                    print(f"Health after attack: {game.player.health}")
                elif event.key == pygame.K_u:
                    for item in game.inventory:
                        if item.effect == 'heal':
                            game.player.health = min(
                                100, game.player.health + item.value)
                            # Debug print
                            print(
                                f"Health after healing: {game.player.health}")
                            game.inventory.remove(item)
                            break
                elif event.key == pygame.K_q:
                    running = False

                # Move player if not attacking or using item
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    new_x = game.player.x + m_x
                    new_y = game.player.y + m_y
                    if game.dungeon.map[new_y][new_x] != '#':
                        game.player.x = new_x
                        game.player.y = new_y
                        game.enemies_move()
                        # Debug print
                        print(f"Enemies remaining: {len(game.enemies)}")

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
        prect = pygame.Rect(px * TILE_SIZE, py * TILE_SIZE,
                            TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, COLOR_PLAYER, prect)

        # Draw enemies
        for enemy in game.enemies:
            erect = pygame.Rect(enemy.x * TILE_SIZE, enemy.y *
                                TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLOR_ENEMY, erect)

        # Draw background rectangle for text
        pygame.draw.rect(screen, COLOR_BG_TEXT, (0, height, width, 120))

        # Draw health and enemy count with smaller font
        font_small = pygame.font.Font(None, 28)
        health_text = font_small.render(
            f"Health: {game.player.health}", True, COLOR_TEXT)
        enemies_text = font_small.render(
            f"Enemies: {len(game.enemies)}", True, COLOR_TEXT)
        screen.blit(health_text, (10, height + 10))
        screen.blit(enemies_text, (10, height + 40))

        # Controls text on a new line below
        font_large = pygame.font.Font(None, 28)
        controls_text = font_large.render(
            "Controls: WASD-Move | F-Attack | U-Potion | Q-Quit", True, COLOR_TEXT)
        screen.blit(controls_text, (10, height + 80))

        pygame.display.flip()
        clock.tick(FPS)

        # Check game over conditions
        if game.player.health <= 0:
            print("\nGame Over! You died 💀")
            running = False
        elif len(game.enemies) == 0:
            print("\n🎉 You defeated all the enemies! You win!")
            running = False

    pygame.quit()


if __name__ == "__main__":
    print("=================")
    print("Welcome to Rogue-lite Dungeon Crawler game!")
    print("Goodluck")
    time.sleep(3)
    main()
