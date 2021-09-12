import random
from os import system, name
from gameData import data1
from art import logo , vs
data = data1
#i = int(input("input here"))
def clear(): 
    # for windows 

    if name == 'nt': 

        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 

    else: 

        _ = system('clear')
# length of data1 in gameData.py is 5
def getRandomDict():
    return (data[random.randint(0,len(data))])
A = False
GameOver = False
def check():
    if A["follower_count"] > B["follower_count"]:
        return A
    else :
        return B
def checkchoice(y):
    
    if y==1:
        x=input("Who do u think have mire follower ?A or B\n\n")
    if x=="A":
        return A
    elif x=="B":
        return B 
score= 0
while GameOver== False:
    clear()
    print(logo)
    print(f"Your Current Score is {score}\n\n")
    if A == False:
        A = getRandomDict()
        
    else:
        A = answer
    print (A["name"]+" a "+A["description"]+" From "+A["country"]+"\n\n")
    print(vs)
    B = getRandomDict()
    print (B["name"]+" a "+B["description"]+" From "+B["country"]+"\n\n")
    userchoice = checkchoice(1)
    answer = check()
    if userchoice == answer:
        GameOver = False
        score = score+1
        print("Score + 1")
    else:
        print("Game Stop")
        clear()
        print(logo)
        print(f"Your Final Score is {score}")
        GameOver=True
        