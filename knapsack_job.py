 # 3(a) Knapsack using Greedy

profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

ratio = []
for i in range(len(profit)):
    ratio.append([profit[i] / weight[i], profit[i], weight[i]])

ratio.sort(reverse=True)

total = 0

for item in ratio:
    if capacity >= item[2]:
        capacity = capacity - item[2]
        total = total + item[1]

print("Maximum Profit =", total)



# 3(a) Knapsack using Dynamic Programming

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)

dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(profit[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit =", dp[n][W])


# 3(b) Job Sequencing

jobs = ['A', 'B', 'C', 'D']
deadline = [2, 1, 2, 1]
profit = [100, 19, 27, 25]

for i in range(len(profit)):
    for j in range(i + 1, len(profit)):
        if profit[i] < profit[j]:
            profit[i], profit[j] = profit[j], profit[i]
            deadline[i], deadline[j] = deadline[j], deadline[i]
            jobs[i], jobs[j] = jobs[j], jobs[i]

slot = [''] * max(deadline)

for i in range(len(jobs)):
    for j in range(deadline[i] - 1, -1, -1):
        if slot[j] == '':
            slot[j] = jobs[i]
            break

print("Job Sequence =", slot)



