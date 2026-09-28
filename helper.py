def days_to_units(num_of_days, conversion_unit):
    conversions = {
        "hours": num_of_days * 24,
        "minutes": num_of_days * 24 * 60,
        "seconds": num_of_days * 24 * 60 * 60
    }
    if conversion_unit not in conversions:
        return "Unsupported unit."
    return f"{num_of_days} days are {conversions[conversion_unit]} {conversion_unit}."


user_input_message = "Hey user, enter number of days and conversion unit (or 'exit' to quit): "