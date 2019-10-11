#!/usr/bin/python

import sys

def mc(amount, current_denomination, denominations):
  # if amount = 0 return 1
  if amount == 0:
    return 1
  # add combinations of everything:
  # call itself in a loop with good amount - denomination if amound - denomination >= 0
  combinations = 0
  for denomination in denominations:
    new_amount = amount - denomination
    if new_amount >= 0 and denomination <= current_denomination:
      combinations += mc(new_amount, denomination, denominations)
  # return combinations
  return combinations

def making_change(amount, denominations):
  return mc(amount, max(denominations), denominations)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")