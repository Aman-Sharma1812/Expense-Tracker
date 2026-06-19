#-------------------------------------------------------------------------------------
expensesList = []
print("\nWelcome to Expense Tracker\n")

while True :

    print("=======Menu=======")
    print("1. Add Items that you buy")
    print("2. View your total expenses")
    print("3. Exist")
    print("-------------------------")

    choice = int(input("\nEnter your choice\n"))

    if choice == 1 :
        
        item = []
        price = []

        noi = int(input("Enter No. of items you buy\n"))
        for i in range(noi) :
            i = input(f"Enter your {i+1} items\n")
            item.append(i)
        

        for p in range(noi) :
            p = float(input(f"Enter <-{item[p]}-> price \n"))
            price.append(p)

        expenses = {
            "items" : item,
            "prices" : price
        }

        expensesList.append(expenses)
        print("\n---Expense added successfully---\n")

    elif choice == 2:
        print("\nBelow are the list of items along with prices\n")
        print(item)
        print(price)
        total = sum(price)
        print(f"You spent total Rs. {total} money\n")
    
    else:
        print("Thank you for using Expense_Tracker\n")
        print("Have a nice day\n")
        break
