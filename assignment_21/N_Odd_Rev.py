def Gen_Odd_Rev(n):
    if n>=1:
        print(2*n-1)
        Gen_Odd_Rev(n-1)

Gen_Odd_Rev(int(input("enter a last number:-")))