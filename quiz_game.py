print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
""" print(playing) """

if playing.lower() != "yes":
    quit()
count = 0
print("Okay! Let's play :)")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
    count += 1
else:
    print('Incorrect!')


answer = input("What does PSU stand for? ")
if answer.lower() == "Power supply":
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

print("You got " + str(count) + " questions correct!")
print("You got " + str((count/4) * 100) + "%.")
