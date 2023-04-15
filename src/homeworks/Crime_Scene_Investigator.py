# Name: Raven Daigle
# Course: ITSE 1302
# Date: April 05, 2023
# Description: Crime scene investigation tool

# Create forensics class
class Forensics:
    def __init__(self):
        # Give default values of 0 to all variables
        self.medulla = 0
        self.hair = 0
        self.femur = 0
        self.gender = 0

    # Getter functions
    def get_medulla_diameter(self):
        return self.medulla

    def get_hair_diameter(self):
        return self.hair

    def get_femur_height(self):
        return self.femur

    def get_gender(self):
        return self.gender

    # Setter functions
    def set_medulla_diameter(self, value):
        self.medulla = value

    def set_hair_diameter(self, value):
        self.hair = value

    def set_femur_height(self, value):
        self.femur = value

    def set_gender(self, value):
        self.gender = value

# Get the hair type based on medulla diameter and hair diameter
def getHairType(medulla_diameter, hair_diameter):
    ratio = medulla_diameter / hair_diameter
    if ratio >= 0.5:
        # It is an animal hair
        return 0
    else:
        # It is a human hair
        return 1

# Get the height based on the femur height and gender
def getHeight(femur_height, gender):
    if gender == 0:
        # Calculate for a male
        return 69.089 + (2.238 * femur_height)
    else:
        # Calculate for a female
        return 61.412 + (2.317 * femur_height)

# Get input from the user. Keep trying until valid input
def get_float_input(text, is_gender):
    while True:
        try:
            # Get the input, try to convert to a float
            input_value = float(input(text))
            if input_value < 0.0:
                print("Must be greater than or equal to 0.")
                continue
            elif is_gender and input_value != 0 and input_value != 1:
                print("You must input 0 or 1 for male or female.")
                continue
            return input_value
        except:
            print("Bad input, try again.")


print("Welcome inspector,")
# Create the object to hold the data we collect
data = Forensics()

print("\nHair Analysis:")
# Get the medulla value
input_value = get_float_input("Please enter the medulla width in mm: ", False)
data.set_medulla_diameter(input_value)

# Get the hair diameter value
input_value = get_float_input("Please enter the entire hair width in mm: ", False)
data.set_hair_diameter(input_value)

print("\nHeight Analysis:")
# Get the gender 
input_value = get_float_input("Please enter the gender (0=male, 1=female): ", True)
data.set_gender(input_value)

# Get the femur length
input_value = get_float_input("Please enter the femur length in cm: ", False)
data.set_femur_height(input_value)

# Calculate if it is a human or animal
specimen = "human"
if getHairType(data.get_medulla_diameter(), data.get_hair_diameter()) == 0:
    specimen = "animal"
print(f"\nThe specimen is {specimen}.")

# Calculate the height of the specimen
height = getHeight(data.get_femur_height(), data.get_gender())
print(f"The height is estimated to be {height:0.3f} cm.")

