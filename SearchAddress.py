#Creator: Cody Puskas
import sys
import os
from geopy.geocoders import Nominatim

#Grabs Nominatim api
locator = Nominatim()

#Gets input from user
while True:
    try:
        user_location = str(raw_input("Enter an address: "))
        break
    except ValueError:
        print "Invalid input"
        sys.exit()

#Gets location from Nominatim api
location = locator.geocode(user_location)

if location is None:
    print "Address does not exist"
    input()

else: 
    print "Location Found"
    print location.address
    print (location.latitude, location.longitude)
    input()

