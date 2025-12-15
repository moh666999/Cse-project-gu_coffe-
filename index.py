def gu_caffe_menu():
    menu = [
        ["Espresso", 65.00],
        ["Double Espresso", 85.00],
        ["Cappuccino", 95.00],
        ["Cafe Latte", 100.00],
        ["Americano", 80.00],
        ["Mocha", 110.00],
        ["Flat White", 95.00],
        ["Hot Chocolate", 90.00],
        ["Turkish Coffee", 50.00],
        
        ["Iced Americano", 90.00],
        ["Iced Latte", 110.00],
        ["Cold Brew", 105.00],
        ["Caramel Frappe", 130.00],
        ["Berry Smoothie", 140.00],
        ["Still Water", 25.00],
        
        ["Butter Croissant", 85.00],
        ["Almond Croissant", 95.00],
        ["Chocolate Brownie", 90.00],
        ["Cheesecake Slice", 140.00],
        ["Tiramisu", 150.00],
        
        ["Bagel w/ Cream Cheese", 110.00],
        ["Avocado Toast", 220.00],
        ["Grilled Cheese", 180.00],
        ["Chicken Panini", 240.00],
        ["Caesar Salad", 210.00]
    ]

    order_list = []
    
    print("-" * 40)
    print(" WELCOME TO GU CAFFE ")
    print("-" * 40)

    while True:
        print("\n--- MENU ---")
        for i, item in enumerate(menu):
            print(f"{i + 1}. {item[0]:<25} {item[1]:.2f} EGP")
        
        print("-" * 40)
        print("Type the number to order, or 'exit' to finish.")
        
        choice = input("Enter choice: ")

        if choice.lower() == 'exit':
            break
        
        if choice.isdigit():
            index = int(choice) - 1
            
            if 0 <= index < len(menu):
                selected_item = menu[index]
                order_list.append(selected_item)
                print(f"Added: {selected_item[0]}")
            else:
                print("Invalid number. Please try again.")
        else:
            print("Please enter a number.")

    print("\n" + "=" * 40)
    print("      GU CAFFE RECEIPT      ")
    print("=" * 40)
    
    total_price = 0
    
    if len(order_list) > 0:
        for item in order_list:
            name = item[0]
            price = item[1]
            print(f"{name:<25} {price:.2f} EGP")
            total_price += price
    else:
        print("No items purchased.")
        
    print("-" * 40)
    print(f"TOTAL DUE:{' '*10}{total_price:.2f} EGP")
    print("=" * 40)
    print("Thank you for visiting Gu Caffe!")

gu_caffe_menu()
