# s225224771 - Ambesiwe Majavu
# s225025426 - Liyema Booi

stock_code_list = list()
stock_price_list = list()
stock_count_list = list()

def AddStockCode():
    while True:
        decision = input("Would you like to add a stock code? (y or n): ")
        decision = decision.lower()

        if decision == "y":
            print("-" * 50)
            print("Adding a stock code")
            print("-" * 50)

            stock_c = input("Enter stock code: ")
            stock_c = stock_c.upper()

            if len(stock_code_list) < 50:
                stock_code_list.append(stock_c)
                print("Stock code added.")
                print("")
            else:
                print("The number of stock codes added to system must not exceed 50!")
                break

            while True:
                stock_p = input("Enter stock price: ")
                try:
                    stock_p = float(stock_p)

                    while stock_p > 1000:
                        print("The price of stock item must exceed 1000!")
                        stock_p = float(input("Enter stock price: "))

                    if stock_p <= 1000:
                        stock_price_list.append(stock_p)
                        print("Stock price added.")
                        print("")
                        break

                except ValueError as msg:
                    print()
                    print(msg, "\n")

        elif decision != "n":
            print("Make sure to enter 'y' or 'n'!")
            continue

        elif decision == "n":
            break


# Create function called SearchCode()
def SearchCode(search):
    global code, index
    try:
        index = -1
        for item, code in enumerate(stock_code_list):
            if stock_code_list[item] == search:
                index = item
                break
        if index > -1:
            print(search, "was found as stock number ", index + 1, ".")
            print("")
            return index
        else:
            print("Stock code does not exist!")
            print("")

        return -1
    except IndexError as msg:
        print("Invalid index!", msg)


def AddStockItem():
    while True:
        decision = input("Would you like to add a stock item? (y or n): ")
        decision = decision.lower()

        if decision == "y":
            print("-" * 50)
            print("Adding number of items to include under stock code ")
            print("-" * 50)

            stk_code = input("Enter stock code you wish to search for: ")
            stk_code = stk_code.upper()
            stk_index = SearchCode(stk_code)

            if stk_index == -1:
                # SearchCode function displays necessary feedback
                continue

            while True:
                num_of_items = input("Enter number of items (maximum is 100): ")

                try:
                    num_of_items = int(num_of_items)

                    while num_of_items > 100:
                        print("Number of items should not be more than 100!")
                        print("")
                        num_of_items = int(input("Enter number of items(max is 100): "))

                    else:
                        stock_count_list.insert(index, num_of_items)
                        print(num_of_items, "items have been added to stock code ", stk_code)
                        print("")
                        break

                except ValueError as msg:
                    print()
                    print(msg, "\n")

        elif decision != "n":
            print("Make sure to enter 'y' or 'n'!")
            continue

        elif decision == "n":
            break


def DisplayStockList():

    total = 0.00

    if len(stock_count_list) != len(stock_code_list):
        print("To display stock list, please provide the number of stock item for every existing stock code.")
    else:
        print("-" * 50)
        print("Stock Code | In stock | Price      | Stock Value")
        print("-" * 50)
        for code, price, num_of_items in zip(stock_code_list, stock_price_list, stock_count_list):
            total_stock_value = price * num_of_items
            print(f"{code:<10} | {num_of_items:<8.0f} | R {price:<8.2f} | R {total_stock_value:<10.2f}")
            total += total_stock_value
        print("-" * 50)
        print("Total: ", "R", str(float(total)))


def Menu():
    opt = 0
    while opt != 4:
        print()
        print("-" * 50)
        print("Menu:")
        print("1. Add Stock Code")
        print("2. Add Stock Item")
        print("3. Display Stock List")
        print("4. Exit")
        print("-" * 50)

        try:
            opt = int(input("Choose an option from the menu (1 - 4): "))
            print("")
            if opt == 1:
                AddStockCode()
            elif opt == 2:
                AddStockItem()
            elif opt == 3:
                DisplayStockList()
            elif opt == 4:
                print("System successfully closed!!!")
                break
            else:
                print("Invalid option. Please choose an option from 1 to 4 only!")
        except ValueError as msg:
            print()
            print(msg, "\n")


Menu()
