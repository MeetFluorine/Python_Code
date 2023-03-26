def Gen_Odd(n,count=1):
    if count<=n:
        print(2*(count-1))
        Gen_Odd(n,count+1)
    
Gen_Odd(int(input("enter a last number:-")))
