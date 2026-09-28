from helper import days_to_units, user_input_message
import os
import logging

logger = logging.getLogger("MAIN")
logger.error("Error occurred in the app")


print(os.name)

"""

user_input = ""

while user_input != "exit":
    user_input = input(user_input_message)
    if user_input.lower() == "exit":
        break
    days_str, unit = user_input.split(":")
    result = days_to_units(int(days_str), unit)
    print(result)
"""