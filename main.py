calculation_to_units = 24 *60 *60
name_of_unit = "seconds"

def get_user_input():
    user_input = input("Enter number of days and I will convert it to seconds (or 'exit' to quit): ")
    return user_input

def validate_and_execute(number_of_days):
    try:
        days = int(number_of_days)
        if days > 0:
            calculated_units = days * calculation_to_units
            print(f"{days} days are {calculated_units} {name_of_unit}.")
        elif days == 0:
            print("You entered 0 days, which is equal to 0 seconds.")
        else:
            print("You entered a negative number of days, which is not valid.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

user_input = ""

while user_input != "exit":
    user_input = get_user_input()
    if user_input.lower() == "exit":
        break
    for number_of_days in set(x.strip() for x in user_input.split(",")):
        validate_and_execute(number_of_days)








    
    









