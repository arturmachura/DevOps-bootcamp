calculation_to_units = 24 *60 *60
name_of_unit = "seconds"

def days_to_units():
    user_input = input("Enter number of days and I will convert it to seconds: ")
    try:
        days = int(user_input)
        if days > 0:
            calculated_units = days * calculation_to_units
            print(f"{days} days are {calculated_units} {name_of_unit}.")
        elif days == 0:
            print("You entered 0 days, which is equal to 0 seconds.")
        else:
            print("You entered a negative number of days, which is not valid.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

days_to_units()