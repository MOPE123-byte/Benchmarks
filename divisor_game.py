# Name: Mohmmad Parvez
# Collaborators: 
# Notes: 


def valid_integers(rules):
    while True:
        value = input(rules)
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
        print("Invalid input. Enter a positive integer.")

def take_turns():
    n = valid_integers("Enter a positive integer : ") 
    numbers = list(range(1, n + 1)) 
    current_player = 1
    while len(numbers) > 0:
        print(f"Remaining numbers: {numbers}")
        player_input = valid_integers(f"Player {current_player}, enter a number: ")

        if player_input in numbers:
            numbers = [numb for numb in numbers if numb % player_input != 0]
            current_player = 3 - current_player  
        else:
            print("Invalid move. Only choose a number from the remaining list.")

    print(f"Player {current_player} wins!")

take_turns()

    


