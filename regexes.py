"""
regexes - regular expressions 
to validate that data is correct, that patters same, or clean up some data
validate.py
re - library fo regular expressions
"""
#LVL1
email = input("what's the email?")

if "@" in email and "." in email:
    print('Valid')
else:
    print('Broke')
#LVL2
email = input("what's the email?")

username, domain = email.split("@")

if username and "." in domain:
    print('Valid')
else:
    print('Broke')
#LVL3
email = input("what's the email?")

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print('Valid')
else:
    print('Broke')