# in this file various aerodynamic functions will be defined as I need'em


# evaluates the Reynolds number
def Re(U, L, nu):
    return U*L/nu


# checks the system Re against a design one and proposes new values
def checkRe(Red, U, L, nu):
    options = ("1. Velocity", "2. Length", "3. Viscosity", "4. I'd like to use this Reynolds anyway")
    if Red != U*L/nu:
        print("The Reynolds is different from the design one. What would you like to change?\n")
        for i in options:
            print(i)
        choice = input()

        if choice == '1':
            Un = Red*nu/L
            return Re(Un, L, nu), Un, L, nu
        elif choice == '2':
            Ln = Red*nu/U
            return Re(U, Ln, nu), U, Ln, nu
        elif choice == '3':
            nuN = U*L/Red
            return Re(U, L, nuN), U, L, nuN
        elif choice == '4':
            return Red, U, L, nu



