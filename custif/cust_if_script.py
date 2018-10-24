#!/usr/bin/env python3
points = 'Your grade is : '
print('How many points did you get?')
points1 = float(input())
if points1 >= 90:
    points = points + 'A'
elif points1 >= 80:
    points = points + 'B'
elif points1 >= 60:
    points = points + 'C'
else:
    points = points + 'Go find a book.'
print(points)
