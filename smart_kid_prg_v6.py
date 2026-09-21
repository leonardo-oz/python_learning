import csv
def main():
  database_file="output/records.txt"

  menu_str = "\n\n\n>>>>smart kid program<<<< \npress 1 Add records \npress 2 Display records \n\
press 3 find best student\npress 4 to end\npress 5 to find record by name\npress 6 to find longest name\npress 7 to find records has score > input score:\npress 8 to update a persons math score"

  print(menu_str)
  choice=input()
  while choice!= "4":
    if choice== "1":
      print("==== Start Adding Records ============")
      proccess(database_file)
    elif choice == "2":
      order_by_dic = {1:"name", 2:"math_score",3:"IQ",4:"name_length"}
      order_by_choice=int(input("Do you want to order by\n1.name\n2.math_score\n3.IQ\n4.name_length "))
      order_by = order_by_dic.get(order_by_choice,"name")
      ascending_str=input("??ascending Y or N??  ")
      ascending=(ascending_str=="Y")
      print("==== Start Displaying Records ============")
      # student_records = load(database_file)
      student_records = load_csv(database_file)
      # display(student_records)
      display_by_order(student_records,order_by,ascending)
    elif choice =="3":
      print("==== Start Finding Best Student============")
      records = load(database_file)
      best_record = find_highest_score(records)
      print(best_record["name"],best_record["math_score"],best_record["IQ"],compute(best_record["math_score"],best_record["IQ"]))
    elif choice== "5":
      print("====starting to find student=========")
      records= load(database_file)
      names_qry= input("please insert a name: ")
      find(records,names_qry )
    elif choice=="6":
      print("=======finding longest name==========")
      records=load(database_file)
      find_longest_name(records)
    elif choice=="7":
      score= int(input("please enter a qualification score: "))
      print(f"=======starting displaying students final score > {score}: ============")
      records= load(database_file)
      gt_records = qry_gt(records, score)
      display(gt_records)
    elif choice=="8":
      name=input("please enter the person's score name you want to change ")
      math_score= input(f"please enter the new score for the {name} ")
      print("========updating record==============")
      update_mark(name,math_score,database_file)
    else:
      print(" wrong choice choose to type between 1-8")
    # end if 
    print(menu_str)
    choice=input()
  # end while
# end method main

  # proccess(database_file)
  # names,maths, IQs = display(database_file)
  # max_score_pos, max_final_score = find_highest_score(names,maths,IQs)
  # print(f"best student: {names[max_score_pos]}, \
  #       math score: {maths[max_score_pos]}, \
  #       IQ{IQs[max_score_pos]},\
  #       final score: {max_final_score}") \
        
# end method

def proccess(database_file):
  with open(database_file, "a") as writer:
    record=input("please enter your name, math score and IQ, press Q to end: ")
    while record != "Q":
      words=record.strip().split()
      name= words[0]
      math= int(words[1])
      IQ= int(words[2])
      writer.write(f"{name}, {math}, {IQ}\n")
      record=input("please enter your name, math score and IQ: \n")
    # end while
  # end with
  writer.close()
  return 
# end proccess method


def display_by_order(student_records, order_by="name", ascending=True):
  if order_by == "name":
    for record in sorted(student_records,key=lambda student: student["name"],reverse=not ascending):
      print(f"{record['name']},{record['math_score']},{record['IQ']}")
    # end for loop
  elif order_by == "math_score":
      for record in sorted(student_records,key=lambda student: student["math_score"],reverse=not ascending):
        print(f"{record['name']},{record['math_score']},{record['IQ']}")
      # end for loop
  elif order_by == "IQ":
    for record in sorted(student_records,key=lambda student: student["IQ"],reverse=not ascending):
      print(f"{record['name']},{record['math_score']},{record['IQ']}")
    # end for loop
  elif order_by == "name_length":
    for record in sorted(student_records,key=lambda student: len(student["name"]),reverse=not ascending):
      print(f"{record['name']},{record['math_score']},{record['IQ']}")
    # end for loop
  # end if
# end method display_by_order 

def display(student_records):
  
  for i in range(len(student_records)):
    student = student_records[i]
    math = student["math_score"]
    IQ= student["IQ"]
    name= student["name"]
    score=compute(math, IQ)
    print(f"{name}, {math}, {IQ}, {score:.2f}")
    # end for i
  # end with
  return 
# end display method


def compute(maths, IQs):
  return maths*0.3 + IQs*0.7
# end method compute


def load_csv(database_file):
  records = []
  with open(database_file) as file:
    reader=csv.reader(file)
    for name,math_score,IQ in reader:
      records.append({"name":name,"math_score":int(math_score),"IQ":int(IQ)})
    # end for loop
  # end with
  return records
# end method load_csv
    
    
def load(database_file):
  records=[]

  with open(database_file, "r") as reader:
    line=reader.readline()
    while len(line) != 0:
     
      letters= line.strip().split(',')
      # print(letters)
      name= letters[0].title()
      math= int(letters[1])
      IQ= int(letters[2])
      # record["name"]=name
      # record["math_score"] = math
      # record["IQ"] = IQ
      record = {"name":name,"math_score":math, "IQ":IQ}
      records.append(record)
      line=reader.readline()
    # end while
    
  return records
# end display method


def find_highest_score(records):
  # initialize
  max_num=0
  max_record = {}
  for i in range(len(records)):
    record=records[i]
    math=record["math_score"]
    IQ= record["IQ"]
    final_score_i= compute(math, IQ) 
    if final_score_i > max_num:
      # print(final_score_i)
      max_num =final_score_i
      max_record = record
    # end if
  # end for i
  return max_record
# method highest score

def find(records, names_qry):
  found_record = None
  pos_i=-1
  for i in range(len(records)):
    record= records[i]
    name=record["name"]
    if name.lower()== names_qry.lower():
      found_record = record
      pos_i=i
      break
    # end if
  # end for i 
  if found_record != None:
    print(found_record["name"], found_record["math_score"],found_record["IQ"], compute(found_record["math_score"], found_record["IQ"]))
  else:
    print("name not found")
  # ennd if
  return pos_i
# end method 

def find_longest_name(records):
  l_name= ""
  longest_record=None
  for i in range(len(records)):
    rrecord= records[i]
    name= rrecord["name"]
    if len(name)>len(l_name):
      l_name= name
      longest_record= rrecord
    # end if
  # end for i


  if longest_record != None:
    print(longest_record["name"], longest_record["math_score"], longest_record["IQ"])
  else:
    print("no records")
# end method find_longest_name

def qry_gt(records, score):
  qualifies= []
  for i in range(len(records)):
    math= records[i]["math_score"]
    IQ= records[i]["IQ"]
    result= compute(math, IQ)
    if result > score:
      qualifies.append(records[i])
    # end if else
  # end for i
  return qualifies
# end method quarry


def update_mark(s_name, math_score,database_file):
  records=load(database_file)
  pos_i=find(records,s_name)
  if pos_i !=-1:
    records[pos_i]["math_score"]=math_score
  else:
    print(f"{s_name} not found")
  # end if 
  write(records, 'output/junk_2.csv')
# end method update mark

  

def write(data,database_file):
  with open(database_file,"w") as writer:
    for d in data:
      out_str = f"{d['name']},{d['math_score']},{d['IQ']} \n"
      writer.write(out_str)
    # end for d
  # end with
  
# end method write









if __name__=="__main__":
  main()





