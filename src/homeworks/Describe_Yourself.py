# Name: Raven Daigle
# Course: ITSE-1302
# Date: April 15, 2023
# Description: Program to open a description of the user in a simple web page

# import modules for opening html in browser
import webbrowser
import os

# Get info about the user
def get_user_info():
    # Ask user for name
    name = input("Enter your name: ")
    # Ask user for a description of themselves
    description = input("Describe yourself in a sentence: ")
    return name, description

# Create html file from user input
def create_html(name, description):
    description_file = open('about_me.html', 'w')
    description_file.write(("<html>\n" +
            "\t<head>\n" +
            "\t</head>\n" +
            "\t<body>\n" +
            "\t\t<center>\n" +
            "\t\t\t<h1>{name}</h1>\n" +
            "\t\t\t<h2>\n" +
            "\t\t\t\t{description}\n" +
            "\t\t\t</h2>\n" +
            "\t\t</center>\n" +
            "\t</body>\n" +
            "</html>").format(name=name, description=description))
    description_file.close()

# Call main, open html file in browser
def main():
    name, description = get_user_info()
    create_html(name, description)
    webbrowser.open('file://' + os.path.realpath('about_me.html'))

main()
