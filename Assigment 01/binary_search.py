def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input("Enter number to search: "))

result = binary_search(numbers, target)
if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")