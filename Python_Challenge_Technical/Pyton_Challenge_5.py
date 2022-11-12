""" Write a Python Program that checks if a string is a Palindrome. Optionally write a unit test to check the
Program's correctness. """


def is_a_palindrome(string):
    if string == string[::-1]:
        print("Is Palindrome")
    else:
        print("Not a Palindrome")


is_a_palindrome("meme")
is_a_palindrome("madam")
is_a_palindrome("raddar")
is_a_palindrome("Deified")
is_a_palindrome("2/22/22")
