import random
import string

n = int(input("Enter length of the password : "))
print("Select complexity of the password according to below options.")
print("1.Easy")
print("2.medium")
print("3.Hard")
k = int(input("Enter your option : "))
p = []
final_password = ""

def generate_pass(n):
    easy_pass = string.ascii_letters
    medium_pass = string.ascii_letters+string.digits
    hard_pass = string.ascii_letters+string.digits+string.punctuation
    count = 1
    while n>=count:
        if k==1:
            password = random.choice(easy_pass)
            count +=1
        elif k==2:
            password = random.choice(medium_pass)
            count +=1
        elif k==3:
            password = random.choice(hard_pass)
            count +=1
        else:
            print("please enter in available options.")
        
        p.append(password)

generate_pass(n)
for i in p:
    final_password += i
print("New generated password : ",final_password)
