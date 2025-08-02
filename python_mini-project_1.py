# creating a backend feature for an e-commerce website.
# when a user adds items to their shopping cart, we need to store the list of products they selected.

shopping_cart = []

def show_menu():
    print("\n🛒 shopping cart menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Count specific item")
    print("5. clear cart")
    print("6. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_cart.append(item)
        print(f" '{item}' is added to cart")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f" '{item}' item removed 🗑️ successfully!")
        else:
            print("Item not found ☹️")

    elif choice == "3":
        if shopping_cart:
            print("Current cart items")
            for i,item in enumerate(shopping_cart, 1):
                print(f"{i}.{item}")
        else:
            print("Cart is empty")

    elif choice == "4":
        item = input("Enter item to count: ")
        count = shopping_cart.count(item)
        print(f"you have {count} '{item}'(s) in your cart")

    elif choice == "5":
        shopping_cart.clear()
        print("Cart has been cleared")

    elif choice == "6":
        print("Thank you for shopping😊.see you again 😉")
        break
    else:
        print("choice not found😟.please select the choice from (1-6)")

