import os
import json
import requests
import webbrowser
from termcolor import colored


# We are fetching the cprs from cdn.hypll.org
url = "https://cdn.hypll.org/services/programing/cprnr-system/data.json"
res = requests.get(url)
cprs = json.loads(res.text)["cprsNrs"]


password = ""

# Checking if the password.txt file exists
if os.path.exists("password.txt"):
    with open("password.txt", "r") as f:
       password = f.read()
else:
    password = "000000"

# Functions
    # UPDATE password
    def update_password():
        newPassword = input(colored("Skriv din nye adgangskode: ", "cyan"))


    
# When the user is logged run this function
def user_loggedIn():
  print()
  print(colored("❓ Hvad vil du gøre nu?", "cyan"))
  print()
  print(colored("1. Opdater din adgangskode", "grey"))
  print(colored("2. Giv en stjerne på Github", "grey"))
  print(colored("3. Exit programmet", "grey"))
  print()

  choice = int(input("Skriv dit valg: "))
  ################################################################
  if choice == 1:
      print()
      newPassword = input(colored("🔑 Skriv din nye adgangskode: ", "grey"))
      confirmPassword = input(colored("🚨 Bekræft venligst den nye adgangskode: ", "grey"))
      confirmChangePassword = input(colored("❓ Er du sikker på du vil ændre adgangskoden: (ja/nej) ", "grey"))

                
      if (len(newPassword) != 6):
          print()
          print(colored("❌ Adgangskoden skal være/må kun være 6 cifre!", "red"))
          print()
          return
      elif (confirmPassword != newPassword):
          print()
          print(colored("❌ Adgangkoden matcher ikke!", "red"))
          print()
          return
      elif (confirmPassword == password):
          print()
          print(colored("❌ Den adgangskode du skrev, er din nuværende. Vælg en anden eller slut handlingen...", "red"))
          print()
      else:
        if (confirmChangePassword.lower != "ja" or confirmChangePassword.lower != "j"):
            print()
            print(colored("✅ Du opdaterede din adgangskode!", "green"))

            # we are updaing the password.txt file
            with open("password.txt", "w") as f:
                f.write(newPassword)

            print()
        else:
            print()
            exit(colored("✅ Du sluttede handlingen...", "green"))
    ################################################################
  elif choice == 2:
        webbrowser.open("https://github.com/lassv/cpr-nr-system")
        print(colored("Tak for din støtte ❤️", "blue"))
    ################################################################
  elif choice == 3:
      print()
      exit(colored("✅ Programmet blev lukket", "green"))
  else:
      print()
      print(colored("❌ Invalid choice", "red"))
      print()
            
      
    
################################################################
print()
usernameInput = input(colored("🔎 Scan dit sygesikringsbevis... Eller tast ind => ", "blue"))
print()

################################################################
if usernameInput not in cprs:
    print()
    print(colored("❌ Du er ikke med i listen af godkendte cpr numere!", "red"))
    print()
else:
    print()
    typePassword = input(colored("🔑 Skriv Password: ", "grey"))
    print()

    if (typePassword == password):
       if os.path.exists("password.txt"):
           with open("password.txt", "r") as f:
               if (typePassword == password):
                   print()
                   print(colored("✅ Du er nu logget in i systemet!", "green"))
                   user_loggedIn()
                   print()
       else:
           print(colored("🚨 Du skal nu lave en ny kode...", "cyan"))
           enterNewPassWord = input(colored("🔏 Skriv den nye adgagns kode for at få adgang: ", "magenta"))

           if (len(enterNewPassWord) == 6):
               with open("password.txt", "w") as f:
                 f.write(enterNewPassWord)
                 print()
                 print(colored("✅ Din adgangskode er nu gemt!", "green"))
                 print()
           else:
               print()
               print(colored("🚨 Adgangskoden må/skal være 6 cifre... Prøv igen.", "yellow"))  
               print() 
    else:
        print()
        print(colored("❌ Forkert adgangskode...", "red"))
        print()