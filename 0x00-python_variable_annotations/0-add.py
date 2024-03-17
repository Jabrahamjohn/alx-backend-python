#!/usr/bin/env python3
add = __import__('0-add').add

print(add(3.5,2.22) == 3.5 + 2.22)
print(add.__annotations__)