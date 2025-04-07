import datetime  # Import the datetime module for handling dates and times

# Define a dictionary 'products' to store product information.
# The structure is: {category: {product: {price: ..., stock: ...}}}
products = {
    "Groceries": {
        "Bread": {"price": 45, "stock": 50},
        "Bagel": {"price": 23.50, "stock": 30},
        "Croissant": {"price": 24, "stock": 20},
        "Rice": {"price": 24, "stock": 40},
        "Flour": {"price": 22, "stock": 30},
        "Sugar": {"price": 12, "stock": 40},
        "Pasta": {"price": 10, "stock": 60},
        "Apple": {"price": 12, "stock": 20},
        "Banana": {"price": 6, "stock": 20},
        "Carrot": {"price": 8.10, "stock": 30},
        "Potato": {"price": 12, "stock": 50},
        "Tomato": {"price": 15.50, "stock": 20},
        "Chicken": {"price": 60, "stock": 60},
        "Ground Beef": {"price": 75, "stock": 60},
        "Pork": {"price": 90, "stock": 40},
        "Salmon": {"price": 105, "stock": 20},
        "Shrimp": {"price": 60, "stock": 30},
        "Cheese": {"price": 15, "stock": 50},
        "Butter": {"price": 20, "stock": 30},
        "Yogurt": {"price": 18.50, "stock": 20},
        "Eggs": {"price": 10.50, "stock": 60},
        "Ketchup": {"price": 12, "stock": 40},
        "Salt": {"price": 6, "stock": 30},
        "All Purpose Seasoning": {"price": 16, "stock": 25},
        "Olive Oil": {"price": 36, "stock": 20},
    },
    "Beverages": {
        "Sparkling Water": {"price": 7, "stock": 40},
        "Soda": {"price": 8, "stock": 60},
        "Orange Juice": {"price": 18.50, "stock": 25},
        "Energy Drink": {"price": 12.50, "stock": 60},
        "Cow's Milk": {"price": 18.50, "stock": 25},
        "Almond Milk": {"price": 16, "stock": 20},
        "Iced Tea": {"price": 18.50, "stock": 20},
        "Lemonade": {"price": 16, "stock": 20},
        "Beer": {"price": 30, "stock": 40},
        "Vodka": {"price": 60, "stock": 25},
        "Red Wine": {"price": 54, "stock": 30},
        "Whiskey": {"price": 75, "stock": 20},
    },
    "Household Items": {
        "Paper Towel": {"price": 20, "stock": 30},
        "Toilet Paper": {"price": 10.50, "stock": 60},
        "Air Freshner": {"price": 15, "stock": 22},
        "Dish Soap": {"price": 12.50, "stock": 40},
        "Laundry Detergent": {"price": 22, "stock": 30},
        "Trash Bags": {"price": 15, "stock": 25},
        "Sponge": {"price": 10, "stock": 40},
        "LED Bulb": {"price": 20, "stock": 20},
        "Batteries": {"price": 18, "stock": 25},
        "Broom": {"price": 20, "stock": 15},
    },
    "Personal Care": {
        "Shampoo": {"price": 20, "stock": 30},
        "Conditioner": {"price": 20, "stock": 30},
        "Body Wash": {"price": 17, "stock": 35},
        "Toothpaste": {"price": 12.50, "stock": 40},
        "Toothbrush": {"price": 6.50, "stock": 24},
        "Mouth Wash": {"price": 22, "stock": 26},
        "Deodorant": {"price": 15, "stock": 20},
        "Razor Blades": {"price": 30, "stock": 20},
        "Sunscreen": {"price": 12, "stock": 30},
        "Hand Soap": {"price": 17, "stock": 25},
        "Sanitizer": {"price": 20, "stock": 30},
        "Tampon": {"price": 22, "stock": 20},
    },
}

# Define an empty dictionary 'cart' to store the items the customer wants to buy.
# The structure will be: {product_name: quantity}
cart = {}

# Define an empty list 'sales_history' to store records of completed sales.
# Each sale record will be a dictionary.
sales_history = []

# Function to display the product catalogue.
def view_product_catalogue():
    print("\nProduct Catalogue:")
    for category, items in products.items():  # Iterate through each category and its items
        print(f"\n{category}:")
        for i, (product, details) in enumerate(items.items(), 1): # Iterate through each item with index
            print(f"{i}. {product} - ${details['price']} (Stock: {details['stock']})")

