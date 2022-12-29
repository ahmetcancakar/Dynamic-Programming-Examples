# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:07:15 2022

@author: GYRO
"""

def knapsack(n, W, w, r):
  dp = [[0 for j in range(W+1)] for i in range(n+1)]
  for i in range(1, n+1):
    for j in range(0, W+1):
      if w[i-1] <= j:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + r[i-1])
      else:
        dp[i][j] = dp[i-1][j]
  return dp[n][W]

# Test the knapsack function
n = 3
W = 4
w = [2, 3, 1]
r = [31, 47, 14]
print(knapsack(n, W, w, r))
