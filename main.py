cprs = ["1910055999"]

usernameInput = input("Scan dit sygesikringsbevis... ")

password = "000000"

if usernameInput not in cprs:
    print("Du er ikke med i listen af godkendte cpr numere!")
else:

    passwordInput = input("Hvad er adgangskoden? ")

    if (passwordInput == password):
        print("Du skal nu lave en ny kode...")
        newPassword = input("Skriv den nye kode:")
        password = newPassword
        
        if (len(password) == 6):
            ## Printe den nye kode...
            print("Koden blev ændret til " + password)

            enterNewPassWord = input("Skriv den nye adgagns kode for at få adgang:")

            if (enterNewPassWord == password):
                print("Du er blevet godkendt!")
            else:
                print("Du er logget ud!")

        else:
            print("Koden skal være 6 cifre")
        
    else:
        print("Forkert adgangskode...")