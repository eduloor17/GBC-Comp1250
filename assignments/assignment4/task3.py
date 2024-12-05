class NumbersToBeOrganized:
    def __init__(self):
        self.numbers = [
            73, 18, 64, 60, 26,
            33, 66, 74, 59, 69,
            60, 95, 53, 45, 57,
            1, 48, 88, 13, 62
        ]

    def categorize_numbers(self):
        # Open files in append mode
        with open('50_and_under.txt', 'a') as file_50_and_under, open('over_50.txt', 'a') as file_over_50:
            for number in self.numbers:
                # Determine the range of the number and append to the corresponding file
                if 1 <= number <= 50:
                    file_50_and_under.write(f"{number}\n")
                elif 51 <= number <= 100:
                    file_over_50.write(f"{number}\n")

    def main(self):
        self.categorize_numbers()
        print("Numbers have been categorized and written to files.")


# Running the program!
if __name__ == "__main__":
    numbers_to_be_organized = NumbersToBeOrganized()
    numbers_to_be_organized.main()
