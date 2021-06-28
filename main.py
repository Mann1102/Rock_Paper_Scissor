import random
import context
rock=context.rock
paper=context.paper
scissors=context.scissors
list1=[rock, paper, scissors]
n=int(len(list1))
n1=n
random1=random.randint(0,n1)
Your_choise=int(input("Enter 0 for Rock , 1 for Paper , 2 for Scissor : "))
if (Your_choise == 2) and (random1 == 0):
  print("You selected " + str(Your_choise) + " scissors")
  print(scissors)
  print("Computer selected " + str(random1) + " rock")
  print(rock)
  print("Computer Wins ):")
elif (Your_choise==2) and (random1==1):
  print("You selected " + str(Your_choise) + " scissors")
  print(scissors)
  print("Computer selected " + str(random1) + " paper")
  print(paper)
  print("You Win (:")
elif (Your_choise==2) and (random1==2):
  print("You selected " + str(Your_choise) + " scissors")
  print(scissors)
  print("Computer selected " + str(random1) + " scissors")
  print(scissors)
  print("Match Tied |:")
elif (Your_choise==1) and (random1==0):
  print("You selected " + str(Your_choise) + " paper")
  print(paper)
  print("Computer selected " + str(random1) + " rock")
  print(rock)
  print("You Win (:")
elif (Your_choise==1) and (random1==1):
  print("You selected " + str(Your_choise) + " paper")
  print(paper)
  print("Computer selected " + str(random1) + ' paper')
  print(paper)
  print("Match Tied |:")
elif (Your_choise==1) and (random1==2):
  print("You selected " + str(Your_choise) + ' paper')
  print(paper)
  print("Computer selected " + str(random1) + ' scissors')
  print(scissors)
  print("Computer Win):")
elif (Your_choise==0) and (random1==0):
  print("You selected " + str(Your_choise) + ' rock')
  print(rock)
  print("Computer selected " + str(random1) + ' rock')
  print(rock)
  print("Match Tie |:")
elif (Your_choise==0) and (random1==1):
  print("You selected " + str(Your_choise) + ' rock')
  print(rock)
  print("Computer selected " + str(random1) + ' paper')
  print(paper)
  print("Computer Wins ):")
elif (Your_choise==0) and (random1==2):
  print("You selected " + str(Your_choise) + ' rock')
  print(rock)
  print("Computer selected " + str(random1) + 'scissors')
  print(scissors)
  print("You Wins (:")