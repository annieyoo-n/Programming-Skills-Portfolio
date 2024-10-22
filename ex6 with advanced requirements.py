
#Exercise 6: Brute Force Attack:
    
password = 12345    #Enter the correct password
while password == 12345:  #Using the loop until correct password is entered 
    password_typed = int(input("Enter the password: "))
    if password_typed==12345:
        print("Correct Password. Access Granted")
        break
    else:
        print("IncorrectPassword. Try again!")
        

#Optional Requirements:

password = 12345
maximum_attempts = 5 
while maximum_attempts>0:
    password_typed = int(input("Enter the password: "))
    if password_typed==password:
        print("Correct Password.")  #if correct password entered
        break
    else:
        maximum_attempts= maximum_attempts-1
        if maximum_attempts>0:  #if incorrect password entered
            print(f"Incorrect, you have {maximum_attempts} attempts left.")
        else:
            print("Maximum number of attempts reached, Authorities have been alerted.")
            break
if maximum_attempts ==0:    #if password still incorrect then print the final message 
    print("Access denied")
    
    
    