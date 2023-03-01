# Name: Raven Daigle
# Course: ITSE 1302
# March 01, 2023
# Color blender program that displays a resulting mixed color from input of two different primary colors

# List of valid colors as constant variable 
VALID_COLORS = ["red", "blue", "yellow"]

# Dictionary of blended colors
result_colors = {
    "purple": {"red", "blue"},
    "orange": {"red", "yellow"},
    "green": {"blue", "yellow"}
}

# Intro statement to user
print("Welcome to Color Blender!")
print("Find out the resulting secondary color by blending two primary colors.")

# Color variable assignment
color_1 = "unknown"
color_2 = color_1

# Loop until valid input
valid_response = False
while not valid_response:
    # First primary color input, converts string to lowercase
    color_1 = input(f"Please input your first primary color. Options: {VALID_COLORS}: ").lower().strip()

    # First primary color input error check
    if color_1 in VALID_COLORS:
        valid_response = True
    else:
        print("! Error !: The first color you entered is invalid.")

# Remove the color first picked from the valid options
VALID_COLORS.remove(color_1)

# Loop until valid input
valid_response = False
while not valid_response:
    # Second primary color input, converts string to lowercase
    color_2 = input(f"Please input your second primary color. Options: {VALID_COLORS}: ").lower().strip()

    # Second primary color input error check
    if color_2 == color_1:
        print("! Error !: The color you entered is the same. Please select a different color.")
    elif color_2 in VALID_COLORS:
        valid_response = True
    else:
        print("! Error !: The second color you entered is invalid.")

# Print blended colors from dictionary 
if color_1 in result_colors["purple"] and color_2 in result_colors["purple"]:
    print("The blended color is purple!")
elif color_1 in result_colors["orange"] and color_2 in result_colors["orange"]:
    print("The blended color is orange!")
elif color_1 in result_colors["green"] and color_2 in result_colors["green"]:
    print("The blended color is green!")

