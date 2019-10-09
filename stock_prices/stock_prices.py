#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # compare earilier and later prices
  # return the greatest profit

  maxProfit = -9999
  for idx, firstPrice in enumerate(prices):
    for secondPriceIdx in range(idx + 1, len(prices)):
      secondPrice = prices[secondPriceIdx]
      newProfit = secondPrice - firstPrice
      if newProfit > maxProfit:
        maxProfit = newProfit

  return maxProfit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))