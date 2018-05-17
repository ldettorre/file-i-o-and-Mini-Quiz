import re


print("             ***MENU***")
print("Choose an option,\n 1)Ask a question.\n 2)Add a question.\n 3)End game.")

score = 0
mode = int(input("Choose an option:"))
if mode == 1:
    print("You chose ask a question")
    f = open('questions.txt')
    lines= f.read().lower().split("\n")
    f.close
    for line in lines:
        question,answer = line.split("|")
        guess = input(question)
        if guess == answer:
            print("Correct")
            score = score + 1
            print(score)
        else:
            print("Wrong")
        
        
        
elif mode == 2:
    userQ = input("What is your question?")
    f = open('questions.txt', 'a')
    f.write(userQ)
    f.close()
    
    

elif mode == 3: 
    print("       ***Game Over***")