# Project 1: Password Strength Checker (version1)

# ask user to enter their password 
password = input("enter your password : ")

# we will 'judge' the score of the password for better understanding
score = 0

# adding data... (have'nt learned loops yet)
has_number = (
    "0" in password or
    "1" in password or
    "2" in password or
    "3" in password or
    "4" in password or
    "5" in password or
    "6" in password or
    "7" in password or
    "8" in password or
    "9" in password
)

# adding data...
has_special_character = (
    "!" in password or
    "@" in password or
    "#" in password or
    "$" in password or
    "%" in password or
    "^" in password or
    "&" in password or
    "*" in password or
    "?" in password 
)

# checking if the password of strong or weak
if len(password) >= 8:
    score = score + 1
else :
    print("your password is too short")
    
if has_number:
    score = score + 1
else :
    print("your password does not contain a digit")

if has_special_character:
    score = score + 1
else :
    print("your password does not contain a special character ")
    
if score == 0 or score == 1 :
    print("password strength : WEAK")
elif score == 2 :
    print("password strength : MEDIUM")
else :
    print("password strength : STRONG")