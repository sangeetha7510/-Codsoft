import random

print("Welcome to rock, paper, scissors game")
print("In this game you have to choose any one of the above things.")
print("Winner will be announced according to their choices")

user_points = 0
comp_points = 0

while True:
    user_choice=input("please enter your choice : ")
    choice_options=["rock","paper","scissors"]
    comp_choice=random.choice(choice_options)
    print("yours choice : "+user_choice)
    print("computer choice : "+comp_choice)

    if(user_choice == comp_choice):
        print("Both are in tie")
        comp_points +=1
        user_points +=1
        
    elif (user_choice == "rock" and comp_choice == "paper"):
        print("sorry! computer is the winner, computer got the point")
        comp_points +=1

    elif(user_choice == "rock" and comp_choice == "scissors"):
        print("congratulations! you are the winner, you got a point")
        user_points +=1
        
    elif (user_choice == "paper" and comp_choice == "scissors"):
        print("sorry! computer is the winner, computer got the point")
        comp_points +=1
        
    elif(user_choice == "paper" and comp_choice == "rock"):
        print("congratulations! you are the winner, you got a point")
        user_points +=1
        
    elif (user_choice == "scissors" and comp_choice == "rock"):
        print("sorry! computer is the winner, computer got the point")
        comp_points +=1
        
    elif(user_choice == "scissors" and comp_choice == "paper"):
        print("congratulations! you are the winner, you got a point")
        user_points +=1
        
    user_intrest=input("If you want to continue please type 'yes' otherwise type 'no'.")
    if (user_intrest == "yes"):
        continue
    elif(user_intrest == "no"):
        break
    
print("final scores are : ")
print("users score : "+str(user_points))
print("computer score : "+str(comp_points))
