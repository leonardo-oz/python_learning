class Coin:
  def __init__(self,x,y,size):
    self.x=x
    self.y=y
    self.size=size
# End class


def create_2_coins():
  coin1 = Coin(0,50,10)
  coin2 = Coin(45,25,5)
  return coin1, coin2


if __name__ == "__main__":
  c1,c2 = create_2_coins()
  print(f"c1's size:{c1.size},y position:{c1.y},x position:{c1.x}")
  print(f"c2's size:{c2.size},y position:{c2.y},x position:{c2.x}")

