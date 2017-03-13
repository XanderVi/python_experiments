"""
Script for finding nearest city to your location.
It's count range like straight line, without considering roads, mountains etc.
Made by Alexander Viter
"""
import math
import re

arr = []
distance = []

lon = input() #user's longitude
lat = input() #user's latitude 
lon = float(re.sub(r",", ".", lon)) #if entered in format 3,1415926
lat = float(re.sub(r",", ".", lat)) #like string, not float
n = int(input()) #number of cities which we are testing
for i in range(n):
    city = input()
    arr1 = city.split(";")
# entered in format: 1;Ukraine;Kiev;capital of Ukraine;30.5238000;50.4546600
    arr.append(arr1)
    #arr[i][0] = number
    #arr[i][1] = country
    #arr[i][2] = city
    #arr[i][3] = other info
    #arr[i][4] = lon
    #arr[i][5] = lat
    arr[i][4] = float(re.sub(r",", ".", arr[i][4]))
    arr[i][5] = float(re.sub(r",", ".", arr[i][5]))
    x = (arr[i][4] - lon) * math.cos( (arr[i][5] + lat) / 2)
    y = arr[i][5] - lat
    distance.append(math.sqrt(x**2 + y**2) * 6271)
#https://en.wikipedia.org/wiki/Haversine_formula

print(arr[distance.index(min(distance))][1])
