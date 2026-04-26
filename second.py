 # a) Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [5, 2, 9, 1, 7]
merge_sort(arr)
print("Sorted array using Merge Sort:", arr)


# b) Quick Sort

def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        p = i + 1

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

arr = [5, 2, 9, 1, 7]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array using Quick Sort:", arr)


# c) Binary Search

arr = [1, 2, 5, 7, 9]
key = 7

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Element found at index", mid)
else:
    print("Element not found")


# d) Min-Max using Divide and Conquer

def min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    min1, max1 = min_max(arr, low, mid)
    min2, max2 = min_max(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)

arr = [5, 2, 9, 1, 7]
minimum, maximum = min_max(arr, 0, len(arr) - 1)

print("Minimum =", minimum)
print("Maximum =", maximum)
