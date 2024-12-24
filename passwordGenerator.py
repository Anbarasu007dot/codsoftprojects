import random
import string
def generate_password(len):
    char=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(char)for _ in range(len))
    return password
print("welcome to password generator !")
try:
    len=int(input("enter the length of password you want(min 6 characters) :"))
    if len<6:
        print("the length of the password should be minimumm of 6 characters !")
    else:
        password=generate_password(len)
        print("the generated strong password is",password)
except ValueError:
    print("please enter a valid number as length")
