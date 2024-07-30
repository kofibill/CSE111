import math

print()
from datetime import datetime  

date = datetime.now(tz = None)
print(date)

day_of_week = date.weekday()
print()
filename='volume.txt'
file=open(filename , 'a')

width=float(input('Enter the width of the tire in mm: '))
aspect_ratio=float(input('Enter the aspect ratio of the tire: '))
diameter=float(input('Enter the diameter of the wheel in inches: '))

volume=math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
volume=round(volume, 2)
print(f'The volume in liters is {volume}')

file.write(str(round(volume , 2)) + '\n')
user=input(' Do you wish to buy the tire? (YES/NO)').lower()
if user=='yes'.lower():
    email=input('Please enter your email address: ')
    file.write(f'email address:{email}')
    print('Thanks for entering  your email adsress')
elif user=='no'.lower():
    print('Thanks for using the program...') 