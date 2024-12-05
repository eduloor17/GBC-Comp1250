from Task6_num_valid import Number


def main():
    print("I am using class to validate numbers.")
    valid = Number()
    user_num = input("Enter a number: ")
    valid.is_number_valid(user_num)
    print("Thank your for using the validate numbers program!")


if __name__ == "__main__":
    main()
