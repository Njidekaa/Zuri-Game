import random

print("Welcome To The Game")
print("Rock, Paper, Scissors")
print("R stands for Rock, P stands for Paper, S stands for Scissors")

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["R", "P", "S"]
computerHand = random.choice(possibleHands)

def checkforWinner(playerHand, computerHand):
    if(playerHand == "R" and computerHand == "P"):
        print("Sorry you Lost")
        return "Cpu"
    elif(playerHand == "R" and computerHand == "S"):
        print("Congrats, You win!")  
        return "Player"
    elif(playerHand == "P" and computerHand == "R"):
        print("Congrats, You win!") 
        return "Player"
    elif(playerHand == "P" and computerHand == "S"):
        print("Sorry you Lost")  
        return "cpu"
    elif(playerHand == "S" and computerHand == "R"):
        print("Sorry you Lost") 
        return "cpu"
    elif(playerHand == "S" and computerHand == "P"):
        print("Congrats, You win!")  
        return "Player"
    else:
        print("It is a Tie")
        return "Tie"

while(playerScore != 3 and cpuScore != 3):
    
    while True:
        playerHand = input("Pick a Hand, R, P, or S: ")
        if(playerHand == "R" or playerHand == "P" or playerHand == "S"):
            break
        else:
            print("Invalid Input, Try again!")

    print("Your Hand: ", playerHand)  
    print("Cpu Hand: ", computerHand)  
    result = checkforWinner(playerHand, computerHand)
    if(result == "Player"):
        playerScore += 1
    elif(result == "Cpu"):
        cpuScore += 1
    else:
        tieScore += 1
    print("Your Score: ", playerScore, "Cpu: ", cpuScore, "Tie: ", tieScore)           

  