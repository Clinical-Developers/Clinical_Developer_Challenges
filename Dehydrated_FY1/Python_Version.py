"""
Clinical Developers Hydration Challenge.

An FY1 working in the heat of summer works out that on his ward rounds he needs to drink at least 750mls of water an hour to stay hydrated [this FY1 has Diabetes Insipidus].

By Stefan Mitrosinovic - The Legend Competition Completer ;)
"""
from math import ceil


def FY1_hydration(time):
  """Print the amount to drink."""
  amount = 750 * time
  amountStr = '{}L'.format(str(ceil(float(amount) / 1000))) if amount > 1000 else '{}ml'.format(str(amount))
  plural = 's' if time > 1 else ''
  print('You need to drink {} in the next {} hour{}'.format(amountStr, time, plural))


print('Please input the number of hours you will be working, to get the amount of water you should drink:')
while True:
  try:
    t = int(input('>'))
    print()
    FY1_hydration(t)
    print()
  except ValueError:
    print('Please input a number:')
