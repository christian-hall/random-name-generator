import os
import random

print('WELCOME TO THE ALTERNATE ID GENERATOR')
print('GENERATE A NEW NAME')
print()

def get_names(filename):
    names, filepath = [], os.path.dirname(os.path.abspath(__file__)) + '/' + filename + '.txt'
    print(filepath)
    file = open(filepath, 'r')
    for name in file:
        names.append(name.rstrip('\r\n'))
    file.close()
    return names

def print_names(gender_names, last_names):
    first_name, last_name = gender_names[random.randint(0, len(gender_names) - 1)], last_names[random.randint(0, len(last_names) - 1)]
    print('Your name: ' + first_name.upper() + ' ' + last_name.upper())
    print()

another_name, male_names, female_names, last_names = 'y', get_names('first-names-male'), get_names('first-names-female') , get_names('last-names')

while another_name.lower() == 'y':
    while another_name.lower() == 'y':
        gender = input('Male or female name? (m/f): ')
        if gender.lower() == 'm':
            print_names(male_names, last_names)
            break
        elif gender.lower() == 'f':
            print_names(female_names, last_names)
            break
        else:
            print('invalid selection, please try again!')
    
    another_name = input('Generate another name? (y/n): ')

print()
print('GOODBYE!')
print()
