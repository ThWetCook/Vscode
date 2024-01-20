print("Welcome to this quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does HDMI stand for? ")
if answer.lower() == "high definition multimedia interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GSM stand for? ")
if answer.lower() == "global system for mobile communications":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")