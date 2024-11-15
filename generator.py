from random import *
import os

values = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
    "x", "c", "v", "b", "n", "m", "1", "2", "3", "4",
    "5", "6", "7", "8", "9", "0", "_", "@", "$", "#",
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
    "X", "C", "V", "B", "N", "M"]
     
keep_again = "y"
orders = []

def order_of_digitals():
  global count
  global orders
  while count >= 0:
    orders.append(count)
    count -= 1

while keep_again != "n":
  shuffle(values)
  list = []
  count_2 = 0

  try:
    count = int(input("Set the number of values ​​in the password: "))
  except Exception as e:
    print(e)
    print("Error! Please enter digital.")
    keep_again = "n"
    os.sys.exit()

  while count_2 != count:
    list.append(choice(values))
    count_2 += 1

  order_of_digitals()

  print(orders)
  list[choice(orders)] = choice(["_", "@", "$", "#"]) 

  split = "".join(list)
  print(f"Your password is: {split}")
  orders.clear()
  keep_again = input("Next?(y/n): ")