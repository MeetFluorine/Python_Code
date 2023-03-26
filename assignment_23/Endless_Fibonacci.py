def Fibonacci():
    x,y=0,1
    while True:
        yield x
        x,y=y,x+y

it= Fibonacci()

fib_list=[]
# ans= input("Do you want to generate more(y/n):-")
while True:
    ans= input("Do you want to generate more(y/n):-")
    if ans=='y':
        x= next(it)
        print(x)
        fib_list.append(x)
    else:
        break
print("list of fibonacci series generated by you is ",fib_list)
