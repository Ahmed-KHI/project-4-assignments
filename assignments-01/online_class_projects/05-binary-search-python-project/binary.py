def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

# Example Usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input("Enter number to search: "))
result = binary_search(arr, target)

if result != -1:
    print(f"✅ Number {target} found at index {result}")
else:
    print(f"❌ Number {target} not found in the list")