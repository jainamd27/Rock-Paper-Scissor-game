import random
import os
from time import sleep

print("welcome to stone paper scissor game\n")
print("you have 7 chances to win the game\n")
print("enter from 1,2,3")
print('1 for rock, 2 for paper, 3 for scissor')

player_points = 0 #points for player
ai_points = 0 #points for ai
chances = 7

while chances >0:
    ai_choice = random.randint(1,3)
    
    player_choice = input("your turn: ")
    try:
        player_choice = int(player_choice)
        
    except Exception as e:
        e = "invalid input\n"
        print(e)
        
    chances -=1

    if ai_choice == 1 and player_choice == 2:
        print("ai wins 1 point\n")
        ai_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == 2 and player_choice == 3:
        print("you win 1 point\n")
        player_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == 1 and player_choice == 3:
        print("ai wins 1 point\n")
        ai_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == 3 and player_choice == 2:
        print("ai wins 1 point\n")
        ai_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == 3 and player_choice == 1:
        print("you win 1 point\n")
        player_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == 2 and player_choice == 1:
        print("you win 1 point\n")
        player_points += 1
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
        
    elif ai_choice == player_choice:
        print("tie\n")
        print(f"ai points: {ai_points}\n")
        print(f"your points: {player_points}\n")
         
    print(f"you have {chances} chances")
    
if chances < 0:
    print('game over!')
    
print('results')
if ai_points > player_points:
    print('you lose!')
    
elif ai_points == player_points:
    print("it's a tie")
    
else:
    print('congratulations! you win!')
    
print(f"ai points: {ai_points}")
print(f"your points: {player_points}")

print("Screen will now be cleared in 4 Seconds")

sleep(4)

os.system('clear')
