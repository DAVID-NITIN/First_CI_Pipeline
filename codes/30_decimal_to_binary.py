def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number cannot be negative")
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2
    return binary