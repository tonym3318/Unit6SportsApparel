"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.
Name: Anthony Marquez
Date: 11/24/2026
Version: 1.0
----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    #
    # Python dictionaries handle hash collisions internally.
    # Collisions occur when different keys map to the same table location.
    # Too many collisions can reduce lookup performance
    # Create an empty dictionary for the sports apparel orders.
    # Each order number is a unique key, and the apparel is its value.
    # Python dictionaries use hashing for efficient key-value lookups.
    # Hashing allows orders to be located without searching every entry.

    orders = {}

    # Add customer orders for NFL, MLB, and college apparel.
    orders[1001] = "San Francisco 49ers Jersey"
    orders[1002] = "LA Dodgers Jacket"
    orders[1003] = "Pittsburgh Steelers Jersey"
    orders[1004] = "Colorado Buffaloes Jacket"
    orders[1005] = "Boston Red Sox Jersey"
    orders[1006] = "Arizona Wildcats Jacket"

    # Display all orders currently stored in the dictionary.

    print("\nCurrent Sports Apparel Orders:")
    for order_id, apparel in orders.items():
        print(f"Order {order_id}: {apparel}")

    print("\n=== INSERT OPERATIONS ===")
    print(f"\nSuccessfully added {len(orders)} customer orders.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Look up two existing customer orders using their order numbers.
    # The dictionary uses the order number as a key to find its value.
    # This avoids having to search through every order individually.
    # Updating an existing key does not increase the dictionary size.

    print(f"Order 1001: {orders[1001]}")
    print(f"Order 1006: {orders[1006]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Display the customer orders before making any changes.

    print("\nOrders Before Update:")
    print(orders)

    # Customer changes order 1001 from a 49ers Jersey to a 49ers Jacket.
    # Assigning a new value to an existing key replaces the old value.
    # The order number stays the same, so no duplicate order is created.

    orders[1001] = "San Francisco 49ers Jacket"

    # Display the customer orders after the update.

    print("\nOrders After Update:")
    print(orders)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # Display the customer orders before deleting an order.

    print("\nOrders Before Deletion:")
    print(orders)

    # Customer cancels order 1005 for the Boston Red Sox Jersey.
    # The del statement removes the key and its associated value.

    del orders[1005]

    # Display the remaining orders after the cancellation.

    print("\nOrders After Deletion:")
    print(orders)

    # Display the number of orders remaining.

    print(f"\nTotal Orders Remaining: {len(orders)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Look up an order number that does not exist.
    # The get() method returns the default message instead of
    # causing a KeyError when the order number is missing.
    # Using get() is safer than directly accessing a missing key.
    # It allows the website to display a message instead of crashing.

    print("\nEdge Case 1: Lookup Missing Order")
    missing_order = orders.get(9999, "Order Not Found")
    print(f"Order 9999: {missing_order}")

    # Edge Case 2: Attempt to cancel an order that does not exist.
    # The pop() method removes an order if it exists.
    # Providing a default value prevents a KeyError.
    # If the order does nt exist, pop() returns None.
    # The remaining customer orders are not affected.

    print("\nEdge Case 2: Delete Missing Order")
    canceled_order = orders.pop(8888, None)

    if canceled_order is None:
        print("Order 8888 does not exist. No order was canceled.")
    else:
        print(f"Canceled Order 8888: {canceled_order}")

    # Verify that the five remaining orders were not affected.

    print(f"\nTotal Orders Remaining: {len(orders)}")



if __name__ == "__main__":
    main()