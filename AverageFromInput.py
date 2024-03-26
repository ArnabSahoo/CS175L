#CS175

#Arnab Sahoo

#AverageFromInput.py

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    number = float(line.strip())
                    numbers.append(number)
                    print(f"I read in {len(numbers)} number(s) Current number is: {number:8.2f} Total is: {sum(numbers):8.2f}")
                except ValueError:
                    print(f"Bad data: {line.strip()} skipping")
    except IOError:
        print(f"SystemExit: File not found: {filename} - exiting")
        exit(1)
    return numbers

def calculate_average(numbers):
    if numbers:
        average = sum(numbers) / len(numbers)
        return average
    else:
        return None

def main():
    filename = 'numbers.txt'
    numbers = read_numbers_from_file(filename)
    average = calculate_average(numbers)
    if average is not None:
        print(f"Average: {average:.1f}")
    else:
        print("No valid numbers found in the input file.")


if __name__ == "__main__":
    main()
