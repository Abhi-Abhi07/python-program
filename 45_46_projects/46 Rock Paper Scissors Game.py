import random

l=["Rock","Paper","scissor"]
global uc
while 1:
    a = int(input('''
        Game Start .......
        1. Yes
        2. No | Exit
        '''))

    if a != 1:
        exit(0)
    print("""
    *****choices are*****
    1.Rock
    2.Paper
    3.scissor
    """)
    ui=int(input("Enter your choice : "))
    if ui==1:
        uc="Rock"
    elif ui==2:
        uc="Paper"
    elif ui==3:
        uc="scissor"

    x = random.choice(l)
    print("Coputer selected : ",x)
    print("Your choice : ",uc)

    if uc==x:
        print("Match Draw")
    elif ((uc=="Rock" and x=="scissor") or (uc=="Paper" and x=="Rock") or (uc=="scissor" and x=="Paper")):
        print("AAP jeet gye")
    elif ((uc=="Rock" and x=="Paper") or (uc=="Paper" and x=="scissor") or (uc=="scissor" and x=="Rock")):
        print("AAP har gye")
    else :
        print("invalid choice")