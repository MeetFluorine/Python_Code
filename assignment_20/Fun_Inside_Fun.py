def Check(x):
    if x%2==0:
        DisplayEven()
    else:
        DisplayOdd()

def DisplayEven():
    print("Even")

def DisplayOdd():
    print("Odd")


x= int(input("Enter a number:-"))
Check(x)