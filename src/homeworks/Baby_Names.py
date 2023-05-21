# Name: Raven Daigle
# Course: ITSE-1302
# Date: May 05, 2023
# Description: Program that searches for most popular boy and girl names from file

# Get input from the user
def user_input(question):
    while True:
        try:
            # Get the input from the user. Remove extra white space like \n
            #   and convert to lower to check against list
            input_value = input(question).strip().lower()
            if input_value == "":
                print("Empty names are not allowed. Please try again.")
                continue

            # Split the string into a list of strings
            return input_value.split()
        except:
            print("Bad input, try again.")

# Create main function
def main():

    # Open and read files of names, make lowercase for checking
    girl_contents = ""
    with open("GirlNames.txt", 'r') as file:
        girl_contents = file.read().lower()

    boy_contents = ""
    with open("BoyNames.txt", 'r') as file:
        boy_contents = file.read().lower()
    
    # Create separate lists from files
    girl_list = girl_contents.split()
    boy_list = boy_contents.split()

    # Directions to user
    print("Find out if a name is among the Top 200 boys or girls names.")
    names = user_input("Enter a boy's name, a girl's name, or both: ")

    # Check all names user put
    for name in names:
        name_found = False
        # Display if name was among popular names
        if name in girl_list:
            name_found = True
            print(f"{name} is a popular girl's name!")
        if name in boy_list:
            name_found = True
            print(f"{name} is a popular boy's name!")

        # Name was not found
        if not name_found:
            print(f"{name} is not a popular name.")

# Call main function
main()
