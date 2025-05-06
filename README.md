**Dungeon Delver**

## Project Overview
Dungeon Delver is a top-down, rogue-lite dungeon exploration game inspired by classic dungeon crawlers. Players explore procedurally generated levels, battle enemies, and collect items to survive and grow stronger with each run. Every dungeon layout is unique, offering a new challenge each time.

The project is being developed in two stages:
Stage 1: Core game mechanics (movement, dungeon generation, combat) are implemented in a text-based version to focus on logic and gameplay systems.
Stage 2: A 2D visual version is built using Pygame, featuring a grid-based map and simple character sprites.

The codebase is modular, with separate classes for the player, enemies, and dungeon grid to support clean design and easy future expansion.

## Development Roadmap
Milestone 1: Initial text-based version completed (movement, combat, procedural generation).
Milestone 2: Basic 2D Pygame implementation (grid, player and enemy sprites).
Milestone 3: Additional features: new enemy types, item system, enhanced procedural generation, UI improvements.

## Features
1. Randomly generated dungeon layouts
2. Basic combat system
3. Item collection and player upgrades
4. Simple 2D grid-based visual interface (Pygame)
5. Modular code structure for scalability

## How to play: 
1. Ensure you have Python installed on your system
2. Install Pygame:
   pip install pygame

3. running the game: 
You can run the game in two different modes:
 - Text-Based Mode (Terminal)
    python play.py

- Graphical Mode
    python play_pygame.py

4. Controls
Movement: WASD keys (W: up, A: left, S: down, D: right)
Attack: F key (when adjacent to an enemy)
Use Potion: U key (if you have health potions in your inventory)
Quit: Q key

5. Game Structure
play.py: Core game logic and text-based interface
play_pygame.py: Pygame implementation with graphical interface
entities.py: Enemy class definitions including regular enemies and wizards
dungeon.py: Procedural dungeon generation logic
items.py: Item class for collectible objects like health potions


Have Fun!
