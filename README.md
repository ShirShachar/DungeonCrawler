# Dungeon Delver: A Rogue-lite Dungeon Crawler

Dungeon Delver is a lightweight rogue-lite dungeon crawler game where players explore procedurally generated dungeons, battle a variety of enemies, and collect powerful items to survive. With both a text-based and a graphical interface built using Pygame, the game offers a classic dungeon-crawling experience with modern Python mechanics.

Developed as a final project for a Python programming course.

# 🕹️ How to Play
1. Installation
Ensure you have Python installed, then install the required library:
bash
Copy
Edit
pip install pygame

2. Run the Game
You can play in either mode:
 Text-Based Mode (Terminal):
 bash
 Copy
 Edit
 python play.py

 Graphical Mode (Pygame):
 bash
 Copy
 Edit
 python play_pygame.py

3. Controls
Action	Key
Move	W A S D
Attack	F
Use Potion	U
Quit Game	Q

# 🔑 Key Features
- Procedurally Generated Dungeons: Each level layout is uniquely generated.
- Progressive Difficulty: Survive 5 levels with increasingly challenging enemies.
- Varied Enemy Types: Face off against melee attackers and long-range spellcasting wizards.
- Item System: Collect and use health potions to stay alive.
- Interactive Combat: Turn-based battles with positioning and timing.
- Graphical Interface: Simple 2D visuals using Pygame with grid-based sprites.

# 🧩 Project Structure
File	Purpose
play.py	Core game logic with a text-based interface
play_pygame.py	Graphical version using Pygame
entities.py	Definitions for enemies and their behaviors
dungeon.py	Dungeon layout generation
items.py	Item logic (e.g. health potions)

# 📦 Requirements
Python 3.x
Pygame

Have fun exploring the dungeon! 🗝️💥🧟‍♂️
