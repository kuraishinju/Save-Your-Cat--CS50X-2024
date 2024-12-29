# Save Your Cat - final project for CS50X 2024
### Video Demo:  <URL HERE>
### Description:
**Save the Cat** is a *choose your own adventure*-style game developed in Python using the Pygame library. The player assumes the role of a character in a fantasy world inhabited by talking animals. Their mission is to rescue their beloved cat, who has been kidnapped and taken to the Land of Retrievers, a realm ruled by dogs. The story is relatively short and features two possible endings.

I developed this game after studying programming basics for two and a half months as part of CS50X 2024. Before this, I had no prior programming experience, so this is my first attempt at creating a program entirely from scratch. Except for the elements credited in the [Additional Credits](#additional-credits) section, the story and code were entirely created by me.

The idea of developing this game comes from my love for cats and my desire of challenging myself by learning Python through a project that required skills and knowledge beyond what I acquired during the course.

### The Game:
At the start of the game, the player encounters a menu screen where they must make two inputs:  
1. A selection between *three choices* (inspired by D&D classes).  
2. A name for the cat (a string with a maximum of 10 characters).  

If these requirements are not met, or if the string contains non-alphabetical characters, an error message is displayed.

When the player clicks *Play*, the story screens are rendered incorporating the inputs provided by the user. These screens consist of text accompanied by one or two choices. The game has two different endings, and in both cases the player can either exit the game or return to the main menu. There is no save system as the game is short and can be completed in 1-2 minutes.

### Additional Credits:
- **Cat image**: [PNG Wing](https://www.pngwing.com/)  
- **Word-wrapped text display module** (in *helpers.py*, `class TextRectException` and `def render_textrect`): [David Clark](https://www.pygame.org/pcr/text_rect/index.php)  

This game was developed with the help of **ChatGPT** and **GitHub Copilot**, primarily for tasks such as debugging with print statements (not present in the final version) and splitting the `pygame_gui` UI manager code I wrote into multiple files. AI has also been used to correct any writing mistakes in this `README.md` file and the story since English is not my first language.

The code of this game has also been reviewed by third parties, who helped me identify some bugs and improve code readability and optimization during its development. However, no part of the code was written by them.
