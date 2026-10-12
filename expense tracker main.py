# _____________________________     
# PERSONAL EXPENSE TRACKER
#_____________________________
expenses = []

def addexpense():
    print("--- add expense ---")

    name = input("enter expense name: ")

    
    amount = float(input("enter amount: "))

    if amount <= 0:
        print("amount must be greater than 0.")
            
    expense = {"name": name,"amount": amount}

    expenses.append(expense)

    print("expense added successfully.")

def viewexpenses():
    print("--- expense List ---")

    if len(expenses) == 0:
        print("no expenses recorded.")
        return

    print("no.   Expense              Amount")
    print("-----------------------------------")

    for i in range(len(expenses)):
        print(i + 1, "   ", expenses[i]["name"],
              "          Rs.", expenses[i]["amount"])

def deleteexpense():
    print("--- Delete Expense ---")

    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    viewexpenses()


    number = int(input("Enter expense number to delete: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
            
    removed = expenses.pop(number - 1)

    print(removed["name"], "has been deleted.")

def totalexpense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense: Rs.", total)

def highestexpense():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("highest Expense:")
    print("name   :", highest["name"])
    print("Amount : Rs.", highest["amount"])

def expensecount():
    print("Number of expenses:", len(expenses))

def showsummary():
    print("--- Expense Summary ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    total = 0
    highest = expenses[0]

    for expense in expenses:
        total = total + expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("number of expenses :", len(expenses))
    print("total expense      : Rs.", total)
    print("tighest expense    : Rs.", highest["amount"])
    print("highest expense is :", highest["name"])



def clearexpenses():
    if len(expenses) == 0:
        print("there are no expenses to clear.")
        return

    choice = input( "are you sure you want to delete all expenses? (y/n): ")

    if choice == "y" or choice == "Y":
        expenses.clear()
        print("all expenses have been deleted.")
    else:
        print("operation cancelled.")

def main():

    while True:

        print("___________________________________")
        print("       PERSONAL EXPENSE TRACKER")
        print("_____________________________________")

        print("1. add expense")
        print("2. view expenses")
        print("3. delete expense")
        print("4. total expense")
        print("5. highest expense")
        print("6. number of expenses")
        print("7. expense summary")
        print("8. clear all expenses")
        print("9. exit")

        choice = input("\nenter your choice: ")

        if choice == "1":
            addexpense()

        elif choice == "2":
            viewexpenses()

        elif choice == "3":
            deleteexpense()

        elif choice == "4":
            totalexpense()

        elif choice == "5":
            highestexpense()

        elif choice == "6":
            expensecount()

        elif choice == "7":
            showsummary()

        elif choice == "8":
            clearexpenses()

        elif choice == "9":
            print("thank you for using Personal Expense Tracker.")
            break

        else:
            print("invalid choice. Please try again.")
main()
