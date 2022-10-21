# Lesson 20 Task
#
# Create a class called Human
#
# Add an attribute leg_count with the value of 4
#
# Add a method called get_gender() that returns "Unknown" in the Human class
#
# Create another class called Man that extends Human
#
#
#
# Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method in
# each object instance

class Human:
    leg_count = 2
    sex = "unknown"

    def get_gender(self):
        print("\nHuman {", self.leg_count, ",", self.sex + "}")


class Man(Human):

    legs = "none"

    def __init__(self, leg_count, sex):
        self.leg_count = leg_count
        self.sex = sex


man1 = Man("Female", "Binary")
man1.get_gender()
