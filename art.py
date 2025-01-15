# Name: Mohmmad Parvez
# Collaboraters: None
# The second body/portion of code is designated for the challenge problem




print("Enter a Parabola in the form y = ax^2 + bx + c.")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

x = - b / (2 * a)
y = (a * x ** 2) + (b * x) + c

print("The vertex is", (x , y)) #Algorithm for original first problem


print()
print()




print("Enter a Parabola in the form y = ax^2 + bx + c.")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

x = - b / (2 * a)                     #Challenge Problem
y = (a * x ** 2) + (b * x) + c


if (a <= 0):
    print("The program is not a parabola.")
    
else:
    print("The vertex is", (x , y)) 








