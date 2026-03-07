# Demonstrating List Sorting and Math Operations

sales = [25, 30, 5, 7, 15]

# Sorting in ascending order
sales.sort()
print(f"Sorted: {sales}")

# Reversing the list
sales.reverse()
print(f"Reversed: {sales}")

# Calculating the sum
total_sales = sum(sales)
print(f"Total Sum: {total_sales}")

# Note: You can also combine types, though sorting may then fail
sales.extend(['Amar', 'Tomar'])
print(f"Final mixed list: {sales}")