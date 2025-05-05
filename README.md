# COMS W2132 Intermediate Computing in Python, Final Project 
## <Dungeon Delver: A Rogue-lite Dungeon Crawler>

### Author:
- [Shir Shachar](https://github.com/ShirShachar) <ss6814@columbia.edu>
 
Replace the author name/email with your information.

## Project Description
Add an initial Project description here. There is no requirement for the length of the proposal. A paragraph or two may be enough -- just to get an idea of what you might want to work on. 

For my final project, I’m building a game called Dungeon Delver, inspired by classic rogue-lite dungeon crawlers. The idea is to create a simple top-down dungeon exploration game where the player explores procedurally generated levels, fights off enemies, and collects useful items to survive and get stronger. The game will start off text-based to get the core mechanics right — things like moving around, generating dungeon layouts, and combat. Once that’s working, I plan to build a basic 2D version using Pygame, so there’s a visual interface with a grid-based map and simple character sprites.

## Key Features:
* Procedurally Generated Dungeons: Every level has a unique layout with multiple rooms connected by corridors (randomly generated every time)
* Progressive Difficulty: 5 levels of increasing challenge with different enemies and larger maps
* Enemy Types: Regular melee enemies and wizards that can shoot fireballs from a distance
* Item Collection: Find and use health potions throughout the dungeon
* Interactive Combat: Engage in tactical combat with enemies
* Graphical Interface: Visual representation using Pygame with custom graphics
 
## Milestones: 
Milestone 1 - initial code, making sure it is working in the terminal (play.py)
Milestone 2 - adding a pygame file - play_pygame.py
Milestone 3 - adding features - emojies, level's difficulity, stronger enemies


For the revised project description, we will ask you to be more precise and think about how the entire project can be divided up into individual pieces or modules. It's useful to start thinkign about this now.

## Requirements 
If there are any hardware, software, or online services you think you are going to need, please list them in the Requirements section. This can be tentative for the initial proposal and the teaching staff can help identify resources.

-> Pygame

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


