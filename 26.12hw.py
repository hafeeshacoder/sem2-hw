class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        
        return num1 - num2

    def display_menu(self):
        print("1. Addition")
        print("2. Subtraction")
        print("3. Exit")


    def get_user_choice(self):
        return input("Enter your choice: ")

    def get_numbers(self):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError as e:
                print(f"ValueError: {e}")
    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            return None

    def perform_operation(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                num1, num2 = self.get_numbers()
                print(f"{num1} + {num2} = {self.add(num1, num2)}")

            elif choice == "2":
                num1, num2 = self.get_numbers()
                print(f"{num1} - {num2} = {self.sub(num1, num2)}")

            elif choice == "3":
                try:
                    key = "exit"
                    calc_key = input("Enter 'exit' to confirm: ")
                    if calc_key == key:
                        break
                    else:
                        raise KeyError("Invalid key")
                except KeyError as e:
                    print(f"KeyError: {e}")

            else:
                try:
                    raise TypeError("Invalid choice")
                except TypeError as e:
                    print(f"TypeError: {e}")

calc = Calculator()
calc.perform_operation()

