# Programmer: Hershey Marbeda
# Date: 11.11.2024
# Program Description: This program will sort an array of 0s, 1s, and 2s in ascending order.

# Exercise: Sort 0s, 1s, 2s in an Array
# Function to sort the array of 0s, 1s, and 2s
def sort012(arr, n):
    # Initialize the count of 0s, 1s, and 2s
    count0 = 0
    count1 = 0
    count2 = 0

    # Count the number of 0s, 1s, and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1

    # Update the array with the sorted values
    i = 0
    while count0 > 0:
        arr[i] = 0
        i += 1
        count0 -= 1

    while count1 > 0:
        arr[i] = 1
        i += 1
        count1 -= 1

    while count2 > 0:
        arr[i] = 2
        i += 1
        count2 -= 1
        
    return arr

# Main function
if __name__ == "__main__":
    # Test case 1
    arr1 = [0, 1, 2, 0, 1, 2]
    n1 = len(arr1)
    print("\nExerise #1","\nTest case 1:")
    print("Original array:", arr1)
    print("Sorted array:", sort012(arr1, n1))

    # Test case 2
    arr2 = [2, 1, 0, 0, 1, 2]
    n2 = len(arr2)
    print("\nTest case 2:")
    print("Original array:", arr2)
    print("Sorted array:", sort012(arr2, n2))

# Exercise: Given a sorted arr and an integer k, find the position(0-based indexing) at which
# is present in the array using Binary Search.
def binary_search(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Main function
if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k1 = 5
    print("\nExercise #2:","\nTest case 1:")
    print("Array:", arr1)
    print("Element", k1, "is present at index:", binary_search(arr1, k1))

    # Test case 2
    arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    k2 = 70
    print("\nTest case 2:")
    print("Array:", arr2)
    print("Element", k2, "is present at index:", binary_search(arr2, k2), "\n")
    

