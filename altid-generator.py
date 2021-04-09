import os

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

def print_names(gender, last_names):
    print('printing names')
    return 'n/a'

another_name, male_names, female_names, last_names = 'y', get_names('first-names-male'), get_names('first-names-female') , get_names('last-names')

while another_name.lower() == 'y':
    gender = 'x'
    while gender.lower() != 'm' or gender.lower !='f':
        gender = input('Male or female name? (m/f): ')
        if gender.lower() == 'm':
            print('getting male names')
        elif gender.lower() == 'f':
            print('getting female names')
    
    another_name = input('Generate another name? (y/n): ')

print()
print('GOODBYE!')
print()
