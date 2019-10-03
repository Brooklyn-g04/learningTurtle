# variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven_ = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("there are ""cars""cars available")
print("There are only", drivers, "drivers available")
print("there will be", cars_not_driven_, "empty cars today")
print("we can transport", carpool_capacity, "people today")
print("we have", passengers, "to carpool today")
print("we need to put about", average_passengers_per_car, "in each car")

# More variables
myName = "Brooklyn"
myAge = 14
myHeight = 60 # inches
myEyes = "Brown"
myTeeth = "white"
myHair = "lots"

print("Let's talk about %s." % myName)
print("She's %d inches tall." % myHeight)
print("Shes's got %s eyes and %s hair." % (myEyes, myHair))
print("Her teeth \tare usually %s depending \n on the coffee." % myTeeth)
print("if i add %d and %d, i get %d" % (myAge, myHeight, myAge + myHeight))
