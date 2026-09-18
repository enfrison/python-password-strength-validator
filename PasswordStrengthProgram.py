# Erika Frison
# CIS 125 - 70
#
# This project determines if a password is strong.

import re

def passwordStrength(password):

    character = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (re.search('[a-z]',password)) is None:
        print('Your password is not a mixed case.  Please choose a password with mixed case.')
    if (re.search('[A-Z]', password)) is None:
        print('Your password is not a mixed case.  Please choose a password with mixed case.')
    if (character.search(password) == None):
        print('You do not have a valid special character in your password. Please add at least one special character.')
    if len(password) < 8:
        print('Your password length is too short.  Please choose a password that is at least 8 characters long.')
    else:
        print('Thank you.  Your password is valid.')


def main():
    password = str(input('Please enter a password: '))
    passwordStrength(password)


main()
