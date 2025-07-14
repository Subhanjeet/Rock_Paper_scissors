import random
choices = ['r','p','s']
emoji = {'r':'🪨','p':'📃','s':'✂️'}

while True:
    
    user_choice = input("Rock, Paper, scissors (r,p,s):").lower()
    if user_choice not in choices:
        print("Invalid Choices!!")
        continue
    
    computer_choice = random.choice(choices)
   
    print(f"Your choice {emoji[user_choice]}")
    print(f"Computer choice {emoji[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie")
    elif (user_choice == 'r' and computer_choice == 's') or(user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print("YOU WIN!!")
    else:
        print("YOU LOSS!!")
    should_continue = input("Continue ?(y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing")
        break

    