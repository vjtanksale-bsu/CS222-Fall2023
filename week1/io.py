def main():
  print("Welcome to CS 222")
  firstName = input("Pleae enter your first name: ")
  print("Welcome " + firstName)
  payRate = float(input("Enter hourly pay rate: "))
  hours = float(input("Enter number of hours worked: "))
  print("$ " + str(payRate * hours))
main()