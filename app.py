from database import (
    create_table,
    add_product,
    get_products,
    search_products,
    update_product,
    delete_product,
    get_inventory_value )


def show_products(products):
    if not products:
        print("\nNo products found.")
        return

    print("\nID | Name | Category | Price | Quantity")
    print("-" * 55)

    for product in products:
        print(
            f"{product[0]} | {product[1]} | "
            f"{product[2]} | ₹{product[3]:.2f} | {product[4]}"
        )


def main():
    create_table()

    while True:
        print("\n===== PRODUCT MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        print("7. Total Inventory valu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product Name: ")
            category = input("Category: ")

            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                add_product(name, category, price, quantity)
                print("Product added successfully!")

            except ValueError:
                print("Please enter valid price and quantity.")

        elif choice == "2":
            products = get_products()
            show_products(products)

        elif choice == "3":
            keyword = input("Enter product name/category: ")
            products = search_products(keyword)
            show_products(products)

        elif choice == "4":
            try:
                product_id = int(input("Product ID: "))
                name = input("New Product Name: ")
                category = input("New Category: ")
                price = float(input("New Price: "))
                quantity = int(input("New Quantity: "))

                if update_product(
                    product_id, name, category, price, quantity
                ):
                    print("Product updated successfully!")
                else:
                    print("Product ID not found.")

            except ValueError:
                print("Please enter valid values.")

        elif choice == "5":
            try:
                product_id = int(input("Product ID to delete: "))

                if delete_product(product_id):
                    print("Product deleted successfully!")
                else:
                    print("Product ID not found.")

            except ValueError:
                print("Please enter a valid Product ID.")

        elif choice == "6":
            print("Thank you!")

        else:
            print("Invalid choice. Please select 1-6.")
            
        elif choice == "7":
           total = get_inventory_value()
           print(f"Total Inventory Value: ₹{total:.2f}")
           break


if __name__ == "__main__":
    main()
