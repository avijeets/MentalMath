#!/usr/bin/python
from random import randint

print 'Correct responses receive 20 points, whereas wrong responses receive negative 10 points.  Type q to quit at any time.'
score = 0
while True:
    a = randint(10, 200) #increase or decrease for difficulty of questions 
    b = randint(10, 200) #increase or decrease for difficulty of questions
    yourAnswer = raw_input('What is ' + str(a) + ' plus ' + str(b) + '?\n> ')
    if yourAnswer == 'q':
        break
    elif yourAnswer == str(a + b):
        score += 20
        print 'Correct!  Total score: ' + str(score) + '\n'
    else:
        score -= 10
        print 'Wrong! The correct answer was ' + str(a + b) + '. Total score: ' + str(score) + '\n'

print 'Your score is ' + str(score) + '. Good luck next time!'