def Re(U, L, nu):
    return U*L/nu

def checkRe(Red, U, L, nu):
    options = ('1. Velocity', '2. Length', '3. Viscosity', "4. I'd like to use this Reynolds anyway")
    if Re(U, L, nu) != Red:
        print("The Reynolds number of your system isn't the design one. What would you like to change?\n")
        for i in options:
            print(i)
        choice = int(input())

        if choice == 1:
            U = Red*nu/L
        elif choice == 2:
            L = Red*nu/U
        elif choice == 3:
            nu = U*L/Red
        elif choice != 4:
            print('User input error: Invalid option')
            return -1

        return Re(U, L, nu), U, L, nu
    else:
        return Re(U, L, nu), U, L, nu
