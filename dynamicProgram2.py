# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:14:28 2022

@author: GYRO
"""
def min_cost_plan(t, n, p, m, q, c, d, h, f, i, S):
  for i in range(12):         
      if t == T:
        # Base case: the minimum cost for the last month is simply the cost of the inventory
        return str(i[t] * S[t])
      else:
        # Recursive case: the minimum cost for the current month is the minimum of the following options:
        # - Keep the current number of workers engaged in production
        cost_keep = c[t] * n * p + min_cost_plan(t+1, n, p, m, q, c, d, h, f, i, S)
        # - Leave some workers idle
        cost_idle = d[t] * (n - p) + (1 - q) * (n - p) * min_cost_plan(t+1, n - p, p, m, q, c, d, h, f, i, S)
        # - Hire additional workers
        cost_hire = h[t] * (S[t] - (1 - m) * p * n) + c[t] * (S[t] - (1 - m) * p * n) + min_cost_plan(t+1, S[t] - (1 - m) * p * n, p, m, q, c, d, h, f, i, S)
        # - Fire some workers
        cost_fire = f[t] * n + d[t] * (n - S[t] / (1 - m)) + (1 - q) * (n - S[t] / (1 - m)) * min_cost_plan(t+1, n - S[t] / (1 - m), p, m, q, c, d, h, f, i, S)
        t+=1
        return min(cost_keep, cost_idle, cost_hire, cost_fire)

# Define the input variables
T = 12 # Number of months to plan for
n = 100 # Initial number of workers
p = 50 # Productivity rate of each worker, in bottles of perfume per month
m = 5 # Loss rate of stored bottles, in percentage
q = 3 # Attrition rate of idle workers, in percentage
c = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210] # Unit cost for workers engaged in production for each month
d = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105] # Unit cost for workers left idle for each month
h = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420] # Cost for hiring workers for each month
f = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210] # Cost for firing workers for each month
i = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Cost for the inventory of bottles at the end of each month
S = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100] # Expected sales for each month

# Find the minimum cost employment and production plan
min_cost = min_cost_plan(0, n, p, m, q, c, d, h, f, i, S)
print(min_cost) # This will print the minimum cost for the employment and production plan for the next 12 months

   

