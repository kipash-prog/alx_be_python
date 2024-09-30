def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item=input("Enter the item to add: ")
            shopping_list.append(add_item)
        elif choice == '2':
            remove_item=input("Enter the item to add: ")
            if remove_item in shopping_list:
              shopping_list.remove(remove_item)
              print(f"'{remove_item}' has been removed from your shopping list.")
            else:
                print(f"{remove_item} is not found in the list")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
