from input_handler import InputValidator

from password_crafter import craft_password


def main():
    print("🔐 Welcome to KeyCrafter 🔐")

    while True:
        length_of_password = InputValidator().get_int("Enter the total length of the password to craft: ")
        number_of_digits = InputValidator().get_int("Enter the number of numeric characters to include: ")
        number_of_symbols = InputValidator().get_int("Enter the number of symbols to include: ")

        if number_of_digits + number_of_symbols >= length_of_password:
            print("Symbol + Digit count exceeds total password length!")
        else:
            number_of_letters = length_of_password - number_of_symbols - number_of_digits
            break

    password = craft_password(number_of_digits=number_of_digits,
                              number_of_letter=number_of_letters,
                              number_of_symbols=number_of_symbols)

    print(f"\n🧪 Your crafted password: {password}")


if __name__ == "__main__":
    main()