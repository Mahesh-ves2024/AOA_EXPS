# a) Insertion Sort

arr = [5, 2, 9, 1, 7]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

print("Sorted array using Insertion Sort:", arr)



# b) Selection Sort

arr = [5, 2, 9, 1, 7]

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array using Selection Sort:", arr)





1) Sorting Algorithms
a) Insertion Sort
Idea: Build the sorted part one element at a time.
Take one element and insert it into the correct position in the already sorted left side.
How it works:
Start from the 2nd element.
Compare it with elements before it.
Shift bigger elements right.
Place the key in the correct position.
Example:
Array: 5 2 4 6 1 3
Take 2, insert before 5 → 2 5 4 6 1 3
Take 4, insert between 2 and 5 → 2 4 5 6 1 3
Take 6 → already correct
Take 1 → 1 2 4 5 6 3
Take 3 → 1 2 3 4 5 6
Time complexity:
Best: O(n) when already sorted
Average/Worst: O(n^2)
Properties:
Stable
In-place
Good for small or nearly sorted data
Viva line:
“Insertion sort grows a sorted section gradually by inserting each element into its correct place.”
b) Selection Sort
Idea: Repeatedly find the minimum element and place it at the beginning.
How it works:
Find smallest from unsorted part.
Swap it with the first unsorted element.
Repeat.
Example:
Array: 64 25 12 22 11
Smallest is 11 → 11 25 12 22 64
Smallest in remaining is 12 → 11 12 25 22 64
Then 22 → 11 12 22 25 64
Then 25 → sorted
Time complexity:
Best/Average/Worst: O(n^2)
Properties:
Not stable by default
In-place
Does minimum number of swaps
Viva line:
“Selection sort repeatedly selects the smallest element from the unsorted part and moves it to the front.”
2) Divide and Conquer Algorithms
a) Merge Sort
Idea: Divide the array into halves, sort both halves, then merge them.
Steps:
Split array into two halves.
Recursively sort each half.
Merge two sorted halves.
Example:
Array: 38 27 43 3 9 82 10
Split:
38 27 43 3
9 82 10
Further split and sort:
38 27 → 27 38
43 3 → 3 43
merge → 3 27 38 43
9 82 → 9 82
merge with 10 → 9 10 82
Final merge:
3 9 10 27 38 43 82
Time complexity: O(n log n) in all cases
Space: O(n)
Properties:
Stable
Not in-place generally
Good for large data
Viva line:
“Merge sort divides the array into halves and merges sorted halves back together.”
b) Quick Sort
Idea: Pick a pivot, place it in correct position, then sort left and right parts.
Steps:
Choose pivot.
Partition array:
smaller elements left
larger elements right
Recursively apply to subarrays.
Example:
Array: 10 80 30 90 40 50 70
Choose pivot 50
After partition:
left: 10 30 40
pivot: 50
right: 80 90 70
Then sort left and right.
Time complexity:
Best/Average: O(n log n)
Worst: O(n^2) when pivot is poor
Properties:
Usually in-place
Not stable
Very fast in practice
Viva line:
“Quick sort partitions the array around a pivot and recursively sorts both sides.”
c) Binary Search
Idea: Search in a sorted array by repeatedly dividing the search range in half.
Steps:
Check middle element.
If target is equal, found.
If target is smaller, search left half.
If target is larger, search right half.
Example:
Array: 2 5 8 12 16 23 38 56 72 91
Find 23
Middle = 16
23 > 16 → search right half
Middle of right half = 56
23 < 56 → search left half
Middle = 23 → found
Time complexity: O(log n)
Requirement: Array must be sorted.
Viva line:
“Binary search works only on sorted data and reduces the search space by half each time.”
d) Min-Max Problem
Idea: Find both minimum and maximum in an array efficiently.
Simple method:
Scan all elements once
Update min and max
Divide and conquer method:
Divide array into two halves
Find min and max of each half
Combine results
Example:
Array: 3 5 1 9 2
Min = 1
Max = 9
Time complexity:
Simple method: O(n)
D&C method: also O(n) but fewer comparisons
Viva line:
“Min-max problem finds the smallest and largest element, often using divide and conquer for efficiency.”
3) Greedy and Dynamic Programming
a) Knapsack Problem
There are two forms:
1. Fractional Knapsack (Greedy)
You can take fraction of an item.
Idea: Choose items with highest value/weight ratio first.
Example:
Capacity = 50
Items:
Item1: value 60, weight 10 → ratio 6
Item2: value 100, weight 20 → ratio 5
Item3: value 120, weight 30 → ratio 4
Pick:
Item1 fully
Item2 fully
Remaining capacity = 20
Take 20/30 of Item3
Use: Greedy works here.
2. 0/1 Knapsack (Dynamic Programming)
You can either take an item fully or not take it.
Idea: Use a table dp[i][w] for max value using first i items and weight w.
Example:
Capacity = 5 Items:
(weight 1, value 1)
(weight 2, value 6)
(weight 4, value 18)
Choose best combination without exceeding capacity.
Use: Greedy does not always work for 0/1 knapsack.
Time complexity:
Greedy fractional: O(n log n)
DP 0/1: O(nW) where W is capacity
Viva line:
“Fractional knapsack uses greedy, while 0/1 knapsack uses dynamic programming.”
b) Job Sequencing Problem
Idea: Schedule jobs to maximize profit, where each job takes 1 unit time and has a deadline.
Method:
Sort jobs by profit in descending order.
Place each job in the latest free slot before its deadline.
Example:
Jobs:
J1: deadline 2, profit 100
J2: deadline 1, profit 19
J3: deadline 2, profit 27
J4: deadline 1, profit 25
J5: deadline 3, profit 15
Sort by profit:
J1, J3, J4, J2, J5
Schedule:
Slot 2 → J1
Slot 1 → J3
Slot 3 → J5
Goal: maximum profit
Viva line:
“Job sequencing is a greedy algorithm that schedules highest-profit jobs first within deadlines.”
4) Dijkstra’s Algorithm
Purpose: Find shortest path from one source to all vertices in a weighted graph with non-negative weights.
How it works:
Start from source
Mark distance of source = 0, others = infinity
Pick unvisited vertex with smallest distance
Relax all its neighbors
Repeat
Example:
If source A connects to B=4, C=1, and C connects to B=2, then:
A to C = 1
A to B via C = 1 + 2 = 3, which is better than 4
Important:
Does not work with negative edge weights.
Time complexity:
Using array: O(V^2)
Using priority queue: O((V+E) log V)
Viva line:
“Dijkstra finds shortest paths from one source using greedy selection of the closest unvisited vertex.”
5) Prim’s and Kruskal’s Algorithm
Both are used for Minimum Spanning Tree (MST).
MST
A spanning tree that connects all vertices with minimum total edge weight.
a) Prim’s Algorithm
Idea: Start from one vertex and grow the MST by adding the minimum edge connecting tree to outside vertex.
Steps:
Choose any starting vertex
Keep adding the smallest edge that connects visited and unvisited vertices
Viva line:
“Prim’s algorithm grows the tree vertex by vertex.”
b) Kruskal’s Algorithm
Idea: Sort all edges by weight and keep adding the smallest edge that does not form a cycle.
Steps:
Sort edges
Pick smallest edge
If it forms a cycle, skip it
Continue until MST has V-1 edges
Viva line:
“Kruskal’s algorithm grows the MST edge by edge.”
Difference:
Prim: vertex-based
Kruskal: edge-based
Prim is better for dense graphs
Kruskal is good for sparse graphs


