class Coin:

  number_of_coins_created = 0


  def __init__(self,x,y,size):
    self.x=x
    self.y=y
    self.size=size
    Coin.number_of_coins_created += 1

  @classmethod
  def count_created_coins(cls):
    return cls.number_of_coins_created


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


  @classmethod
  def create_a_coin(cls):
    x = int(input("give initial x postion of a coin: "))
    y = int(input("give initial y position of a coin: "))
    size = int(input("give initial size of the coin: "))
    return cls(x,y,size)

  def __sub__(self, other):
    x=abs(self.x-other.x)
    y=abs(self.y-other.y)
    size=abs(self.size-other.size)
    return Coin(x,y,size)
  def __add__(self, other):
    x=self.x+other.x
    y=self.y+other.y
    size=self.size+other.size
    return Coin(x,y,size)
  
# End class





if __name__ == "__main__":
  c1 = Coin.create_a_coin()
  c2 = Coin.create_a_coin()
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

  print(type(c1))

  added_c=c1+c2
  print(f"addition c{added_c}")
  subtracted_c = c1-c2
  print(f"subtracted c{subtracted_c}")



  print(f"how many coins have created so far: {Coin.count_created_coins()}")

  # c3 = Coin.create_a_coin()

  # print(f"how many coins have created so far: {Coin.count_created_coins()}")
