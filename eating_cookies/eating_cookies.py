#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache={}):
  if n <= 1:
    return 1
  
  if n in cache:
    return cache[n]
  
  combinations = 0
  
  combinations += eating_cookies(n - 1)
  if n > 1:
    combinations += eating_cookies(n - 2)
  if n > 2:
    combinations += eating_cookies(n - 3)
  
  cache[n] = combinations
  return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')