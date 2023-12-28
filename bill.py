# Initialize an empty grocery list
grocery_list = []


# Function to add an item to the list
def add_to_list(item,Qty,Rate):
    grocery_list.append({"Item": item, "Qty": Qty, "Rate": Rate})
    print(f"{item} has been added to the list.")


# Function to remove an item from the list
def remove_from_list(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")


# Function to display the current grocery list
def display_list():
    print("      ------------------------------------\n")
    print("\t\t\t\t\tD MART\t\t\t\t\n")
    print("      ------------------------------------\n")
    print("\t\tDate: 13/09/2023 \t\t\n\t\tPlace: Jalgaon")
    print("      ------------------------------------\n")
    print("\t\tProduct \t\t Qty \t\t Rate\t\t\n")
    for item in grocery_list:
        print(f"\t\t{item['Item']} \t\t\t {item['Qty']}KG \t\t Rs.{item['Rate']}\t\t")
        # print("      ------------------------------------\n")
        # print(f"\t\t{item} \t\t\t {Qty}KG \t\t Rs.{Rate}\t\t")


# Main program loop
while True:
    print("\nOptions:")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. Display the list")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        Qty = input("Enter the Quantity: ")
        Rate = input("Enter the Rate : ")
        add_to_list(item,Qty,Rate)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_from_list(item)
    elif choice == "3":
        display_list()
        print("\n      ------------------------------------")
        print("\t\t\t\t\tTHANK YOU\t\t\t\t")
        print("      ------------------------------------\n")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
