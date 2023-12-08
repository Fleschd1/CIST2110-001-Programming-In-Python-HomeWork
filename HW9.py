# HW9.py
# Author: Daniel Flesch

# This homework will expand upon the code for Lab11.py. If you did not complete Lab11.py, you should do so before attempting this homework.

# Copy the code from Lab11.py into this file 1-11. I'll add some comments to help you out.


### INSERT CODE FROM LAB11.PY HERE 1-11###
class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id   

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.cart = []

    def __str__(self) -> str:
        return f"Customer: {self.name}, ID: {self.customer_id}"
    
    def add_to_cart(self, product: Product):
        self.cart.append(product)
        print(f"{product} was added to {self.name}'s cart.""\n")

    def remove_from_cart(self, product: Product):
        self.cart.remove(product)
        print(f"{product} was removed from {self.name}'s cart.""\n")

    def checkout(self):
        total = 0
        for product in self.cart:
            total += product.price
        print(f"{self.name}'s total is ${total}")
        self.cart = []

    def display_products(self):
        print(f"{self.name}'s Cart")
        for product in self.cart:
            print(product)


    def display_products_pretty(self):
        import tabulate
        print(f"{self.name}'s Cart:")
        print(
            tabulate.tabulate(
                [product.__dict__ for product in self.cart], tablefmt= "fancy_grid"
            )
        )

class Store:
    def __init__(self):
        self.products = []
        self.customers = []


    def add_product(self, product: Product):
        self.products.append(product)
        print(f"{product} was added to the store.""\n")

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer} was added to the store.""\n")

    def display_products(self):
        print("Products: ")
        for product in self.products:
            print(product)
            
    def display_customers(self):
        print("Customers: ")
        for customer in self.customers:
            print(customer)
### END CODE FROM LAB11.PY ###

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def add_product_to_customer_cart(customer: Customer, product : Product):
    Customer.add_to_cart(customer, product)


customer1 = Customer("Jeff", 2)
product1 = Product("iPad", 400, 1)

# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer: Customer, product: Product):
    Customer.remove_from_cart(customer, product)


# 3. Create a menu function that will display the following menu: 
def menu():
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Add Product to Customer's Cart")
    print("4. Remove Product from Customer's Cart")
    print("5. Display Products")
    print("6. Display Customers")
    print("7. Display Customer's Cart")
    print("8. Checkout")
    print("9. Exit")
    choice = input("Enter a choice: ")
    return int(choice)
# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.
# IE main function should look something like this:
def main():
    store = Store()
    while True:
        choice = menu()
        if choice == 1:
            store.add_product(product1)
        elif choice == 2:
            store.add_customer(customer1)
        elif choice == 3:
            add_product_to_customer_cart(customer1, product1)
        elif choice == 4:
            remove_product_from_customer_cart(customer1, product1)
        elif choice == 5:
            store.display_products()
        elif choice == 6:
            store.display_customers()
        elif choice == 7:
            customer1.display_products_pretty()
        elif choice == 8:
            customer1.checkout()
        elif choice == 9:
            print("Goodbye")
            break
# ETC...

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.
# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.

if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
