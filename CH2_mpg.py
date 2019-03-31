#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallon_cost = float(input("Enter cost of a gallon of gas:\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
total_cost = round(gallon_cost * gallons_used, 2)
cost_per_mile = round(total_cost / miles_driven, 2)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(total_cost))
print("Cost Per Mile:\t\t" + str(cost_per_mile))
print()
print("Bye")


