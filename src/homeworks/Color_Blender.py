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
print(result_colors["purple"])
# Intro statement to user
print("Welcome to Color Blender!")

# Instructions to user
print("Discover the resulting color from the combination of two different primary colors: \n"
        "\tred, blue, or yellow")

# Color variable assignment
color_1 = "unknown"
color_2 = color_1

# Loop until valid input
valid_response = False
while not valid_response:
    # First primary color input, converts string to lowercase
    color_1 = input("Please input your first primary color: ").lower()

    # First primary color input error check
    if color_1 in VALID_COLORS:
        valid_response = True
    else:
        print("! Error !: The first color you entered is invalid.")

# Loop until valid input
valid_response = False
while not valid_response:
    # Second primary color input, converts string to lowercase
    color_2 = input("Please input your second primary color: ").lower()

    # Second primary color input error check
    if color_2 == color_1:
        print("! Error !: The color you entered is the same. Please select a different color.")
    elif color_2 in VALID_COLORS:
        valid_response = True
    else:
        print("! Error !: The second color you entered is invalid.")

if color_1 and color_2 in purple:
    print("The blended color is purple!")
elif color_1 and color_2 in orange:
    print("The blended color is orange!")
elif color_1 and color_2 in green:
    print("The blended color is green!")

