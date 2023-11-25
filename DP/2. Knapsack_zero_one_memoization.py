def knapsack_zero_one_memoization(weights,profits,capacity):
    global t
    n=len(profits)
    t = [[-1 for _ in range(capacity+1)] for _ in range(n+1)]

    def knapsack_main(weights,profits,capacity):
        n = len(profits)
        if capacity==0 or n==0:
            return 0
        if t[n][capacity]!= -1:
            return t[n][capacity]

        if weights[n-1]<=capacity:
            t[n][capacity] =  max(profits[n-1]+knapsack_main(weights[:n-1],profits[:n-1],capacity-weights[n-1]), knapsack_main(weights[:n-1],profits[:n-1],capacity))
            return t[n][capacity]
        else:
            t[n][capacity] =  knapsack_main(weights[:n-1],profits[:n-1],capacity)
            return t[n][capacity]
    
    return knapsack_main(weights,profits,capacity)

# weights = [95,4,60,32,23,72,80,62,65,46]
# profits = [55,10,47,5,4,50,8,61,85,87]
# capacity = 269

# weights = [92,4,43,83,84,68,92,82,6,44,32,18,56,83,25,96,70,48,14,58]
# profits = [44,46,90,72,91,40,75,35,8,54,78,40,77,15,61,17,75,29,75,63]
# capacity = 878

# print(knapsack(weights,profits,capacity))
