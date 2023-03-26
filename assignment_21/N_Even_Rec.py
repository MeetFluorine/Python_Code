def Gen_Odd(n,count=2):
    if count<=n+1:
        print(2*(count-1))
        Gen_Odd(n,count+1)
    
Gen_Odd(int(input("enter a last number:-")))