import re



def validate_email():
  email=input("what's your student email? ")

  if re.search(r"^\d{6}@abpat\.qld\.edu\.au",email):
    print("valid student email")
  else:
    print("invalid student email")
  # end if
  return 


def validate_name():
  name = input("What is your name: ").strip()
  if matches := re.search(r"^([a-z]+) +([a-z]+)$",name,re.IGNORECASE):
    print(f"Hello, {matches.group(1)},{matches.group(2)}")
  return

def validate_gender():
  gender=input("what is your gender: ")
  if matches := re.search(r"^(f|m|female|male)$",gender,re.IGNORECASE):
    return matches.group(1)
  else:
    return None
  # end if
# end method
def validate_score():
  score=-1
  "input a score between 0 to 99 and validate with a regular expression"
  score_str = input("What is your score:").strip()
  if matches := re.search(r"^(\d|\d\d)$",score_str):
    score= int(score_str)
  # end if
  return score
# end method
  

if __name__ == "__main__":
  # validate_name()
  gender=validate_gender()
  if gender:
    print(f"your gender is: {gender}")
  else: # None case
    print("gender is not available")
  # end if
  print("end of program")


