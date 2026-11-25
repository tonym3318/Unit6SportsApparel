
# Unit 6: Python Dictionaries as Hash Tables

## Project Overview

For this assignment, I created an online sports apparel ordering system using a Python dictionary as a hash table. The system tracked customer orders for NFL, MLB, and college jerseys and jackets.

Each customer order was assigned a unique order number as the key, while the apparel description was stored as its associated value.

## Implementation

I implemented the following dictionary operations:

- Inserted six customer orders using unique order numbers.
- Retrieved existing orders using their keys.
- Updated an existing order from a San Francisco 49ers jersey to a jacket.
- Deleted a canceled Boston Red Sox jersey order.
- Tested missing order numbers using get() and pop() to avoid errors.

## Hash Table Performance

Python dictionaries use hashing to store and retrieve key-value pairs efficiently. I learned that collisions occur when different keys map to the same table location. Python handles these collisions internally.

Dictionary lookups typically have an average time complexity of O(1), making them useful for an online ordering system with many customer orders.

## Testing

I ran the program in IntelliJ and verified that all operations completed successfully. The program handled both missing-order edge cases and finished with exit code 0.

## Files

- `Unit6SportsApparel.py` - Python implementation
- `discussion.md` - Unit 6 discussion reflection
