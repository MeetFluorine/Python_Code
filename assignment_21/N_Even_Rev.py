def Gen_Even_Rev(n):
    if n!=1:
        print(2*(n-1))
        Gen_Even_Rev(n-1)

Gen_Even_Rev(int(input("enter a last number:-")))