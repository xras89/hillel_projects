year = int(input("Which year do you want to check? (between 1900 and 1000000) "))

if 1900 <= year <= 1000000:

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(f"{year} is Leap year")
      else:
        print(f"{year} is not Leap year")
    else:
      print(f"{year} is Leap year")
  else:
    print(f"{year} is not Leap year")

else: print("You entered the wrong year, try again.")