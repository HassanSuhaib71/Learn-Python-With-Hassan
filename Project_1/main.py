import random


computer = random.choice([-1,0,1])

youstr = input("Enter Your Choice : ")
youdict = {"s":-1, "w":1, "g":0}
reversedict = {-1:"Snake", 1:"Water", 0:"Gun" }

you = youdict[youstr]

print(f"You choose {reversedict[you]} and computer chose {reversedict[computer]}")

if(computer == you):
    print("Its Draw!")
else:

    if(computer == -1 and you == 1):
        print("You Win!")
        
    elif(computer == -1 and you == 0):
        print("You lose!")
        
    elif(computer == 1 and you == -1):
        print("You lose!")
        
    elif(computer == 1 and you == 0):
        print("You Win!")
        
    elif(computer == 0 and you == 1):
        print("You Win!")
        
    elif(computer == 0 and you == -1):
        print("You lose!")
    else:
        print("Something went wrong!")