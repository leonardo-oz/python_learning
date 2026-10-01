import argparse

parser=argparse.ArgumentParser(description="A program that allows you to create a database on students")
parser.add_argument("-F",default="output/records.txt",help="File that contains all the info on what you did.")
args=parser.parse_args()



class Student:

  def __init__(self,name: str, math: int, IQ: int) -> None:
    self._name = name
    self._math = math
    self._IQ = IQ


  @property
  def name(self) -> str:
    return self._name


  @name.setter
  def name(self,name: str):
    self._name=name

  @property
  def math(self) -> int:
    return self._math

  @math.setter
  def math(self,math: int):
    if self._math < 0 or self._math > 100:
      raise ValueError("math score must be between 0 and 100")
    self._math=math

  @property
  def IQ(self) -> int:
    return self._IQ

  @IQ.setter
  def IQ(self,IQ: int):
    if self._IQ < 0 or self._IQ > 300:
      raise ValueError("IQ score must be between 0 and 300")
    self._IQ=IQ
  

    
  def compute(self) -> float:
    return self.math*0.3 + self.IQ*0.7
  # end method compute

  def __str__(self) -> str:
    return f"{self.name},{self.math},{self.IQ},{self.compute()}"


class StudentDBMgr: 
  MAX_RECORDS: int = 10
  def __init__(self,database_file:str) -> None:
    """Constructor of StudentDBMgr Class """
    if database_file is None:
      self.records: list = []
    else:
      self.database_file: str =database_file
      self.load()
    
  



  def load(self):
    self.records = []
    with open(self.database_file, "r") as reader:
      line: str=reader.readline()
      while len(line) != 0:
      
        letters: str= line.strip().split(',')
        name: str= letters[0].title()
        math: int= int(letters[1])
        IQ: int= int(letters[2])
        self.records.append(Student(name,math,IQ))
        line=reader.readline()
      # end while
      
  # end display method

  def add_a_record(self):
    MAX_RECOREDS_REACHED_ERROR_MSG: str = "too many student records"
    if len(self.records) >= self.MAX_RECORDS:
      raise ValueError(MAX_RECOREDS_REACHED_ERROR_MSG)
    # end if 
    record: str=input("please enter your name, math score and IQ, press Q to end: ")
    while record != "Q":
      words=record.strip().split()
      name= words[0]
      math= int(words[1])
      IQ= int(words[2])
      new_student: object = Student(name,math,IQ)

      self.records.append(new_student)    
      if len(self.records) >= self.MAX_RECORDS:
        raise ValueError(MAX_RECOREDS_REACHED_ERROR_MSG)

      record=input("please enter your name, math score and IQ: \n")
    # end while
    self.write_all()

    # return 
  # end proccess method


  def display_by_order(self, order_by="name", ascending=True):
    if order_by == "name":
      for record in sorted(self.records,key=lambda student: student.name,reverse=not ascending):
        print(record)
      # end for loop
    elif order_by == "math_score":
        for record in sorted(self.records,key=lambda student: student.math,reverse=not ascending):
          print(record)
        # end for loop
    elif order_by == "IQ":
      for record in sorted(self.records,key=lambda student: student.IQ,reverse=not ascending):
        print(record)
      # end for loop
    elif order_by == "name_length":
      for record in sorted(self.records,key=lambda student: len(student.name),reverse=not ascending):
        print(record)
      # end for loop
    else:
      self.display(self.records)
    # end if
  # end method display_by_order

  def display(self,gt_records:list):
  
    for s in gt_records:
      print(s)
    return 
  # end display method
  
  def find_highest_score(self) -> str:
    # initialize
    max_num: int=0
    best_student = None
    for i in range(len(self.records)):
      s: str = self.records[i]
      final_score_i: int=s.compute()
      if final_score_i > max_num:
        # print(final_score_i)
        max_num =final_score_i
        best_student = s
      # end if
    # end for i
    return best_student
  # method highest score

  def find(self, names_qry: str) -> int:
    found_record = None
    pos_i: int=-1
    for i in range(len(self.records)):
      record= self.records[i]
      name: str=record.name
      if name.lower()== names_qry.lower():
        found_record = record
        pos_i=i
        break
      # end if
    # end for i 
    if found_record != None:
      print(f"{record} is found")
    else:
      print("name not found")
    # ennd if
    return pos_i
  # end method 

  def find_longest_name(self):
    l_name: str= ""
    longest_record=None
    for i in range(len(self.records)):
      rrecord= self.records[i]
      name= rrecord.name
      if len(name)>len(l_name):
        l_name= name
        longest_record= rrecord
      # end if
    # end for i


    if longest_record != None:
      print(longest_record)
    else:
      print("no records")
  # end method find_longest_name

  def qry_gt(self, score:int) -> list:
    qualifies: list= []
    for i in range(len(self.records)):
      record: str=self.records[i]
      s: int=record.compute()
      result=s
      if result > score:
        qualifies.append(record)
      # end if else
    # end for i
    return qualifies
  # end method quarry


  def update_mark(self,s_name: str, math_score: int):
    self.load()
    pos_i=self.find(s_name)
    if pos_i !=-1:
      self.records[pos_i].math=math_score
    else:
      print(f"{s_name} not found")
    # end if 
    self.write_all()
  # end method update mark

  
  def write(self,student: str ):
    with open(self.database_file,"a") as writer:
      writer.write(f"{student.name}, {student.math}, {student.IQ}\n")

  # End method

  def write_all(self):
    with open(self.database_file,"w") as writer:
      for d in self.records:
        # out_str = f"{d['name']},{d['math_score']},{d['IQ']} \n"
        out_str = f"{d.name},{d.math},{d.IQ}\n"
        writer.write(out_str)
      # end for d
    # end with
    
  # end method write


