#!/usr/bin/env python3.7
# Printing odd numbers with break

count = 1

while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
    