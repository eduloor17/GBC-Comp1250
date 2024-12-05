from Task7_num_odd import Odd


def main():
    print("I am using a class to validate odd numbers.")
    odd_number = Odd()
    user_number = input("Enter a number: ")
    odd_number.validate_and_check_odd(user_number)


if __name__ == "__main__":
    main()
