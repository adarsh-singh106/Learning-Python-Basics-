import random
import os
import sys

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_message(message, message_type='info'):
    """Prints a message to the console with some styling."""
    if message_type == 'error':
        print(f"\n❌ ERROR: {message}\n")
    elif message_type == 'success':
        print(f"\n✅ SUCCESS: {message}\n")
    else: # info
        print(f"\nℹ️  INFO: {message}\n")

def get_player_choice(player_name):
    
    """
    Prompts a player for their choice and validates it.
    Returns the validated choice ('s', 'w', or 'g').
    """
    while True:
        choice = input(f"{player_name}, enter your choice (s for Snake, w for Water, g for Gun): ").lower().strip()
        if choice in ['s', 'w', 'g']:
            return choice
        else:
            display_message("Invalid choice! Please enter 's', 'w', or 'g'.", 'error')

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['s', 'w', 'g'])

def determine_winner(player1_choice, player2_choice, player1_name, player2_name):
    """
    Determines the winner of a round based on choices.
    Returns (winner_name, result_message).
    """
    choice_names = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    winning_rules = {
        's': 'w', # Snake beats Water
        'w': 'g', # Water beats Gun
        'g': 's'  # Gun beats Snake
    }

    p1_choice_name = choice_names[player1_choice]
    p2_choice_name = choice_names[player2_choice]

    if player1_choice == player2_choice:
        return None, f"Both chose {p1_choice_name}. It's a Draw!"
    elif winning_rules[player1_choice] == player2_choice:
        return player1_name, f"{player1_name} chose {p1_choice_name} and {player2_name} chose {p2_choice_name}. {player1_name} wins!"
    else:
        return player2_name, f"{player1_name} chose {p1_choice_name} and {player2_name} chose {p2_choice_name}. {player2_name} wins!"

def display_scoreboard(player1_name, player1_score, player2_name, player2_score):
    """Displays the current scores."""
    print("\n--- SCOREBOARD ---")
    print(f"{player1_name}: {player1_score}")
    print(f"{player2_name}: {player2_score}")
    print("------------------\n")

def main_game_loop():
    """Main function to run the Snake, Water, Gun game."""
    while True:
        clear_screen()
        print("--- Welcome to Snake, Water, Gun! ---")

        # Player selection
        while True:
            try:
                num_players_input = input("How many players? (1 or 2): ").strip()
                num_players = int(num_players_input)
                if num_players in [1, 2]:
                    break
                else:
                    display_message("Please enter either 1 or 2.", 'error')
            except ValueError:
                display_message("Invalid input. Please enter a number (1 or 2).", 'error')

        player1_name = ""
        player2_name = ""
        player1_score = 0
        player2_score = 0

        if num_players == 1:
            player1_name = input("Enter your name: ").strip() or "Player 1"
            player2_name = "Computer"
            display_message(f"You will be playing against the {player2_name}!")
        else:
            player1_name = input("Enter Player 1's name: ").strip() or "Player 1"
            player2_name = input("Enter Player 2's name: ").strip() or "Player 2"
            display_message(f"{player1_name} vs. {player2_name}!")

        current_player = 1 # 1 for Player 1, 2 for Player 2

        # Game rounds loop
        while True:
            clear_screen()
            display_scoreboard(player1_name, player1_score, player2_name, player2_score)

            player1_choice = ''
            player2_choice = ''

            if num_players == 1:
                player1_choice = get_player_choice(player1_name)
                player2_choice = get_computer_choice()
                print(f"{player1_name} chose: {player1_choice.upper()}")
                print(f"Computer chose: {player2_choice.upper()}")
            else:
                # Player 1's turn
                player1_choice = get_player_choice(player1_name)
                clear_screen() # Clear screen after first player's choice for secrecy
                display_message(f"{player1_name} has made their choice. Now it's {player2_name}'s turn.", 'info')

                # Player 2's turn
                player2_choice = get_player_choice(player2_name)
                print(f"{player1_name} chose: {player1_choice.upper()}")
                print(f"{player2_name} chose: {player2_choice.upper()}")

            winner, result_message = determine_winner(player1_choice, player2_choice, player1_name, player2_name)
            print(f"\n{result_message}")

            if winner == player1_name:
                player1_score += 1
            elif winner == player2_name:
                player2_score += 1

            display_scoreboard(player1_name, player1_score, player2_name, player2_score)

            # Post-round options
            while True:
                print("Options:")
                print("  [C]ontinue (Replay)")
                print("  [R]estart (New Game)")
                print("  [E]xit")
                action = input("What would you like to do? ").lower().strip()

                if action == 'c':
                    break # Break from this inner loop to continue the game loop
                elif action == 'r':
                    return # Exit the main_game_loop to restart the whole game
                elif action == 'e':
                    print("\nThanks for playing Snake, Water, Gun! Goodbye!")
                    sys.exit() # Exit the program
                else:
                    display_message("Invalid option. Please choose 'c', 'r', or 'e'.", 'error')

if __name__ == "__main__":
    main_game_loop()
