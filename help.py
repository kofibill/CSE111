# First ask the user for the radius of the circle
# Calculate the diameter
# Calculate the circumference
# calculate the area of that circle

import math # importing the built in math module

radius=int(input('What is the radius of the circle? ')) # asking the user for the radius of the circle
diameter= 2 * radius #calculating the diameter
circumference= 2 * math.pi * radius # calculating the circumference
area =math.pi * radius **2 # calculating the area of the circle

# printing or displaying the results using the format strings.
print(f'A circle with a radius of {radius} units will have a diameter of {diameter} units')
print(f'a circumference of {circumference} units and an area of {area} square units.')