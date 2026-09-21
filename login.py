import random
def main():
  a=1
  b=100
  guess(a,b)
  # ok= verify("Cabbage!@#$", max=2)
  # if ok:
  #   print("login succesful MR.Cabbage")
  # else:
  #   print("invalid pass")
# end method main


def verify(password, max=3):
  passed = False
  i=0 
  while i<max:
    words= input("enter pass: ")
    if words==password:
      passed=True
      break
    i+=1
  # end while
  
  return passed
# end method verify





def input_integer():
  # while True:
  #   try:
  #     c_x=int(input("please enter a number: "))
  #   except ValueError:
  #     print("x is not integer")
  #   else:
  #     break
  #   # end try 
  # # end while

  running = True
  while running:
    try:
      x_str = input("guess my number: ")
      x=int(x_str)
    except ValueError:
      print(f"{x_str} is not integer")
    else:
      running=False
    # end try 
  # end while
  return x
# end method
  


def guess(a,b):
  i=0
  s_n=random.randint(a,b)
  x=input_integer()
  while x!=s_n:
    if x > s_n:
      print(f"{x} is bigger than my scret number")
    else:
      print(f"{x} is smaller than my secret number")
    # end if else
    i+=1
    x=input_integer()
  # end while
  i+=1
  print(f"congratulations you have got my secret number {s_n} after {i} times!")
# end method guess







main()

# x=input_integer()
# print(x)