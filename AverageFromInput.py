# AverageFromInput.py

def main():
    total = 0
    count = 0

    with open('numbers.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            number = float(line.strip())
            total += number
            count += 1
            average = total / count
            print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f} Average is: {average:.2f}")

if __name__ == "__main__":
    main()
