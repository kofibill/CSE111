import math
from datetime import datetime
filename='volume.txt'
file=open(filename , 'a')

for i in range(0, 10):
    width=int(input('Please enter the width of the tie in mm: '))
    aspect_ratio=int(input('Please enter the aspect ratio of the tire: '))
    diameter=int(input('Please enter the diameter of the wheel in liters'))
math.pi
today=datetime.now().strftime('%y-%m-%d')

volume=math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
print(f'The approximate volume of the tire is {round(volume,2)} liters ')

