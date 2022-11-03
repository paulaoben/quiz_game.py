print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CSS stand for? ").lower()
if answer == "cascading style sheet":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does JS stand for? ").lower()
if answer == "javascript":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PHP stand for? ").lower()
if answer == "hypertext preprocessor":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 4) * 100) + "%.")
