from random import *

values = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
    "x", "c", "v", "b", "n", "m", "1", "2", "3", "4",
    "5", "6", "7", "8", "9", "0", "_", "@", "$", "#",
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
    "X", "C", "V", "B", "N", "M"]
     
keep_again = "y"    

while keep_again != "n":
  shuffle(values)
  list = []
  count = int(input("Set the number of values ​​in the password: "))
  count_2 = 0
  while count_2 != count:
    list.append(choice(values))
    count_2 += 1
  split = "".join(list)
  print(f"Your password is: {split}")
  keep_again = input("Next?(y/n): ")
