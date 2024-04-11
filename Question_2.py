#Task 1
shopping_list = []

def grocery_list():
    while True:
        print('1. View List')
        print('2. Add Item')
        print('3. Remove Item')
        print('4. Exit')
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current List: ")
            for x in shopping_list:
                print(x)
        elif choice == "2":
            new_item = input("Enter the name of the new product: ")
            shopping_list.append(new_item)
            print(f"{new_item} has been added to the inventory")
#Task 2        
        elif choice == "3":
            item_to_remove = input("Enter the name of the product to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} has been removed")
            else:
                print(f"{item_to_remove} not found in inventory")
        elif choice == "4":
            break
        else:
            print("Invalid entry, please choose again")

grocery_list()