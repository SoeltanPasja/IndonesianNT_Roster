# Indonesian National Team Rosters Database

## Overview
This CRUD (Create, Read, Update, Delete) program manages the Indonesian National Team Rosters database. It allows users to view player statistics, add new players, remove players, update player data, rank players based on specific criteria, compare players, and suggest team formations. The program is implemented in Python and uses basic command-line interface (CLI) interactions.

## Features
- **Show Statistics**
  - View all players' statistics.
  - Calculate and display average goals by position.
  - Calculate and display average assists by position.
  - Calculate and display average age by position.
  - Identify and display the top-rated players by position.
  - Display players' goal contributions or G/A (goals + assists).

- **Add New Player(s)**
  - Add new players to the roster by providing their details.

- **Remove Player(s)**
  - Remove players from the roster by specifying their number.

- **Update Data**
  - Update existing player data by specifying the player number and the attribute to update.

- **Rank Players**
  - Rank players based on goals, assists, or ratings.

- **Compare Players**
  - Compare the statistics of two players by specifying their numbers or comparing all players from the same positions.

- **Suggest Team Formation**
  - Suggest a team formation based on predefined or custom formations and display the selected players.

- **Exit Program**
  - Exit the program.

## Requirements
- Python 3.x
- Basic understanding of Python programming

## How to Run the Program
1. Make sure you have Python installed on your device.
2. Copy the code provided into a Python script file (e.g., `indonesian_team_roster.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Run the script using the command: `python indonesian_team_roster.py`.

## Main Menu
Upon running the program, you will be presented with the main menu:

```
Welcome to Indonesian National Team Rosters Database

Main Menu:
1. Show Statistics
2. Add New Player(s)
3. Remove Player(s)
4. Update Data
5. Rank Players
6. Compare Players
7. Suggest Team Formation
8. Exit Program

Enter the number corresponding to the menu option you want to select.
```

## Viewing Statistics
Select option 1 from the main menu to view statistics. Choose from the sub-options to see specific statistics or to return to the main menu.

## Adding a New Player
Select option 2 from the main menu. Follow the prompts to enter the new player's details. Confirm the addition to update the roster.

## Removing a Player
Select option 3 from the main menu. Enter the number of the player you wish to remove. Confirm the removal to update the roster.

## Updating Player Data
Select option 4 from the main menu. Enter the number of the player you wish to update. Choose the attribute to update and enter the new value. Confirm the update to save changes.

## Ranking Players
Select option 5 from the main menu. Choose the attribute (goals, assists, ratings) to rank the players. View the ranked list of players.

## Comparing Players
Select option 6 from the main menu. Choose to compare just two players or compare players based on positions. View the comparative statistics of the two players.

## Suggesting Team Formation
Select option 7 from the main menu. Choose a predefined formation or create a custom formation. View the suggested team based on the chosen formation.

## Exiting the Program
Select option 8 from the main menu to exit the program.

## Data Structure
The player data is stored in a dictionary named `pemain` with the following keys:
- `name`: List of player names.
- `no`: List of player numbers.
- `age`: List of player ages.
- `position`: List of player positions (GK, DF, MF, FW).
- `club`: List of clubs the players belong to.
- `country`: List of countries where the players' clubs belong to.
- `goal`: List of goals scored by players.
- `assist`: List of assists made by players.
- `rating`: List of player ratings.

## Contribution
Feel free to contribute to this project by suggesting improvements, reporting bugs, or adding new features. You can contact the author or submit pull requests on the project's repository.

## License
This project is open-source and free to use. Please attribute the author when using or modifying the code.
