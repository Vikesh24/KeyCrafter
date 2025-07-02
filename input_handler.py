
class InputValidator:
    @staticmethod
    def get_int(prompt:str):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError as e:
                print("❌ Invalid input. Please enter a numeric value.")

    @staticmethod
    def get_string(prompt):
        while True:
            value = input(prompt)
            if value.isalpha():
                return value
            else:
                print("❌ Invalid input. Please enter a valid string.")