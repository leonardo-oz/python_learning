

class Student:

  MATH_SCORE_WEIGHT: float = 0.3
  IQ_SCORE_WEIGHT: float = 0.7

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
    return self.math*self.MATH_SCORE_WEIGHT + self.IQ*self.IQ_SCORE_WEIGHT
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
    record: str=input("please enter your name, math score and IQ, press Q to end: \n ")
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



  def compare_name(self,s,name_qry):
    return s.name.lower()== name_qry.lower()
  # end method compare_name 
  

  def find_by_name(self,name_qry):
    qn=list(filter(lambda s: self.compare_name(s,name_qry),self.records))
    if qn:
      return qn
    else:
      return []
    # end if 
  # end method find_by_name




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
   return [s for s in self.records if s.compute() > score]
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


