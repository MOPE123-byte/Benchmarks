# Name: Mohmmad Parvez
# Collaborators: None
# Notes: 

def is_valid_isbn(isbn):
    
    isbn = isbn.replace("-", "")
    if not isbn.isdigit() or len(isbn) != 13:
        return ("ISBN must be a 13-digit code.")

    
    total = sum(int(isbn[i]) * (3 if i % 2 == 1 else 1) for i in range(13))

    
    if total % 10 == 0:
        return "Valid ISBN"
    else:
        return "Invalid ISBN"

isbn = input("Enter a 13-digit ISBN: ")

result = is_valid_isbn(isbn)
print(result)