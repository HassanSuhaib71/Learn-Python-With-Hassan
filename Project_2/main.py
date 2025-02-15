import random

n = random.randint(1,100)
a = -1
gusses = 1
while(a != n):
    gusses += 1
    a = int(input("Guess the Number : "))
    if(a > n):
        print("Lower Number Please.")
    elif(a < n):
        print("Higher Number Please.")

print(f"You have guessed th number {n} correctly in {gusses} attempt.")