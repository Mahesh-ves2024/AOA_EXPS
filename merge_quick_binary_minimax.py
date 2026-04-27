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




'''advantages complexity
1. Insertion Sort
Time Complexity:
Best: O(n)
Avg/Worst: O(n²)
Advantages:
Simple
Works well for small data
Efficient for nearly sorted arrays
Disadvantages:
Slow for large data
Not suitable for big inputs
🔹 2. Selection Sort
Time Complexity:
Best/Avg/Worst: O(n²)
Advantages:
Simple
Minimum swaps
Disadvantages:
Always slow (no best case improvement)
Not efficient for large data
🔹 3. Merge Sort
Time Complexity:
Best/Avg/Worst: O(n log n)
Advantages:
Stable
Works well for large datasets
Disadvantages:
Extra memory required
Slower than quick sort in practice
🔹 4. Quick Sort
Time Complexity:
Best/Avg: O(n log n)
Worst: O(n²)
Advantages:
Very fast in practice
In-place (no extra memory)
Disadvantages:
Worst case is slow
Not stable
🔹 5. Binary Search
Time Complexity:
Best: O(1)
Avg/Worst: O(log n)
Advantages:
Very fast
Efficient for large data
Disadvantages:
Works only on sorted arrays
🔹 6. Min-Max
Time Complexity:
Best/Avg/Worst: O(n)
Advantages:
Simple
Fewer comparisons using D&C
Disadvantages:
Not much improvement over linear scan
🔹 7. Fractional Knapsack (Greedy)
Time Complexity:
All cases: O(n log n)
Advantages:
Optimal solution
Fast
Disadvantages:
Only works for fractional case
🔹 8. 0/1 Knapsack (DP)
Time Complexity:
All cases: O(nW)
Advantages:
Gives optimal solution
Disadvantages:
High memory usage
Slow for large capacity
🔹 9. Job Sequencing
Time Complexity:
Best/Avg: O(n log n)
Worst: O(n²)
Advantages:
Maximizes profit
Simple greedy approach
Disadvantages:
Works only for specific conditions
🔹 10. Dijkstra
Time Complexity:
O(V²) or O(E log V)
Advantages:
Efficient shortest path
Faster than Bellman-Ford
Disadvantages:
Cannot handle negative weights
🔹 11. Prim’s Algorithm
Time Complexity:
O(V²) or O(E log V)
Advantages:
Good for dense graphs
Disadvantages:
Slower for sparse graphs
🔹 12. Kruskal Algorithm
Time Complexity:
O(E log E)
Advantages:
Simple
Good for sparse graphs
Disadvantages:
Needs cycle detection
🔹 13. Bellman-Ford
Time Complexity:
O(VE)
Advantages:
Handles negative weights
Detects negative cycles
Disadvantages:
Slower than Dijkstra
🔹 14. Floyd-Warshall
Time Complexity:
O(V³)
Advantages:
Finds all-pairs shortest path
Disadvantages:
Very slow for large graphs
🔹 15. LCS
Time Complexity:
O(mn)
Advantages:
Accurate result using DP
Disadvantages:
High time and space
🔹 16. Sum of Subsets
Time Complexity:
O(2^n)
Advantages:
Finds all solutions
Disadvantages:
Very slow (exponential)
🔹 17. Graph Coloring
Time Complexity:
O(m^n)
Advantages:
Solves constraint problems
Disadvantages:
Very slow
🔹 18. Euclidean Distance
Time Complexity:
O(n)
Advantages:
Simple
Fast
Disadvantages:
Not suitable for categorical data
🔹 19. Jaccard Distance
Time Complexity:
O(n)
Advantages:
Good for set comparison
Disadvantages:
Ignores frequency of elements
🔹 20. Bloom Filter
Time Complexity:
Insert/Search: O(k)
Advantages:
Very fast
Memory efficient
Disadvantages:
False positives possible
Cannot delete easily'''
