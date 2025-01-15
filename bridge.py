# Name: Mohmmad Parvez
# 
# Notes: Attempted challenge problem

def evaluate_bridge_hand(hand):
    # Define the values of the cards
    card_values = {'A': 4, 'K': 3, 'Q': 2, 'J': 1, 'T': 0}

    # Set variables to count HCP and the shape of the hand
    hcp = 0
    shape = [0, 0, 0, 0]  # Four suits: Spades, Hearts, Diamonds, Clubs

    # Remove spaces and make the input case-insensitive
    hand = hand.replace(" ", "").upper()

    # Check if the input has exactly 13 characters
    if len(hand) != 13:
        return "Invalid hand."

    for card in hand:
        if card in card_values:
            # If the card is a high card, add its value to HCP
            hcp += card_values[card]
        elif card.isdigit() and card != '0':
            # If the card is a digit (2-9), update the shape of the hand
            suit_index = (int(card) - 1) % 4  # Calculate the suit index
            shape[suit_index] += 1
        elif card != 'X':
            # If an invalid character is encountered, return an error message
            return "Invalid hand."

    # Format and print the results 
    result = f"{hcp} HCP\n{'='.join(map(str, shape))}"
    return result

# Ask the user to enter a bridge hand
hand = input("Enter a bridge hand: ")



print(evaluate_bridge_hand(hand))
