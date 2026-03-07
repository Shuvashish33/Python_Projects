# Demonstrating dynamic list modifications

names = ['Nazla', 'Joy', 'jacob']

# Inserting at specific positions
names.insert(2, 77)         # Insert 77 at index 2
names.insert(0, 'sharma')    # Insert 'sharma' at the start
print(f"After inserts: {names}")

# Removing specific values
names.remove('jacob')
print(f"After removing 'jacob': {names}")

# Deleting slices
del names[2:]
print(f"After deleting from index 2 onwards: {names}")

# Adding multiple items
names.extend(['A', 'B'])
print(f"After extend: {names}")

# Concatenation
more_data = names + ['Jacob', 13.4]
print(f"Concatenated list: {more_data}")