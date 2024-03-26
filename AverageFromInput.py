#CS175

#Arnab Sahoo

#AverageFromInput.py

def main():
    total = 0
    count = 0

    with open('numbers.txt', 'r') as file:
        for line_number, line in enumerate(file, 1):
            number = float(line.strip())
            total += number
            count += 1
            print(f"I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}")

    if count > 0:
        average = total / count
        print(f"Average: {average:.1f}") 
    else:
        print("No numbers found in the input file.")


if __name__ == "__main__":
    main()
