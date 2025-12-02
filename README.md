# CHE-120: Dumb Ways to Waterloo

This repository contains a collection of text-based minigames grouped
into a single launcher called `Main_Game.py`. These minigames are loosely inspired by the game Dumb Ways to Die, but customized to the University of Waterloo Chemical Engineering student experience. The laucher `Main_Game.py` implements 6 main mini games. The overall highscore of this game is stored in `highscore.txt`.

Contents
--------
 - `Main_Game.py`: game launcher that lets players choose and play a single minigame or play
	 in classic Survival Mode. The launcher includes a menu to:
	 - Start Game (randomized)
	 - Play a single minigame
	 - Change difficulty
	 - Toggle Cruel Mode (cause time limits to shrink during survival)
	 - View credits
 
List of minigames
-----------------
	-Safety_Inspection_Minigame.py
	-do_your_homework.py
	-find_exam_desk.py
	-dana_porter_elevator.py
	-Sarah V1.py
	-Madi's_Contribution.py

Basic idea
----------
Each minigame will ask the user to do a task within a time limit. This usually includes selecting a response or typing into the terminal. When the player successfully completes the task, it will return `True` or it will return `False` if the user is not successful. In survival mode, each player has 3 lives. Other modes like cruel mode adjust the speed in which the tasks need to be completed as the player progresses through the levels, similar to the game Dumb Ways to Die.

How to run
----------
Open a terminal, `cd` into the repo root, then run:

```bash
python3 Main_Game.py
```

Main Menu & Difficulty
----------------------
When you start the game, a simplified main menu will appear. The menu lets you:

 - Start Game (randomized): the minigames will automatically be played in a
	 randomized order and you will have a number of lives until the game ends. If "Cruel Mode" is enabled, the per-minigame time limit will decrease as you get more wins, so the game gets harder the
	 better you do.
 - Difficulty: choose from Easy / Normal / Hard or a Custom time limit for each mini game.
	Each minigame will display the effective time for its prompt so the player knows
	how long they have.
  
- Quit: exit the game laucher.

Contributors
-----------------
Katherine Kurti, Madilyn Schaus, Krist Sirichan, Sarah Yendall

Enjoy! 🎮
