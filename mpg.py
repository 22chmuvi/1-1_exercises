#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t"))
# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
tgc = round(cost_per_gallon * gallons_used, 1)     
cpm = round(tgc / miles_driven, 1)      
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(tgc))
print("Cost Per Mile:\t\t" + str(cpm))
print()
print("Bye")
