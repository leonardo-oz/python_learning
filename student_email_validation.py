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


def validate_score():
  "input a score and validate with a regular expression"
  pass

if __name__ == "__main__":
  validate_name()
  print("end of program")


