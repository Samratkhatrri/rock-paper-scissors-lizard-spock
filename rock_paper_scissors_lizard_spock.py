import random

# alright lets set up this game now

# rock beats scissors  1>3
# scissors beat paper 3>2
#paper beats rock  2>1



print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️  (Scissors)")
print("4) 🦎 (Lizard)")
print("5) 🖖 (Spock)")

while True:
    try:
        num = int(input("Pick a Number: "))
        if num in [1, 2, 3, 4, 5]:
            break
        else:
            print("Invalid number, Please enter 1, 2, 3, 4 or 5.")
    except:
        print("That's not a number! Try again.")

player = num
computer = random.randint(1, 5)

print()

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
elif player == 4:
    print("You chose: 🦎")
else:
     print("You chose: 🖖")

if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌️")
elif computer == 4:
    print("CPU chose: 🦎")
else:
     print("CPU chose: 🖖")
    
'''    
Scissors cut Paper. 3>2
Paper covers Rock. 2>1
Rock crushes Lizard. 1>4
Lizard poisons Spock. 4>5
Spock smashes Scissors. 5>3
Scissors beat Lizard. 3>4
Lizard eats Paper. 4> 2
Paper disproves Spock. 2> 5
Spock vaporizes Rock. 5> 1
Rock breaks Scissors 1 >3
'''
    
# The results 
if (player == 3 and computer == 2) or \
   (player == 2 and computer == 1) or \
   (player == 1 and computer == 4) or \
   (player == 4 and computer == 5) or \
   (player == 5 and computer == 3) or \
   (player == 3 and computer == 4) or \
   (player == 4 and computer == 2) or \
   (player == 2 and computer == 5) or \
   (player == 5 and computer == 1) or \
   (player == 1 and computer == 3):
    print("The Player won!")
elif (player ==computer):
    print("Its a tie!")
else:
    print("The Computer won!")   




