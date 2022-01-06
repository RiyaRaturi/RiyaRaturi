import math
import random
def check_guess(user_guess,correct_guess):
    if user_guess==correct_guess:
       return True

def get_userguess():
    guess=int(input('Enter your guess[1-50]:'))
    return guess

def play_menu():
    print("----Guess the number----")
    print("1.Start")
    print("2.Exit")

def hints(correct_guess,user_guess):
    if user_guess%2!=0 and correct_guess%2==0:
        return "Hint: Correct guess is a multiple of 5(try again)"
    elif correct_guess <user_guess:
        return "Hint: Your guess is Too high(try again)"
    elif correct_guess > user_guess:
        return "Hint: Your guess is Too low(try again)"

def main():
    play_menu()
    print(18*"-*")
    choice=input("Enter your choice:")
    correct_guess=random.randint(1,50)
    score=0
    if choice=='1':
        play='y'
        while play=='y':
            user_guess=get_userguess()
            success=check_guess(user_guess,correct_guess)
            if success == True:
                print("Perfect!!!")
                score+=5
                print("You gain 5 points...\nScore:",score)
                correct_guess=random.randint(1,50)
            else:
                score-=1
                print("You loose 1 point...\nScore:",score)
                print(hints(correct_guess,user_guess))
            print(41*"_")
            play=input("do you want to repeat the task....(yes/no):")
            print(41*"_")
    elif choice=='2':
        print("close game....")
        exit()
main()

