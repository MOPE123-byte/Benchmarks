# Name: Mohmmad Parvez
# Collaborators: No
# Notes: Attempted to convert to fraction

# Write your program here

from fractions import Fraction

print("Welcome to my history trivia game!")
print("Answer each question by typing A, B, C, or D.")

questions = ("What U.S president served two non consectutive terms?: ",
             "Which U.S president was responsible for dropping the atomic bomb on japan?: ",
             "Who was the shortest U.S president to ever serve in office?: ")

options = (("A. Grover Cleveland ","B. Woodrow Wilson ","C. Calvin Coolidge ","D. Richard Nixon "),
           ("A. Gerald Ford ","B. John Adams ","C. Dwight Eisenhower ","D. Harry Truman "),
           ("A. Abraham Lincoln ","B. James Madison ","C. William Mckinley ","D. Zachary Taylor "))

answers = ("A", "D", "B")

user_guesses = []

score = 0 

question_number = 0


for question in questions:
    print()
    print(question)
    for option in options[question_number]:
        print(option)
        
    user_guess = input("Enter (A, B, C, D): ").upper()
    user_guesses.append(user_guess)
    if user_guess == answers[question_number]:
        score += 1
        print("Correct! ")
    else: 
        print(f"Sorry, the answer was {answers[question_number]}. " )
    
    
    question_number += 1
    
    
    
print()
print()
    

        
        
        
score = float(score / len(questions) * 100)


print(f"You got {score}% answers correct.")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        