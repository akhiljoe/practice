# # You are climbing a staircase. It takes n steps to reach the top.

# # Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# # Example 1:

# # Input: n = 2
# # Output: 2
# # Explanation: There are two ways to climb to the top.
# # 1. 1 step + 1 step
# # 2. 2 steps


# # Example 2:

# # Input: n = 3
# # Output: 3
# # Explanation: There are three ways to climb to the top.
# # 1. 1 step + 1 step + 1 step
# # 2. 1 step + 2 steps
# # 3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        current_sum = 0
        for i in range(0,n+1):
            if (n-i)%2==0:
                one = i
                two = int((n-i)/2)
                current_sum = current_sum + int((self.factorial(one+two))/(self.factorial(one)*self.factorial(two)))
        return current_sum
    
    def factorial(self,n):
        if n<=1:
            return 1
        else:
            return n * self.factorial(n-1)
    
if __name__ == "__main__":
    solution = Solution()
    print("\n")
    n = 998
    print(f"for {n} --> ",solution.climbStairs(n))
    
    