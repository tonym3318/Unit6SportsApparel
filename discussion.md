
# Unit 6 Discussion: Dictionaries as Hash Tables – Tony Marquez

## Reflection

For this assignment, I learned how Python dictionaries use key-value pairs to manage information. I created an online sports apparel ordering system where each order number was a unique key and the jersey or jacket purchased was its associated value. This helped me understand how to insert, look up, update, and delete customer orders.

One challenge was understanding which dictionary methods to use, especially when handling orders that did not exist. I used `get()` to look up missing orders and `pop()` to safely remove them. Running the program in IntelliJ helped me verify that the operations worked correctly without affecting other orders.

Hash tables use a hashing function to determine where information is stored, allowing faster lookups without searching every entry. Collisions occur when different keys map to the same location. Python handles these collisions internally, although too many can reduce performance. Hash tables typically provide an average lookup time of O(1), compared to O(n) for a linear search. This would be useful for an online apparel website handling thousands of orders during busy shopping periods.
