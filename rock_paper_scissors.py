import random

# alright lets set up this game now

# rock beats scissors  1>3
# scissors beat paper 3>2
#paper beats rock  2>1

print("====================")
print("Rock Paper Scissors")
print("====================")

print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️  (Scissors)")

while True:
    try:
        num = int(input("Pick a Number: "))
        if num in [1, 2, 3]:
            break
        else:
            print("Invalid number, Please enter 1, 2, or 3.")
    except:
        print("That's not a number! Try again.")
player = num
computer = random.randint(1, 3)

if (player == 1 and computer == 3):
    print("You chose: ✊")
    print("CPU chose: ✌️")
    print("The Player won!")
elif (player == 3 and computer == 2):
    print("You chose: ✌️")
    print("CPU chose: ✋")
    print("The Player won!")
elif (player == 2 and computer == 3):
    print("You chose: ✋")
    print("CPU chose: ✌️")
    print("The Player won!")
elif( player == computer):
    print("Its a Tie!")
else:
    print("The computer won!")   




