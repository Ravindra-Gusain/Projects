import random 
l=["rock","paper","scissor"]
(''' 
 Rock vs Paper ---> Paper wins
 Paper vs Scissor ---> Scissor wins
 Rock vs Scissor ---> Rock wins
 ''')

while True:
    Ucount=0
    Ccount=0
    uc=int(input('''
    Game Start....
    1 Yes
    2 No|Exit'''))
    if uc==1:
        for a in range(1,6):
            UserInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper'''))
            if UserInput==1:
                uchoice="rock"
            elif UserInput==2:
                uchoice="scissor"
            elif UserInput==3:
                uchoice="paper"
            else:
                print("Invalid Input")
            Cchoice=random.choice(l)
            if uchoice==Cchoice:
                print("Game Draw")
                print("User Choice:---",uchoice)
                print("Computer choice:---",Cchoice)
                Ucount=Ucount+1
                Ccount=Ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor")or (uchoice=="paper"and Cchoice=="rock")or (uchoice=="scissor"and Cchoice=="paper"):
                print("User wins")
                print("User Choice:---",uchoice)
                print("Computer choice:---",Cchoice)
                Ucount=Ucount+2
            else:
                print("Computer Wins")
                print("User Choice:---",uchoice)
                print("Computer choice:---",Cchoice)
                Ccount=Ccount+2
        if Ucount==Ccount:
            print("Final Game Draw")
            print("Total count of User:---",Ucount)
            print("Total count of computer:---",Ccount)
        elif Ucount>Ccount:
            print("Final Game Wins by User")
            print("Total count of User:---",Ucount)
            print("Total count of computer:---",Ccount)
        else:
            print("Final Game Wins by Computer")
            print("Total count of User:---",Ucount)
            print("Total count of computer:---",Ccount)
    else:
        break

