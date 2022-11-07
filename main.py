cprs = ""
import os
import json
import requests
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


print()
usernameInput = input(colored("🔎 Scan dit sygesikringsbevis... Eller tast ind => ", "blue"))
print()

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
