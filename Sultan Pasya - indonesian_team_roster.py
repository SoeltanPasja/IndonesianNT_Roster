
pemain = {"name": ["Rian Putra", "Yakob Solossa", "Dedi Gunawan", "Achmad Al-Ahdal", "Arif Pratama", "Fajar Nugroho", "Iwan Setiawan", "Narendra Aksara", "Yudi Hartono", "Stephan Sudjatmiko", "Jacob Manulang", "Vino Pratama", "Wahyu Adi", "Xavier Putra", "Yoga Prasetya", "Zulfikar Ahmad", "Javier Ahmad"],
          "no": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21],
          "age": [29, 31, 24, 19, 28, 21, 25, 25, 23, 27, 29, 19, 33, 29, 17, 18, 22],
          "position": ["GK", "DF", "DF", "DF", "DF", "MF", "MF", "MF", "FW", "FW", "FW", "GK", "DF", "MF", "MF", "FW", "GK"],
          "club": ["Kashima Antlers", "Persipura", "Inter Miami", "Real Madrid", "Persib", "Barcelona", "FC Koln", "Liverpool", "Persija", "Ulsan Hyundai", "Bali United", "Persita", "Persebaya", "PSM", "Como 1907", "Como 1907", "PSMS"],
          "country": ["Japan", "Indonesia", "USA", "Spain", "Indonesia", "Spain", "Germany", "England", "Indonesia", "South Korea", "Indonesia", "Indonesia", "Indonesia", "Indonesia", "Italy", "Italy", "Indonesia"],
          "goal": [0, 2, 5, 1, 7, 2, 3, 13, 27, 19, 17, 0, 2, 4, 5, 8, 0],
          "assist": [1, 8, 1, 2, 13, 3, 8, 12, 3, 11, 10, 0, 3, 4, 10, 2, 0],
          "rating": [8.5, 7.7, 7.4, 7.8, 8.2, 7.4, 7.7, 8.9, 8.1, 8.3, 7.9, 7.3, 7.7, 7.4, 7.5, 7.3, 7.3]}

# Main Menu
def main_menu():
    print("Welcome to Indonesian National Team Rosters Database\n")
    print("Main Menu:")
    print("1. Show Statistics")
    print("2. Add New Player(s)")
    print("3. Remove Player(s)")
    print("4. Update Data")
    print("5. Rank Players")
    print("6. Compare Players")
    print("7. Suggest Team Formation")
    print("8. Exit Program")

# Menu 1 - Sub 1
def players_table():
    sorted_indices = sorted(range(len(pemain["no"])), key=lambda k: pemain["no"][k])
    print("\nIndonesian National Team Rosters\n")
    print(f"{'No.':<5} {'Name':<20} {'Pos.':<5} {'Age':<5} {'Club':<20} {'Country':<15} {'Goal(s)':<10} {'Assist(s)':<10} {'Rating':<10}")
    print("-" * 105)
    for idx in sorted_indices:
        print(f"{pemain['no'][idx]:<5} {pemain['name'][idx]:<20} {pemain['position'][idx]:<5} {pemain['age'][idx]:<5} {pemain['club'][idx]:<20} {pemain['country'][idx]:<15} {pemain['goal'][idx]:<10} {pemain['assist'][idx]:<10} {pemain['rating'][idx]:<10}")

