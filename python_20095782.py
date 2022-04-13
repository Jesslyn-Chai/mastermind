# A Master Mind Computer Program

# Importing random module
import random

# Declaration of preset colours
colors_set = ["R", "G", "B", "Y", "P", "W"]

# Computation - defining function
# Generating random combination of 4 colours
def randomize_colors():
    random_colors = random.choices(colors_set, k=4)
    return random_colors

# Data validation
def validate_color_input(guess_colors, colors_set):
    if len(guess_colors) != 4:
        print("\nPlease enter 4 colours!\n")
        return False
    for i in range(4):
        if guess_colors[i] not in colors_set:
            print("\n" + guess_colors[i] + " is not in the list above!\n")
            return False
    return True

# Compare colours and provide feedback
def compare_colors(guess_colors, random_colors):
    # cccp - correct_colour_correct_place
    cccp = 0
    # ccwp - correct_colour_wrong_place
    ccwp = 0

    temp_colors = random_colors.copy()
    for i in range(4):
        if guess_colors[i] == temp_colors[i]:
            temp_colors[i] = "X"
            guess_colors = guess_colors[:i] + "X" + guess_colors[i+1:]
            cccp += 1
        
    for i in range(4):
        for j in range(4):
            if guess_colors[i] != "X" and guess_colors[i] == temp_colors[j]:
                temp_colors[j] = "X"
                guess_colors = guess_colors[:i] + "X" + guess_colors[i+1:]
                ccwp += 1

    # Print feedback
    if cccp != 4:
        print("\nCorrect colour in the correct place: " + str(cccp))
        print("Correct colour but in the wrong place: " + str(ccwp) + "\n")
        return False
    else:
        return True

# Start game
def start_game():
    # Heading - Introduction
    print("Welcome to Master Mind Computer Program!\n")
    print("Game Rules: \nThe computer has selected a secret combination of 4 colors and you can continue guessing that combination until you get it correctly.")
    print("\nYour guess should be entered in \"RGBG\" without the double quote.\n[R] Red\n[G] Green\n[B] Blue\n[Y] Yellow\n[P] Pink\n[W] White\n")

    is_continue = True
    while is_continue:
        is_correct = False
        attempt = 0
        colors = randomize_colors()
        while not is_correct:
            #print(colors)
            guess_colors = input("Enter your guess:\n").upper()

            is_valid_input = validate_color_input(guess_colors, colors_set)
            if not is_valid_input:
                continue

            is_correct = compare_colors(guess_colors, colors)
            attempt += 1

            # Print attempts & ask user to play again
            if is_correct:
                print("\nWell done! You took " + str(attempt) + " attempt(s)!")
                play_again = input("\nDo you want to play again? [Y/N}:\n").upper()
                if play_again != "Y":
                    print("\nThanks for playing!")
                    is_continue = False
            else:
                print("Try again!\n")

# Calling function
start_game()

# End of program
