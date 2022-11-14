# Lesson 25 Task
#
# Create a class called Utilities
#
# Create a static method called print_name which accepts a parameter, and prints out the parameter.
#
# Invoke the static method print_name()
#
#
#
# You can use any of the two methods to create your static methods.


class Utilities:
    def print_name(name):
        return name


Utilities.print_name = staticmethod(Utilities.print_name)

print("Name:", Utilities.print_name("Nezz"))