6) Bellman-Ford and Floyd-Warshall
a) Bellman-Ford Algorithm
Purpose: Shortest path from one source to all vertices.
Key feature: Works even with negative edge weights.
How it works:
Relax all edges V-1 times
One more relaxation checks for negative cycle
Example:
If path keeps reducing after V-1 iterations, there is a negative cycle.
Time complexity: O(VE)
Viva line:
“Bellman-Ford finds shortest paths even with negative weights and can detect negative cycles.”
b) Floyd-Warshall Algorithm
Purpose: Shortest paths between all pairs of vertices.
Idea: Dynamic programming.
How it works:
Try every vertex as intermediate
Update distance if going through that vertex gives shorter path
Example:
If A -> B = 5, B -> C = 2, and A -> C = 10, then via B:
A -> B -> C = 7
so update A -> C = 7
Time complexity: O(V^3)
Viva line:
“Floyd-Warshall computes shortest paths for all pairs using intermediate vertices.”
7) Longest Common Subsequence (LCS)
Idea: Find the longest sequence that appears in both strings in the same order, not necessarily continuous.
Example:
String1 = ABCBDAB
String2 = BDCAB
Common subsequence can be BCAB or BDAB
Length = 4
Important:
Subsequence is not substring.
DP logic:
If characters match, dp[i][j] = 1 + dp[i-1][j-1]
Else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
Use: file comparison, bioinformatics, diff tools
Viva line:
“LCS finds the longest ordered sequence common to two strings using dynamic programming.”
8) Backtracking: Sum of Subsets and Graph Coloring
a) Sum of Subsets
Idea: Find subsets whose sum equals a target.
Example:
Set = {5, 10, 12, 13, 15, 18}
Target = 30
Possible subsets:
{12, 18}
{5, 12, 13}
{5, 10, 15}
Method:
Try including or excluding each element.
If sum exceeds target, backtrack.
Viva line:
“Sum of subsets uses backtracking to explore all possible combinations efficiently.”
b) Graph Coloring
Idea: Assign colors to vertices so that adjacent vertices have different colors.
Example:
For a triangle graph, 3 colors are needed.
Method:
Try assigning a color to a vertex
Check if safe
Move to next vertex
Backtrack if no color works
Applications:
Map coloring, scheduling, register allocation
Viva line:
“Graph coloring uses backtracking to assign colors without conflict.”
9) Euclidean Distance and Jaccard Distance
a) Euclidean Distance
Meaning: Straight-line distance between two points.
Formula:
For n dimensions:
Example:
Between (3,4) and (0,0):
Use: clustering, similarity in geometry and ML
b) Jaccard Distance
Meaning: Measures how dissimilar two sets are.
Formula:

Example:
A = {1,2,3,4}
B = {3,4,5}
Intersection = {3,4} → 2
Union = {1,2,3,4,5} → 5
Similarity = 2/5 = 0.4
Distance = 1 - 0.4 = 0.6
Use: text comparison, recommendation, binary data
Viva line:
“Euclidean distance measures geometric distance, while Jaccard distance measures set dissimilarity.”
10) Bloom’s Filter
Idea: A fast space-saving structure to test whether an element is probably in a set.
Important:
Can give false positives
Never gives false negatives
How it works:
Use a bit array, initially all 0
Use multiple hash functions
Insert an element by setting bits at hash positions
Search by checking those bits
Example:
Bit array size = 10
Insert A → bits 2, 5 set
Insert B → bits 1, 5 set
To check C:
If required bits are not all 1 → definitely not present
If all are 1 → maybe present
Use: database, cache, web filters, networking
Viva line:
“Bloom filter is a probabilistic structure that quickly checks membership using hash functions and bit arrays.”

    
