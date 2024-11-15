orders = []

def order_of_digitals(count):
  count -= 1
  global orders
  while count >= 0:
    orders.append(count)
    count -= 1