def main():
  # database_file="output/records.txt"
  database_file = args.F
  menu_str = "\n\n\n>>>>smart kid program<<<< \npress 1 Add records \npress 2 Display records \n\
press 3 find best student\npress 4 to end\npress 5 to find record by name\npress 6 to find longest name\npress 7 to find records has score > input score:\npress 8 to update a persons math score"

  print(menu_str)
  db_mgr=StudentDBMgr(database_file)
  choice=input()
  while choice!= "4":
    if choice== "1":
      print("==== Start Adding Records ============")
      try:
        db_mgr.add_a_record()
      except ValueError  as e:
        print(f"caught error {e}")
        db_mgr.write_all()
    elif choice == "2":
      order_by_dic: dict = {1:"name", 2:"math_score",3:"IQ",4:"name_length"}
      order_by_choice: int=int(input("Do you want to order by\n1.name\n2.math_score\n3.IQ\n4.name_length "))
      order_by = order_by_dic.get(order_by_choice,"name")
      ascending_str: str=input("??ascending Y or N??  ")
      ascending: bool=(ascending_str=="Y")
      db_mgr.load()
      print(f"==== Start Displaying {len(db_mgr.records)} Records ============")
      db_mgr.display_by_order(order_by,ascending)
    elif choice =="3":
      print("==== Start Finding Best Student============")
      db_mgr.load()
      best_record = db_mgr.find_highest_score()
      print(best_record)
    elif choice== "5":
      print("====starting to find student=========")
      db_mgr.load()
      names_qry= input("please insert a name: ")
      db_mgr.find(names_qry )
    elif choice=="6":
      print("=======finding longest name==========")
      db_mgr.load()
      db_mgr.find_longest_name()
    elif choice=="7":
      score= int(input("please enter a qualification score: "))
      print(f"=======starting displaying students final score > {score}: ============")
      db_mgr.load()
      gt_records = db_mgr.qry_gt(score)
      db_mgr.display(gt_records)
    elif choice=="8":
      name=input("please enter the person's score name you want to change ")
      math_score= input(f"please enter the new score for the {name} ")
      print("========updating record==============")
      db_mgr.update_mark(name,math_score)
    elif choice == "9":
      # create a pie chart of marks distribution
      pass
    else:
      print(" wrong choice choose to type between 1-8")
    # end if 
    print(menu_str)
    choice=input()
  # end while
# end method main






if __name__=="__main__":
  main()









