def knapsack_zero_one(weights,profits,capacity):
    n = len(profits)
    if capacity==0 or n==0:
        return 0
    if weights[n-1]<=capacity:
        return max(profits[n-1]+knapsack_zero_one(weights[:n-1],profits[:n-1],capacity-weights[n-1]), knapsack_zero_one(weights[:n-1],profits[:n-1],capacity))
    else:
        return knapsack_zero_one(weights[:n-1],profits[:n-1],capacity)
  
# weights = [2,3,4,5]
# profits = [3,4,5,6]
# capacity=5

# print(knapsack(weights,profits,capacity))