# Function to check if a product is available in the desired quantity.
def is_product_available(category, product, quantity):
    if category in products and product in products[category] and products[category][product]['stock'] >= quantity:
        return True
    return False

# Function to add items to the cart.
def add_to_cart():
    while True: # Loop to continue adding items until user chooses not to
        category = input("Enter product category: ").title() # Get category from user, title case.
        if category in products:
            print(f"\n{category}:")
            item_list = list(products[category].items()) # Convert category items to list for indexing.
            for i, (product, details) in enumerate(item_list, 1):
                print(f"{i}. {product} - ${details['price']} (Stock: {details['stock']})")
            try:
                item_number = int(input("Enter item number: ")) # Get item number from user.
                if 1 <= item_number <= len(item_list): # Check if item number is valid.
                    product, details = item_list[item_number - 1] # Get product and details from list.
                    try:
                        quantity = int(input(f"Enter quantity for {product}: ")) # Get quantity from user.
                        if quantity <= 0:
                            print("Quantity must be greater than 0. Please try again.")
                            continue

                        if is_product_available(category, product, quantity): # Check if product is available.
                            cart[product] = cart.get(product, 0) + quantity # Add item to cart.
                            products[category][product]['stock'] -= quantity # Update stock.
                            print(f"{quantity} {product}(s) added to the cart.")
                            if products[category][product]['stock'] < 5:
                                print(f"You're running low on {product} ({category}).")
                        else:
                            print(f"Sorry, only {products[category][product]['stock']} {product}(s) are available.")
                    except ValueError:
                        print("Invalid input. Please enter a valid quantity.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Invalid input. Please enter a valid item number.")
        else:
            print("Ops! Product category not found.")

        while True:
            print("\nDo you want to add more items?")
            print("1. Yes")
            print("2. No")
            add_more = input("Enter 1 for Yes or 2 for No.: ")

            if add_more == "1":
                break
            elif add_more == "2":
                return
            else:
                print("Invalid choice. Please enter 1 for Yes or 2 for No.")

# Function to remove items from the cart.
def remove_from_cart():
    if not cart:
        print("Sorry! The cart is empty.")
        return
    while True:
        product = input("Enter the name of the product you want to remove from the cart: ").title() #Get product to remove.
        if product in cart:
            try:
                quantity = int(input(f"Enter quantity of {product} to remove: ")) #Get quantity to remove.
                if quantity <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue
                if cart[product] >= quantity:
                    cart[product] -= quantity #Decrease quantity in cart.
                    for cat, item in products.items():
                        if product in item:
                            products[cat][product]['stock'] += quantity #Increase stock
                    print(f"{quantity} {product}(s) removed from the cart.")
                    if cart[product] == 0:
                        del cart[product] #Remove item from cart if quantity is 0
                    break
                else:
                    print(f"Only {cart[product]} {product}(s) in the cart.")
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
        else:
            print(f"{product} is not in the cart.")

# Function to display the items in the cart and calculate the subtotal.
def view_cart():
    if not cart:
        print("The cart is empty.")
        return 0
    print("\nCart:")
    subtotal = 0
    for product, quantity in cart.items():
        for cat, item in products.items():
            if product in item:
                total = item[product]['price'] * quantity
                subtotal += total
                print(f"{product}: {quantity} @ ${item[product]['price']} = ${total}")
    return subtotal

# Function to display items with low stock.
def view_low_stock_items():
    low_stock = {}
    for category, items in products.items():
        for product, details in items.items():
            if details['stock'] < 5:
                low_stock[f"{product} ({category})"] = details['stock']
    if low_stock:
        print("\nLow Stock Alert:")
        for item, stock in low_stock.items():
            print(f"- {item}: {stock} left")