# Menu 1 - Sub 2
def average_goals_by_position():
    positions_calculated = []
    for i in range(len(pemain["position"])):
        position = pemain["position"][i]
        if position not in positions_calculated:
            positions_calculated.append(position)
            total_goals = sum(pemain["goal"][j] for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            count = sum(1 for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            average_goals = total_goals / count if count != 0 else 0
            print(f"Average Goals for {position}: {average_goals:.2f}")

# Menu 1 - Sub 3
def average_assists_by_position():
    positions_calculated = []
    for i in range(len(pemain["position"])):
        position = pemain["position"][i]
        if position not in positions_calculated:
            positions_calculated.append(position)
            total_assists = sum(pemain["assist"][j] for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            count = sum(1 for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            average_assists = total_assists / count if count != 0 else 0
            print(f"Average Assists for {position}: {average_assists:.2f}")

# Menu 1 - Sub 4
def average_age_by_position():
    positions_calculated = []
    for i in range(len(pemain["position"])):
        position = pemain["position"][i]
        if position not in positions_calculated:
            positions_calculated.append(position)
            total_age = sum(pemain["age"][j] for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            count = sum(1 for j in range(len(pemain["name"])) if pemain["position"][j] == position)
            average_age = total_age / count if count != 0 else 0
            print(f"Average Age for {position}: {average_age:.2f}")

# Menu 1 - Sub 5
def top_rated_players_by_position():
    positions_calculated = []
    for i in range(len(pemain["position"])):
        position = pemain["position"][i]
        if position not in positions_calculated:
            positions_calculated.append(position)
            top_rating = -1
            top_player = None
            for j in range(len(pemain["name"])):
                if pemain["position"][j] == position and pemain["rating"][j] > top_rating:
                    top_rating = pemain["rating"][j]
                    top_player = pemain["name"][j]
            print(f"Top Rated Player for {position}: {top_player:<20} | Rating: {top_rating:.2f}")

# Menu 1 - Sub 6
def goal_contribution():
    contributions = []
    for i in range(len(pemain["name"])):
        contribution = pemain["goal"][i] + pemain["assist"][i]
        contributions.append((pemain["name"][i], contribution))
    contributions.sort(key=lambda x: x[1], reverse=True)
    print(f"{'Player':<20} {'G/A':<5}")
    print("-"*40)
    for name, contribution in contributions:
        print(f"{name:<20} {contribution:<5}")

# Menu 2 - Sub 1
def adding_players():
    while True:
        try:
            add_no = int(input("\nAdd the player's number: "))
            if add_no in pemain["no"]:
                print("The number already exists. Please enter a different number.")
                print(f"Existing numbers: {pemain['no']}")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    new_player = {}

    for attribute in pemain:
        if attribute == "no":
            new_player[attribute] = add_no
        else:
            while True:
                try:
                    if attribute == "age":
                        new_player[attribute] = int(input(f"Add the player's {attribute}: "))
                    elif attribute == "position":
                        pos = input(f"Add the player's {attribute} (GK, DF, MF, FW): ").upper()
                        if pos not in pemain["position"]:
                            print("Invalid position. Please enter one of the following: GK, DF, MF, FW.")
                            continue
                        new_player[attribute] = pos
                    elif attribute in ["goal", "assist"]:
                        new_player[attribute] = int(input(f"Add the player's {attribute}s: "))
                    elif attribute == "rating":
                        new_player[attribute] = float(input(f"Add the player's {attribute}: "))
                    elif attribute == "club":
                        new_player[attribute] = input(f"Add the player's {attribute}: ")
                        club = new_player[attribute]
                    elif attribute == "country":
                        new_player[attribute] = input(f"Add {club}'s country: ")
                    else:
                        new_player[attribute] = input(f"Add the player's {attribute}: ")
                    break
                except ValueError:
                    print(f"Invalid input. Please enter a valid {attribute}.")

    print(f"\nYou are about to add the following player:\n{new_player}\n")

    while True:
        confirm = input("Are you sure you want to add this player? (yes/no): ").strip().lower()
        if confirm in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if confirm == "yes":
        for attribute in pemain:
            pemain[attribute].append(new_player[attribute])

        print(f"\nPlayer {new_player['name']} added successfully.")
        players_table()
    else:
        print("\nPlayer addition cancelled.")

# Menu 3 - Sub 1
def remove_players():
    while True:
        try:
            remove = int(input("\nEnter the number of the player you want to remove: "))
            if remove not in pemain["no"]:
                raise IndexError

            remove_index = pemain["no"].index(remove)  # Find the index of the player to remove
            players_name = pemain["name"][remove_index]  # Save the player's name before deletion

            print(f"\nYou are about to remove the following player: {pemain['name'][remove_index]}\n")

            while True:
                confirm = input("Are you sure you want to remove this player? (yes/no): ").strip().lower()
                if confirm in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if confirm == "yes":
                for y in pemain:
                    del pemain[y][remove_index]  # Deleting the chosen index

                print(f"\nPlayer {players_name} removed successfully.")
                players_table()
            else:
                print("\nPlayer removal cancelled.")
            break

        except ValueError:
            print("Enter a valid player's number.")
        except IndexError:
            print("Index invalid. Please enter a valid player's number.")

# Menu 4 - Sub 1
def update_data():
    players_table()
    while True:
        try:
            player_no = int(input("\nEnter the player number to change: "))
            if player_no in pemain["no"]:
                player_index = pemain["no"].index(player_no)
                break
            else:
                print("Player number not found. Please enter a valid player number.")
        except ValueError:
            print("Invalid input. Please enter a valid player number.")
    
    while True:
        print("\nSelect attribute to change:")
        attributes = list(pemain.keys())
        for i, attr in enumerate(attributes, start=1):
            print(f"{i}. {attr}")

        try:
            attr_choice = int(input("\nEnter your choice: "))
            if attr_choice in range(1, len(attributes) + 1):
                attribute = attributes[attr_choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid attribute index.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the attribute.")

    while True:
        try:
            if attribute in ["age", "goal", "assist"]:
                new_value = int(input(f"Enter new {attribute}: "))
            elif attribute in ["no"]:
                while True:
                    new_value = int(input(f"Enter new {attribute}: "))
                    if new_value in pemain["no"]:
                        print("The number already exists. Please enter a different number.")
                    else:
                        break
            elif attribute == "rating":
                new_value = float(input(f"Enter new player's {attribute} (GK, DF, MF, FW): "))
            elif attribute == "position":
                while True:
                    new_value = input(f"Enter new {attribute}: ").upper()
                    if new_value not in pemain["position"]:
                        print("Invalid position. Please enter one of the following: GK, DF, MF, FW.")
                        continue
                    else:
                        break
            elif attribute == "club":
                new_value = input(f"Enter new {attribute}: ")
                pemain["country"][player_index] = input(f"Enter {new_value}'s country: ")
            elif attribute == "country":
                attribute = "club"
                print("\nIf you want to change the club's country, you should change the club's first.\n")
                new_value = input(f"Enter new {attribute}: ")
                pemain["country"][player_index] = input(f"Enter {new_value}'s country: ")
            else:
                new_value = input(f"Enter new {attribute}: ")
            break
        except ValueError:
            print(f"Invalid input. Please enter a valid {attribute}.")

    while True:
        confirm = input(f"\nAre you sure you want to change {attribute} from {pemain[attribute][player_index]} to {new_value}? (yes/no): ").strip().lower()
        if confirm == "yes":
            pemain[attribute][player_index] = new_value # Changing value
            print("\nPlayer data updated successfully.\n")
            break
        elif confirm == "no":
            print("\nUpdate cancelled.\n")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Menu 5 - Sub 1
def rank_players():
    while True:
        try:
            print("\nRank Players By:")
            print("1. Goals")
            print("2. Assists")
            print("3. Ratings")
            print("4. Back to Main Menu")
            choice = int(input("\nEnter your choice: "))

            if choice in range(1, 4):
                if choice == 1:
                    attribute = "goal"
                    attribute_name = "Goals"
                elif choice == 2:
                    attribute = "assist"
                    attribute_name = "Assists"
                elif choice == 3:
                    attribute = "rating"
                    attribute_name = "Ratings"

                sorted_players = [(pemain["name"][i], pemain[attribute][i], pemain["no"][i], pemain["position"][i])
                                  for i in range(len(pemain["name"]))]
                for i in range(len(sorted_players)):
                    for j in range(0, len(sorted_players) - i - 1):
                        if sorted_players[j][1] < sorted_players[j + 1][1]:
                            sorted_players[j], sorted_players[j + 1] = sorted_players[j + 1], sorted_players[j]

                print(f"\nPlayers Ranked by {attribute_name}\n")
                print(f"{'Rank':<5} {'No.':<5} {'Name':<20} {'Pos.':<5} {attribute_name:<10}")
                print("-" * 50)
                for rank, (name, value, no, pos) in enumerate(sorted_players, start=1):
                    print(f"{rank:<5} {no:<5} {name:<20} {pos:<5} {value:<10}")
                print()
                continue
            elif choice == 4:
                print()
                break
            else:
                raise IndexError
        except IndexError:
            print("\nPlease input the right index to continue.")
            continue
        except ValueError:
            print("\nPlease input the right index to continue.")
            continue

# Menu 6 - Sub 1
def compare_players():
    print("\nPlayers List:")
    print(f"{'No.':<5} {'Name':<20} {'Pos.':<5}")
    print("-" * 30)
    position_order = {'GK': 0, 'DF': 1, 'MF': 2, 'FW': 3}
    player_details = list(zip(pemain["no"], pemain["name"], pemain["position"]))
    sorted_players = sorted(player_details, key=lambda x: position_order.get(x[2]))
    for player in sorted_players:
        player_no, player_name, player_position = player
        print(f"{player_no:<5} {player_name:<20} {player_position:<5}")

    while True:
        print("\nCompare Players:")
        player1_no = int(input("Enter number of first player: "))
        player2_no = int(input("Enter number of second player: "))

        if player1_no in pemain["no"] and player2_no in pemain["no"]:
            if player1_no == player2_no:
                print("\nCannot compare the same player. Please enter different player numbers.")
                continue

            player1_index = pemain["no"].index(player1_no)
            player2_index = pemain["no"].index(player2_no)

            if pemain['position'][player1_index] != pemain['position'][player2_index]:
                print("\nPlayers must have the same position to be compared. Please try again.")
                continue

            print("\nPlayer 1:")
            print(f"Name: {pemain['name'][player1_index]}")
            print(f"Position: {pemain['position'][player1_index]}")
            print(f"Club: {pemain['club'][player1_index]}")
            print(f"Country: {pemain['country'][player1_index]}")
            print(f"Goals: {pemain['goal'][player1_index]}")
            print(f"Assists: {pemain['assist'][player1_index]}")
            print(f"Rating: {pemain['rating'][player1_index]}")

            print("\nPlayer 2:")
            print(f"Name: {pemain['name'][player2_index]}")
            print(f"Position: {pemain['position'][player2_index]}")
            print(f"Club: {pemain['club'][player2_index]}")
            print(f"Country: {pemain['country'][player2_index]}")
            print(f"Goals: {pemain['goal'][player2_index]}")
            print(f"Assists: {pemain['assist'][player2_index]}")
            print(f"Rating: {pemain['rating'][player2_index]}")

            input("\nPress Enter to continue...")
            break  # Exit the loop and return to main menu
        else:
            print("\nPlayer number not found. Please try again.")

# Menu 6 - Sub 2
def players_by_position():
    while True:
        positions = []
        for i in range(len(pemain["position"])):
            position = pemain["position"][i]
            if position not in positions:
                positions.append(position)
        print("\nSelect Position to Compare:")
        for i, pos in enumerate(positions):
            print(f"{i + 1}. {pos}")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice in range(1, 5):
                selected_position = positions[choice - 1]
                print(f"\nPlayers in Position: {selected_position}\n")
                print(f"{'No.':<5} {'Name':<20} {'Age':<5} {'Club':<20} {'Country':<15} {'Goal(s)':<10} {'Assist(s)':<10} {'Rating':<10}")
                print("-" * 100)
                for i in range(len(pemain["name"])):
                    if pemain["position"][i] == selected_position:
                        print(f"{pemain['no'][i]:<5} {pemain['name'][i]:<20} {pemain['age'][i]:<5} {pemain['club'][i]:<20} {pemain['country'][i]:<15} {pemain['goal'][i]:<10} {pemain['assist'][i]:<10} {pemain['rating'][i]:<10}")
                break
            else:
                raise IndexError
        except IndexError:
            print("\nPlease input the right index to continue.")
            continue
        except ValueError:
            print("\nPlease input the right index to continue.")
            continue

# Menu 7 - Sub 1
def suggest_formation():
    while True:
        print("\nChoose Formation:")
        print("1. 4-4-2")
        print("2. 4-3-3")
        print("3. 3-5-2")
        print("4. Custom")
        print("5. Back to Main Menu")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            formation = [("GK", 1), ("DF", 4), ("MF", 4), ("FW", 2)]
        elif choice == 2:
            formation = [("GK", 1), ("DF", 4), ("MF", 3), ("FW", 3)]
        elif choice == 3:
            formation = [("GK", 1), ("DF", 3), ("MF", 5), ("FW", 2)]
        elif choice == 4:
            formation = []
            while True:
                total_players = 0
                for position in ["DF", "MF", "FW"]:
                    try:
                        num = int(input(f"Enter number of {position}: "))
                    except ValueError:
                        print("\nInvalid input. Please enter a valid number.\n")
                        formation.clear()
                        break
                    if num < 0:
                        print("\nNumber of players cannot be negative. Try again.\n")
                        formation.clear()
                        break
                    formation.append((position, num))
                    total_players += num
                else:
                    formation.insert(0, ("GK", 1))  # Automatically set GK to 1
                    if total_players == 10:
                        break
                    else:
                        print("\nTotal number of players must be 10 (excluding GK). Try again.\n")
                        formation.clear()
        elif choice == 5:
            print()
            break  # Exit the while loop to return to main menu
        else:
            print("\nInvalid choice. Please try again.")
            continue

        if formation is not None:
            team = []
            for pos, num in formation:
                players = [i for i in range(len(pemain["position"])) if pemain["position"][i] == pos]
                players = sorted(players, key=lambda x: pemain["rating"][x], reverse=True)[:num]
                if len(players) < num:
                    print(f"\nNot enough players for position {pos}. Please try again.")
                    break  # Exit the loop if not enough players
                team.extend(players)

            if len(team) == 11:
                print_team(team)
                print()
                break
            else:
                print("\nFormation not completed due to insufficient players. Please try again.")

def print_team(team):
    print("\nSuggested Team Formation\n")
    print(f"{'No.':<5} {'Name':<20} {'Pos.':<5} {'Age':<5} {'Club':<20} {'Country':<15} {'Goal(s)':<10} {'Assist(s)':<10} {'Rating':<10}")
    print("-" * 105)
    for i in team:
        print(f"{pemain['no'][i]:<5} {pemain['name'][i]:<20} {pemain['position'][i]:<5} {pemain['age'][i]:<5} {pemain['club'][i]:<20} {pemain['country'][i]:<15} {pemain['goal'][i]:<10} {pemain['assist'][i]:<10} {pemain['rating'][i]:<10}")

# Program Start
while True:
    try:
        main_menu()
        menu = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nInvalid choice. Please enter a number between 1 and 8.\n")
        continue

    if menu == 1:
        while True:
            try:
                print("\nShow Statistics:")
                print("1. Players' Statistics")
                print("2. Average Goals by Positions")
                print("3. Average Assists by Positions")
                print("4. Average Age by Positions")
                print("5. Top Rated Players by Positions")
                print("6. Goal Contributions")
                print("7. Back to Main Menu")
                menu1 = int(input("\nEnter your choice: "))
                if menu1 == 1:
                    players_table()
                    continue
                elif menu1 == 2:
                    print()
                    average_goals_by_position()
                    continue
                elif menu1 == 3:
                    print()
                    average_assists_by_position()
                    continue
                elif menu1 == 4:
                    print()
                    average_age_by_position()
                    continue
                elif menu1 == 5:
                    print()
                    top_rated_players_by_position()
                    continue
                elif menu1 == 6:
                    print()
                    goal_contribution()
                    continue
                elif menu1 == 7:
                    print()
                    break
                else:
                    print("\nPlease input the right index to continue.")
                    continue
            except ValueError:
                print("\nPlease input the right index to continue.")
                continue

    elif menu == 2:
        while True:
            try:
                print("\nAdd New Player(s):")
                print("1. Add New Player")
                print("2. Back to Main Menu")
                menu2 = int(input("\nEnter your choice: "))
                if menu2 == 1:
                    adding_players()
                    print()
                    break
                elif menu2 == 2:
                    print()
                    break
                else:
                    print("\nPlease input the right index to continue.")
                    continue
            except ValueError:
                print("\nPlease input the right index to continue.")
                continue

    elif menu == 3:
        while True:
            try:
                print("\nRemove Player(s):")
                print("1. Remove Player's Data")
                print("2. Back to Main Menu")
                menu3 = int(input("\nEnter your choice: "))
                if menu3 == 1:
                    print("\nPlayers List:")
                    print(f"{'No.':<5} {'Name':<20} {'Pos.'}")
                    print("-" * 30)
                    for i in range(len(pemain["no"])):
                        print(f"{pemain['no'][i]:<5} {pemain['name'][i]:<20} {pemain['position'][i]:<5}")
                    remove_players()
                    print()
                    break
                elif menu3 == 2:
                    print()
                    break
                else:
                    print("\nPlease input the right index to continue.")
                    continue
            except ValueError:
                print("\nPlease input the right index to continue.")
                continue

    elif menu == 4:
        while True:
            try:
                print("\nUpdate Data:")
                print("1. Update Player's Data")
                print("2. Back to Main Menu")
                menu4 = int(input("\nEnter your choice: "))
                if menu4 == 1:
                    while True:
                        update_data()
                        another = input("Do you want to change another data? (yes/no): ").strip().lower()
                        if another != "yes":
                            break
                    players_table()
                    print()
                    break
                if menu4 == 2:
                    print()
                    break
                else:
                    print("\nPlease input the right index to continue.")
                    continue
            except ValueError:
                print("\nPlease input the right index to continue.")
                continue

    elif menu == 5:
        rank_players()

    elif menu == 6:
        while True:
            try:
                print("\nCompare Players:")
                print("1. Compare Two Players")
                print("2. Compare Players Based on Positions")
                print("3. Back to Main Menu")
                menu6 = int(input("\nEnter your choice: "))
                if menu6 == 1:
                    compare_players()
                    continue
                elif menu6 == 2:
                    players_by_position()
                    continue
                elif menu6 == 3:
                    print()
                    break
                else:
                    print("\nPlease input the right index to continue.")
                    continue
            except ValueError:
                print("\nPlease input the right index to continue.")
                continue

    elif menu == 7:
        suggest_formation()

    elif menu == 8:
        print("\nEnd of Program.\n")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 8.\n")
        continue