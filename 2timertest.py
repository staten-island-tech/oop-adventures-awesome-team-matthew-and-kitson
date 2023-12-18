import random
import time

def block():
  t_time = random.randint(1, 5)
  t1 = time.time()
  while True:
    user_input = input("Enter 'Block': ")
    t2 = time.time()
    t3 = t2 - t1
    if user_input == "Block" and t3<=t_time:
      print("Blocked!")
      break
    if t3 >= t_time:
      print("Failed to Block")
      break

block()