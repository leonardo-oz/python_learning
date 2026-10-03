import argparse
from smart_kid_prg_v7 import StudentDBMgr,Student

parser=argparse.ArgumentParser(description="A program that allows you to create a database on students")
parser.add_argument("-F",default="output/records.txt",help="File that contains all the info on what you did.")
args=parser.parse_args()


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
      name_qry= input("please insert a name: ")
      qs = db_mgr.find_by_name(name_qry)
      if qs:
        print(f"{name_qry} is found")
        db_mgr.display(qs)
      else:
        print(f"{name_qry} NOT found")
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

def test_create_list_of_students():

    names = ["John", "Alice", "Bob", "Eve"]
    math_scores = [85, 92, 78, 90]
    IQ_scores = [110, 120, 105, 115]

    students=[Student(names[i], math_scores[i], IQ_scores[i]) for i in range(len(names))]
    for i,student in enumerate(students,1):
        print(i,student)
    # end for 

    # # students: list[dict] = [{"name": names[i], "math_score": math_scores[i], "IQ": IQ_scores[i]} for i in range(len(names))]
    # # for s in students:
    # #     print(f"{s['name']}, {s['math_score']}, {s['IQ']}, score: {s['math_score']*Student.MATH_SCORE_WEIGHT + s['IQ']*Student.IQ_SCORE_WEIGHT}")

    # students_dict: dict = {names[i]: {"math_score": math_scores[i], "IQ": IQ_scores[i]} for i in range(len(names))}
    # # for s in students_dict:
    # #     print(f"{s},{students_dict[s]['math_score']},{students_dict[s]['IQ']}")
    # for name, scores in students_dict.items():
    #     print(f"{name}, {scores['math_score']}, {scores['IQ']}, score: {scores['math_score']*Student.MATH_SCORE_WEIGHT + scores['IQ']*Student.IQ_SCORE_WEIGHT}")

if __name__=="__main__":
  test_create_list_of_students()
#   main()









