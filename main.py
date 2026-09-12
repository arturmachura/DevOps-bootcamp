calculation_to_units = 24 *60 *60
name_of_unit = "seconds"


def days_to_units():
    user_input = input("Enter number of days and I will convert it to seconds: ")
    days = int(user_input)
    calculated_units = days * calculation_to_units
    print(f"{days} days are {calculated_units} {name_of_unit}.")

days_to_units()


