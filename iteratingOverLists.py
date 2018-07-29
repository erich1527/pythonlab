#!/usr/bin/env python3.7
# See previous lab (workingWithIf)

users = [
    { 'admin': True, 'active': True, 'name': 'Eric' },
    { 'admin': True, 'active': False, 'name': 'Jim' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' }
]

line = 1

for user in users:
    prefix  = f"{line} "

    if user['admin'] and user['active']:
        prefix += "Active - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "Active "

print(prefix + user['name'])
line += 1