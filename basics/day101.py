# Converts 32 degrees to radian (HINT: math.pi!).
# Asks the user for a radius then prints out the surface area and volume of a sphere.
# Tells the user what time of day it is, in a nice format.
# Splits a sentence into its words
# Joins a list of words into a sentence. Find TWO ways to do this!

# 1
# degrees -> fariheit = (0 degrees x 1.8) + 32 = 32 Farinheit
# degress -> radian =
from datetime import datetime
import math
from time import time
from cv2 import split

from numpy import array, mat

degree  = 32 
# Using the math.radians  approach
print("Using the math.radians -> approach")
print ("32 Degrees to Radians: ",math.radians(degree), "\n")

#using the math.pi approach

degree_In_Radians = degree * math.pi/180

print("Using the math.pi -> approach")
print("32 Dgrees to Radians: ", degree_In_Radians)

#2
# print("Program to calculate surface area and volume of a square")
# radius = int(input("Enter radius:"))

# # area of a sphere -> 4pir**2
# area = 4 * math.pi * math.pow(radius,2)
# volume = 4/3 * math.pi * math.pow(radius,3)

# print("Surface Area of Sphere: ", area, "\n")
# print("Volume of Sphere: ", volume)

#3 
todays_date = datetime.today()
time_of_day = datetime.today().strftime("%H:%M %a")
# string format in time -> "%H:%M %p" -> prints time in Am or PM
# string format in time -> "%H:%M %a" -> prints time and appends the current day

print("Today's date is: ", todays_date.strftime("%B %d %Y"))
print("Today's time is : ", time_of_day)
# print(type(time_of_day))


#4 
sentence = "This is a sentence"

words = sentence.split(" ")
print(words)

words1 = words[0]
words2 = words[1]
words3 = words[3]

print(words1)
print(words2)
print(words3)

#5
list_of_words = ['my', 'favorite', 'programming', 'language', 'is', 'pyhton']

sentence = " ".join(list_of_words)

print(sentence)