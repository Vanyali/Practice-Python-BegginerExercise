import random

# Awroken

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    print(f"Is it {NUMBER} ?")
    ANSWER = input()
    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
        NUMBER -= random.randint(1, 4)
    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
        NUMBER += random.randint(1, 4)
    elif ANSWER.lower() == "no":
        print("Higher or lower?")
        ANSWER = input()
        if ANSWER.lower() == "higher":
            NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
            NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
        if TRY < 2:
            print (f"Yes! It only took me {TRY} try!")
        elif TRY < 2 and TRY < 10:
            print (f"Pretty well for a robot, {TRY} tries.")
        else:
            print (f"That's so bad, {TRY} tries.")
        RUNNING = False
    TRY += 1
    
print ("Thanks for the game!")