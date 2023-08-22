def main():
  print("Welcome to CS 222")
  #firstName = input("Please enter your first name: ")
  #print("Welcome " + firstName)
  #payRate = float(input("Enter hourly pay rate: "))
  #hours = float(input("Enter number of hours worked: "))
  #print("$ " + str(payRate * hours))
  average = float(input("Please enter student's average score: "))
  if average >= 60:
    print("Pass")
  else:
    print("Fail")
  if average >= 90:
    print("A")
  elif average >= 80:
    print("B")
  elif average >= 70:
    print("C")
  elif average >= 60:
    print("D")
  else:
    print("F")

  for counter in range(5):
    print(counter)
main()