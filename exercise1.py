import time
#USing a function to ask a questions
def kbc_game():
    questions=[
        ("Which is the largest ocean in the world?","C",["A. Atlantic Ocean" , "B. Indian Ocean" , "C. Pacific Ocean" , "D. Arctic Ocean"],1000),
        ("Who was the first President of the United States?","B",["A. Thomas Jefferson","B. George Washington","C. Abraham Lincoln","D. John Adams"],5000),
        ("Who is known as the father of the Internet?","B",["A. Tim Berners-Lee","B. Vint Cerf","C. Alan Turing","D. Steve Jobs"],10000),
        ("Which is the smallest continent in the world?","D",["A.Africa","b.Asia","C.Europe","D.Australia"],20000),
        ("Which sport is known as the 'gentleman's game'?","C",["A. Football","B. Tennis","C. Cricket","D. Golf"],50000)
    ]
    total=0
    print("Welcome to KBC - Kaun Banega Crorepati!")
    for i, (question, correct_answer, options, prize) in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        for option in options:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D or 'Q' to quit): ").upper()
        
        if user_answer == 'Q':
            print("You chose to quit the game.")
            break
        
        if user_answer == correct_answer:
            total+= prize
            print(f"Correct! You have won ₹{prize}.")
            print(f"Total winnings: ₹{total}")
        else:
            print("Incorrect answer! Game over.")
            total= 0
            break
    
    print(f"\nYou are taking home ₹{total}. Thanks for playing KBC!")

time.sleep(1)
kbc_game()
