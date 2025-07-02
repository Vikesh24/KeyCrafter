""" Script to generate a random password for given length """
import secrets
import string

def craft_password(number_of_digits: int, number_of_symbols: int, number_of_letter: int) -> str:
    """
    Function to craft a password of given number of digits, symbols and letter combination
    :param number_of_digits: Number of numeric digits to include
    :param number_of_symbols: Number of symbols to include
    :param number_of_letter: Number of letters to include
    :return: the password string
    """
    password = []

    for _ in range(number_of_digits):
        password.append(secrets.choice(string.digits))

    for _ in range(number_of_symbols):
        password.append(secrets.choice(string.punctuation))

    for _ in range(number_of_letter):
        password.append(secrets.choice(string.ascii_letters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)