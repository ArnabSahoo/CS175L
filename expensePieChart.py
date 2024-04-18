#CS175

#Arnab Sahoo

#expensePieChart.py


import matplotlib.pyplot as plt

def read_expenses(file_path):
    expenses = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                category, amount = line.strip().split('\t')
                try:
                    expenses[category] = int(amount)
                except ValueError:
                    print(f"Error: Invalid amount for category '{category}'. Skipping.")
    except IOError:
        print("Error: Could not open the file.")
    return expenses

def plot_pie_chart(expenses):
    labels = list(expenses.keys())
    values = list(expenses.values())

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution')
    plt.show()

def main():
    file_path = 'expenses.txt'
    expenses = read_expenses(file_path)
    if expenses:
        plot_pie_chart(expenses)

if __name__ == "__main__":
    main()


