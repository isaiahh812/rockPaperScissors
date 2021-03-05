import tkinter as tk
import random as r

window = tk.Tk()

window.configure(background = "blue")

def calculateWinner(num):
    playerChoice = choiceAsString(num)
    computerChoice = choiceAsString(r.randrange(0,3))
    message.config(text = f"Computer picked: {computerChoice}")
    if(playerChoice == computerChoice):
        results.config(text = "Welp I can't complain")
    elif (playerChoice == "rock" and computerChoice == "scissors"):
        results.config(text = "Fuck you bitch I'm  a sore loser!!")
    elif(playerChoice == "scissors" and computerChoice == "paper"):
        results.config(text = "Fucking slut I'll kill you!!")
    elif(playerChoice == "paper" and computerChoice == "rock"):
        results.config(text = "You gotta be fucking kidding me!!")
    else:
        results.config(text = "Hehe you fucking suck ass")
def choiceAsString(num):
    print(num)
    if num is 0:
        return "rock"
    elif num is 1:
        return "paper"
    else:
        return "scissors"
greeting = tk.Label(
    window,
    text = "Ready to play;)",
    foreground = "white",
    background = "blue"
)
greeting.grid(
    column = 2
)
message = tk.Label(
    window,
    text = "  ",
    background = "blue",
    foreground = "white"
)
results = tk.Label(
    window,
    text = "   ",
    background= "blue",
    foreground = "white"
)
rock = tk.Button(
    window,
    width = 5,
    text = "Rock",
    command = lambda :calculateWinner(0)
)
rock.grid(
    row = 5,
    column = 1
)
paper = tk.Button(
    window,
    width = 5,
    text = "Paper",
    command = lambda :calculateWinner(1)
)
paper.grid(
    row = 5,
    column = 2
)
scissors = tk.Button(
    window,
    text = "Scissors",
    command = lambda :calculateWinner(2)
)
scissors.grid(
    row = 5,
    column = 3
)

message.grid(
    column = 2
)
results.grid(
    column = 2
)

window.mainloop()