# Function to handle the checkout process.
def checkout():
    subtotal = view_cart()
    if subtotal == 0:
        return
    tax_rate = 0.10
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    discount_rate = 0
    discount_amount = 0
    if subtotal >= 1000:
        discount_rate = 0.10
        discount_amount = subtotal * 0.10
        total -= discount_amount
    elif subtotal >= 500:
        discount_rate = 0.05
        discount_amount = subtotal * 0.05
        total -= discount_amount

    print("\nCheckout:")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount_amount > 0:
        print(f"Discount: ${discount_amount:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    while True:
        try:
            change = 0
            amount_paid = float(input("Enter amount received: "))
            if amount_paid < total:
                print("Ops! The amount entered is not enought to cover the total.")
                print("Would you like to remove the item(s) from the cart?")
                while True:
                    print("1. Yes")
                    print("2. No")
                    choice = input("Enter 1 for Yes or 2 for No.: ")
                    if choice == "1":
                        for product, quantity in cart.items():
                            for cat, item in products.items():
                                if product in item:
                                    products[cat][product]['stock'] += quantity
                        cart.clear()
                        return
                    elif choice == "2":
                        break
                    else:
                        print("Invalid input. Please enter 1 for Yes or 2 for No")
                continue
            change = amount_paid - total
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Change: ${change:.2f}")

    receipt_width = 50
    print("\n" + "BEST BUY SUPERMARKET".center(receipt_width))
    print("\n" + "17 Worthington Ave, Kingston 5".center(receipt_width))
    print("Tel# +1 (876) 123-4567".center(receipt_width))
    date = datetime.datetime.now().strftime("%d/%m/%y")
    time =  datetime.datetime.now().strftime("%I:%M %p")
    print(f"{"Date: " + date:<25}{"Time: " + time:>25}")
    print("-" * receipt_width)

    print(f"{"Item(s)":<25}{"Qty":^10}{"Price":>15}")
    print("=" * receipt_width)
    for product, quantity in cart.items():
        for cat, item in products.items():
            if product in item:
                unit_price = item[product]["price"]
                total_price = unit_price * quantity
                print(f"{product:<25}{str(quantity):^10}{"$" + format(total_price, ".2f"):>15}")

    print("=" * receipt_width)
    print(f"{'Subtotal: ${:.2f}'.format(subtotal).rjust(receipt_width)}")
    if discount_amount > 0:
        print(f"{'Discount ({}%): -${:.2f}'.format(int(discount_rate * 100), discount_amount).rjust(receipt_width)}")

    print(f"{'Tax ({}%): +${:.2f}'.format(int(tax_rate * 100), tax_amount).rjust(receipt_width)}")
    print(f"{'Total: ${:.2f}'.format(total).rjust(receipt_width)}")
    print(f"{'Cash: ${:.2f}'.format(amount_paid).rjust(receipt_width)}")
    print(f"{'Change: ${:.2f}'.format(change).rjust(receipt_width)}")
    print("-" * receipt_width)
    print("\n" + "Thank You For Shopping With Us!".center(receipt_width))

    sales_history.append({
        "date": datetime.datetime.now().strftime("%d/%m/%y %I:%M %p"),
        "items": cart.copy(),
        "total": total,
    })
    cart.clear()

# Function to display the sales history.
def view_sales_history():
    if not sales_history:
        print("No sales history available.")
        return
    print("\nSales History:")
    for sale in sales_history:
        print(f"Date: {sale['date']}")
        print("Items:")
        for item, quantity in sale['items'].items():
            print(f"  {item}: {quantity}")
        print(f"  Total: ${sale['total']:.2f}")

# Function to display the main menu and handle user input.
def main_menu():
    while True:
        print("\n" + " " * 10 + "B E S T  B U Y  S U P E R M A R K E T")
        print("\nMain Menu")
        print("1. View Product Catalogue")
        print("2. Add items to Cart")
        print("3. Remove items from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. View Low Stock Items")
        print("7. View Sales History")
        print("8. Exit")
        choice = input("Choose an option from 1 to 8: ")

        if choice == "1":
            view_product_catalogue()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
            while True:
                print("\nWould you like to process another transaction?")
                print("1. Yes")
                print("2. No")
                another_transaction = input("Enter 1 for Yes or 2 for No: ")
                if another_transaction == "1":
                    break
                elif another_transaction == "2":
                    return
                else:
                    print("Invalid choice. Please enter 1 for Yes or 2 for No.")
        elif choice == "6":
            view_low_stock_items()
        elif choice == "7":
            view_sales_history()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose an option from 1 to 8.")

# Call the main menu function to start the program.
main_menu()