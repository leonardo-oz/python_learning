class Coin:


  def __init__(self,x,y,size):
    self.x=x
    self.y=y
    self.size=size



  def __str__(self):
    return f"size:{self.size},y position:{self.y},x position:{self.x}"

  @property
  def y(self):
    return self._y
  
  @y.setter
  def y(self,y):
    if y < 0:
      raise ValueError("y cannot be negative")
    self._y = y

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self,size):
    if size < 0:
      raise ValueError("size cannot be negative")
    self._size = size


  @property
  def x(self):
    return self._x

  @x.setter
  def x(self,x):
    if x < 0:
      raise ValueError("x cannot be negative")
    self._x = x

  def move_down(self):
    self.y = self.y -1

  def update_pos(self,new_x,new_y):
    self.x=new_x
    self.y=new_y
# End class


def create_2_coins():
  coin1 = Coin(0,50,10)
  coin2 = Coin(45,25,5)
  return coin1, coin2


if __name__ == "__main__":
  c1,c2 = create_2_coins()
  # print(f"c1's size:{c1.size},y position:{c1.y},x position:{c1.x}")
  # print(f"c2's size:{c2.size},y position:{c2.y},x position:{c2.x}")
  print(c1)
  print(c2)
  c2.move_down()
  print(c2)
  c2.move_down()
  print(c2)

  c1.update_pos(20,50)
  print(c1)
  c2.x = 20
  print(c2)


