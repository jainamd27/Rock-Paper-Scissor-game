import random

print("welcome to stone paper scissor game\n")
print("you have 7 chances to win the game\n")
print("enter from 1,2,3")
print('1 for rock, 2 for paper, 3 for scissor')

p_p = 0 #points for player
p_ai = 0 #points for ai
chances = 7

d_ai = random.randint(1,3)

while chances >0:
    d_p = input("your turn: ")
    try:
        d_p = int(d_p)
        
    except Exception as e:
        e = "invalid input\n"
        print(e)
        
    chances -=1

    if d_ai == 1 and d_p == 2:
        print("ai wins 1 point\n")
        p_ai += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == 2 and d_p == 3:
        print("you win 1 point\n")
        p_p += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == 1 and d_p == 3:
        print("ai wins 1 point\n")
        p_ai += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == 3 and d_p == 2:
        print("ai wins 1 point\n")
        p_ai += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == 3 and d_p == 1:
        print("you win 1 point\n")
        p_p += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == 2 and d_p == 1:
        print("you win 1 point\n")
        p_p += 1
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
        
    elif d_ai == d_p:
        print("tie\n")
        print(f"ai points: {p_ai}\n")
        print(f"your points: {p_p}\n")
         
    print(f"you have {chances} chances")
    
if chances < 0:
    print('game over!')
    
print('results')
if p_ai > p_p:
    print('you lose!')
    
elif p_ai == p_p:
    print("it's a tie")
    
else:
    print('congratulations! you win!')
    
print(f"ai points: {p_ai}")
print(f"your points: {p_p}")