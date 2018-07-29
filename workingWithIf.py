#!/usr/bin/env python3.7
# Create a script with a single variable contianing a dict

user = { 'admin': True, 'active': False, 'name': 'Eric' }
prefix = ""

if user['admin'] and user['active']:
    prefix = "Active - (ADMIN) "
elif user['admin']:
    prefix = "(ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])