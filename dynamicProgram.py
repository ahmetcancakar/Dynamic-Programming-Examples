# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:44:28 2022

@author: GYRO
"""

def find_optimal_allocations(votes):
  # Initialize the dp array with -1
  dp = [[-1 for j in range(6)] for i in range(6)]

  # Set the base case
  dp[0][0] = 0

  # Set the values for i = 6 and j = 6
  dp[6][6] = 0

  # Iterate through all possible values of i and j
  for i in range(1, 7):
    for j in range(i+1):
      # Initialize the maximum value to the base case
      max_votes = dp[i-1][0]

      # Find the maximum estimated increase in votes
      # by assigning i-j volunteers to the other faculties
      for k in range(1, i):
        max_votes = max(max_votes, dp[i-1][k] + votes[j][k])

      # Store the maximum value in the dp array
      dp[i][j] = max_votes

  # Find the maximum estimated increase in votes
  max_votes = dp[6][0]
  for j in range(1, 7):
    max_votes = max(max_votes, dp[6][j])

  # Print all the optimal allocations
  for i in range(7):
    for j in range(7):
      if dp[i][j] == max_votes:
        print(f"{i} volunteers in the Management faculty, {j} volunteers in the other faculties")

# Example usage
votes =[
    [0, 0, 0, 0, 0],
    [1, 4, 7, 5, 6],
    [2, 9, 11, 10, 11],
    [3, 15, 16, 15, 14],
    [4, 18, 18, 18, 16],
    [5, 22, 20, 21, 17],
    [6, 24, 21, 22, 18]]
   
find_optimal_allocations(votes)