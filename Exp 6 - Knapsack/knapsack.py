def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

   
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]



def knapsack_top_down(weights, values, capacity):
    n = len(weights)


    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(i, w):
      
        if i == 0 or w == 0:
            return 0


        if memo[i][w] != -1:
            return memo[i][w]


        if weights[i - 1] <= w:
            memo[i][w] = max(
                values[i - 1] + solve(i - 1, w - weights[i - 1]),
                solve(i - 1, w)
            )
        else:
            memo[i][w] = solve(i - 1, w)

        return memo[i][w]

    return solve(n, capacity)



weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

bottom_up_result = knapsack_bottom_up(weights, values, capacity)
top_down_result = knapsack_top_down(weights, values, capacity)

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)

print("Maximum value using Bottom-Up:", bottom_up_result)
print("Maximum value using Top-Down:", top_down_result)