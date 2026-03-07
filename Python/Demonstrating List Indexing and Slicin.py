# Demonstrating List Indexing and Slicing in Python

nums = [20, 15, 25, 12, 13]

# Accessing by index
print(f"First element: {nums[0]}")  # 20
print(f"Last element: {nums[-1]}")   # 13

# Slicing: Getting elements from index 2 to the end
# Output: [25, 12, 13]
print(f"Slicing [2:]: {nums[2:]}")

# Handling IndexErrors
try:
    print(nums[5])
except IndexError as e:
    print(f"Caught an expected error: {e}")