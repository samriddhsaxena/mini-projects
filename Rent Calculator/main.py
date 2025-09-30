print("RENT CALCULATOR")
print()

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter your food cost = "))
electricity = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit of electricity = "))
persons = int(input("Enter the number of persons in your room = "))

total_bill = electricity*charge_per_unit

output = (food+rent+total_bill)//persons

print("Each person will pay = ",output)
