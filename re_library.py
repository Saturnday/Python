"""
- ipmort the library
- prompt with input and save to variable email
- use if else to find if the '@: in the email use the searching function of the library
- 


import re

email = input("prompt the email  ")

if re.search("@", email): #anki syntax
    print('valid')
else:
    print('invalid')


- ipmort the library
- prompt with input and save to variable email
- use if else to find if the '@: in the email use the searching function of the library
- use the r

import re

email = input("prmot the email  ")

if re.search(r'.+@.+\.edu', email):
    print('valid')
else:
    print('invalid')

#using the \w

import re

email = input("prmot the email  ")

if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email,re.IGNORECASE): #forgot to include the UPPERCASE flag
    print('valid')
else:
    print('invalid')

"""
import re

email = input("prmot the email  ").strip()

if re.search(r'^\w+@(\w+(\.+|\.edu))$', email,re.IGNORECASE):
    print('valid')
else:
    print('invalid')